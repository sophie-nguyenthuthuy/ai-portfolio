"""Agent tools: a ``Tool`` protocol, a registry, and three real implementations.

* ``calculator``  — safe arithmetic evaluation over a restricted AST (no eval()).
* ``retriever``   — ranks the bundled local corpus by cosine similarity over a
                    deterministic hashing vectorizer, with a keyword-overlap
                    tie-break. numpy only; no embeddings download.
* ``web_search``  — uses a deterministic :class:`FakeSearch` by default. A real
                    Tavily-backed implementation is provided but lazy/optional and
                    is never invoked in tests.

Each tool returns a :class:`ToolResult` carrying the human observation string and
optional structured sources for citation.
"""

from __future__ import annotations

import ast
import math
import operator
import re
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

import numpy as np

from .config import Settings, get_settings
from .data import Chunk, load_corpus


@dataclass
class ToolResult:
    """Outcome of a tool call."""

    observation: str
    sources: list[dict[str, str]] = field(default_factory=list)


@runtime_checkable
class Tool(Protocol):
    """A callable tool with a stable name and description."""

    name: str
    description: str

    def __call__(self, tool_input: str) -> ToolResult:  # pragma: no cover - protocol
        ...


# ---------------------------------------------------------------------- #
# calculator
# ---------------------------------------------------------------------- #
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def safe_eval(expression: str) -> float:
    """Evaluate a pure arithmetic expression without using ``eval``.

    Supports + - * / // % ** and parentheses. Raises ``ValueError`` on anything
    outside that grammar (names, calls, attribute access, etc.).
    """
    # Normalize a caret to Python power for convenience.
    expression = expression.replace("^", "**")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"invalid expression: {expression!r}") from exc
    return _eval_node(tree.body)


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("only numeric literals are allowed")
        return float(node.value)
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _BIN_OPS:
            raise ValueError(f"operator not allowed: {op_type.__name__}")
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        result = _BIN_OPS[op_type](left, right)
        if math.isinf(result) or math.isnan(result):
            raise ValueError("non-finite result")
        return float(result)
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _UNARY_OPS:
            raise ValueError(f"unary operator not allowed: {op_type.__name__}")
        return float(_UNARY_OPS[op_type](_eval_node(node.operand)))
    raise ValueError(f"unsupported syntax: {type(node).__name__}")


class CalculatorTool:
    name = "calculator"
    description = "Evaluate a pure arithmetic expression, e.g. '2 * (3 + 4)'."

    def __call__(self, tool_input: str) -> ToolResult:
        try:
            value = safe_eval(tool_input.strip())
        except ValueError as exc:
            return ToolResult(observation=f"error: {exc}")
        # Render integers without a trailing .0 for readability.
        rendered = str(int(value)) if value == int(value) else f"{value:.6g}"
        return ToolResult(observation=rendered)


# ---------------------------------------------------------------------- #
# retriever
# ---------------------------------------------------------------------- #
def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _hash_vector(tokens: list[str], dim: int = 256) -> np.ndarray:
    """Deterministic hashing-trick bag-of-words vector (no model download)."""
    vec = np.zeros(dim, dtype=np.float64)
    for tok in tokens:
        # signed hashing trick keeps it stable and collision-tolerant
        h = hash_token(tok)
        vec[h % dim] += 1.0 if (h // dim) % 2 == 0 else -1.0
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec


def hash_token(token: str) -> int:
    """Stable (cross-run) hash for a token using a simple FNV-1a."""
    h = 0x811C9DC5
    for ch in token.encode("utf-8"):
        h ^= ch
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


class RetrieverTool:
    name = "retriever"
    description = "Search the local knowledge corpus and return the top matching passages."

    def __init__(self, chunks: list[Chunk], top_k: int = 3, dim: int = 256) -> None:
        self.chunks = chunks
        self.top_k = top_k
        self.dim = dim
        self._matrix = np.vstack(
            [_hash_vector(c.tokens, dim) for c in chunks]
        ) if chunks else np.zeros((0, dim))

    def __call__(self, tool_input: str) -> ToolResult:
        if not self.chunks:
            return ToolResult(observation="no_results")
        q_tokens = _tokenize(tool_input)
        q_vec = _hash_vector(q_tokens, self.dim)
        cosine = self._matrix @ q_vec  # rows are unit vectors -> dot == cosine

        # Require real keyword overlap so unrelated queries return no_results
        # (the hashing vectorizer alone can score spurious collisions). Cosine
        # then orders the lexically-relevant chunks.
        q_set = set(q_tokens)
        overlap = np.array(
            [len(q_set & set(c.tokens)) for c in self.chunks], dtype=float
        )
        score = np.where(overlap > 0, overlap + np.maximum(cosine, 0.0), -1.0)

        if float(score.max()) <= 0.0:
            return ToolResult(observation="no_results")

        order = np.argsort(-score)[: self.top_k]
        sources: list[dict[str, str]] = []
        snippets: list[str] = []
        for idx in order:
            if score[idx] <= 0.0:
                continue
            chunk = self.chunks[int(idx)]
            snippet = _first_sentence(chunk.text)
            snippets.append(snippet)
            sources.append(
                {"title": f"{chunk.title} ({chunk.doc})", "snippet": snippet, "origin": "retriever"}
            )
        if not snippets:
            return ToolResult(observation="no_results")
        return ToolResult(observation=" ".join(snippets), sources=sources)


def _first_sentence(text: str) -> str:
    text = " ".join(text.split())
    m = re.match(r"(.*?[.!?])(\s|$)", text)
    return m.group(1) if m else text


# ---------------------------------------------------------------------- #
# web_search
# ---------------------------------------------------------------------- #
class FakeSearch:
    """Deterministic web-search stand-in used in tests and offline runs.

    It returns a stable, query-derived result so the agent's web_search branch is
    exercised without any network access.
    """

    name = "web_search"
    description = "Search the web for up-to-date information (deterministic stub offline)."

    def __init__(self, canned: dict[str, str] | None = None) -> None:
        self.canned = canned or {}

    def __call__(self, tool_input: str) -> ToolResult:
        query = tool_input.strip()
        key = query.lower()
        for canned_key, value in self.canned.items():
            if canned_key.lower() in key:
                return ToolResult(
                    observation=value,
                    sources=[{"title": f"web: {canned_key}", "snippet": value, "origin": "web_search"}],
                )
        # Deterministic synthetic result derived from the query terms.
        terms = ", ".join(_tokenize(query)[:5]) or "the topic"
        snippet = f"Public sources summarize current information about {terms}."
        return ToolResult(
            observation=snippet,
            sources=[{"title": f"web: {query[:40]}", "snippet": snippet, "origin": "web_search"}],
        )


class TavilySearch:  # pragma: no cover - network path, never exercised in tests
    """Real web search via the Tavily API (lazy import; optional)."""

    name = "web_search"
    description = "Search the web for up-to-date information via Tavily."

    def __init__(self, settings: Settings, max_results: int = 3) -> None:
        self.settings = settings
        self.max_results = max_results

    def __call__(self, tool_input: str) -> ToolResult:
        import os

        import httpx

        api_key = os.environ.get("TAVILY_API_KEY", "")
        if not api_key:
            return ToolResult(observation="error: TAVILY_API_KEY not set")
        resp = httpx.post(
            "https://api.tavily.com/search",
            json={"api_key": api_key, "query": tool_input, "max_results": self.max_results},
            timeout=self.settings.llm_timeout_s,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        sources = [
            {"title": r.get("title", ""), "snippet": r.get("content", ""), "origin": "web_search"}
            for r in results
        ]
        observation = " ".join(s["snippet"] for s in sources) or "no_results"
        return ToolResult(observation=observation, sources=sources)


# ---------------------------------------------------------------------- #
# registry
# ---------------------------------------------------------------------- #
class ToolRegistry:
    """Name -> Tool lookup with a guarded dispatch."""

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def names(self) -> list[str]:
        return sorted(self._tools)

    def run(self, name: str, tool_input: str) -> ToolResult:
        tool = self._tools.get(name)
        if tool is None:
            return ToolResult(observation=f"error: unknown tool {name!r}")
        return tool(tool_input)


def build_registry(settings: Settings | None = None) -> ToolRegistry:
    """Assemble the default tool registry (calculator, retriever, web_search)."""
    settings = settings or get_settings()
    registry = ToolRegistry()
    registry.register(CalculatorTool())
    registry.register(
        RetrieverTool(load_corpus(settings), top_k=settings.retriever_top_k)
    )
    if settings.search_backend == "tavily":
        registry.register(TavilySearch(settings))  # pragma: no cover
    else:
        registry.register(FakeSearch())
    return registry
