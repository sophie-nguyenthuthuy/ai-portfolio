"""LLM clients.

Two interchangeable implementations behind a single :class:`LLMClient` protocol:

* :class:`FakeLLM` — deterministic, offline, used in ALL tests and as the default
  pipeline backend. It does not call any network. Given the agent scratchpad it
  decides the next tool action (a ``TOOL: <name> | <input>`` directive) using
  simple, explainable heuristics, and synthesizes a final answer purely from the
  observations collected so far.
* :class:`OllamaLLM` — calls a local Ollama server over HTTP via httpx. Imported
  and used only when ``settings.llm_backend == "ollama"``; never touched in tests.

Both return a plain string. The agent loop interprets a leading ``TOOL:`` line as
a tool directive and anything else (or a ``FINAL:`` line) as a final answer.
"""

from __future__ import annotations

import re
from typing import Protocol, runtime_checkable

from .config import Settings, get_settings

# Marker conventions the agent loop understands.
TOOL_PREFIX = "TOOL:"
FINAL_PREFIX = "FINAL:"

# Words that hint at arithmetic in the question.
_ARITH_RE = re.compile(r"[-+*/^]|\b\d+\b|\bcalculate\b|\bcompute\b|\bsum\b|\bproduct\b")
_EXPR_RE = re.compile(r"[-+*/().\d\s^]{3,}")


@runtime_checkable
class LLMClient(Protocol):
    """Minimal text-in / text-out interface."""

    def complete(self, prompt: str) -> str:  # pragma: no cover - protocol
        ...


def build_prompt(question: str, scratchpad: str, plan: list[str]) -> str:
    """Render the agent prompt shared by all backends."""
    plan_block = "\n".join(f"- {p}" for p in plan) if plan else "(no plan yet)"
    obs_block = scratchpad or "(no observations yet)"
    return (
        "You are a research agent. Use tools to gather evidence, then answer.\n"
        "Available tools: calculator, retriever, web_search.\n"
        "Respond with exactly one line, either:\n"
        f"  {TOOL_PREFIX} <tool_name> | <tool_input>\n"
        f"  {FINAL_PREFIX} <answer>\n\n"
        f"Question: {question}\n"
        f"Plan:\n{plan_block}\n\n"
        f"Observations so far:\n{obs_block}\n"
    )


class FakeLLM:
    """Deterministic test/offline LLM.

    The ``complete`` method is stateless; it inspects the prompt (which embeds the
    question, plan, and accumulated observations) and returns the next directive.
    """

    def complete(self, prompt: str) -> str:
        question = _extract_field(prompt, "Question:")
        observations = _extract_block(prompt, "Observations so far:")
        called = _tools_already_called(observations)

        q_lower = question.lower()

        # 1) Arithmetic questions -> calculator first.
        if "calculator" not in called and self._looks_arithmetic(question):
            expr = self._extract_expression(question)
            if expr:
                return f"{TOOL_PREFIX} calculator | {expr}"

        # 2) Always try to ground the answer in the local corpus.
        if "retriever" not in called:
            return f"{TOOL_PREFIX} retriever | {question}"

        # 3) If the corpus was thin, reach for web search once.
        if "web_search" not in called and self._needs_web(q_lower, observations):
            return f"{TOOL_PREFIX} web_search | {question}"

        # 4) Otherwise synthesize a final answer from observations.
        return f"{FINAL_PREFIX} {self.synthesize(question, observations)}"

    # ------------------------------------------------------------------ #
    def synthesize(self, question: str, observations: str) -> str:
        """Compose a cited answer purely from gathered observations."""
        facts = _observation_payloads(observations)
        if not facts:
            return f"I could not find evidence to answer: {question}"
        # Lead with any calculator result, then the strongest retrieved facts.
        calc = [f for tool, f in facts if tool == "calculator"]
        text = [f for tool, f in facts if tool != "calculator"]
        parts: list[str] = []
        if calc:
            parts.append(f"The computed result is {calc[0]}.")
        if text:
            joined = " ".join(text[:2])
            parts.append(joined)
        return " ".join(parts) if parts else f"Based on the evidence: {facts[0][1]}"

    # ------------------------------------------------------------------ #
    @staticmethod
    def _looks_arithmetic(question: str) -> bool:
        return bool(_ARITH_RE.search(question.lower())) and any(
            ch.isdigit() for ch in question
        )

    @staticmethod
    def _extract_expression(question: str) -> str | None:
        candidates = _EXPR_RE.findall(question)
        candidates = [c.strip() for c in candidates if any(ch.isdigit() for ch in c)]
        if not candidates:
            return None
        # Prefer the longest arithmetic-looking span.
        return max(candidates, key=len)

    @staticmethod
    def _needs_web(q_lower: str, observations: str) -> bool:
        # Heuristic: explicit "latest/news" intent, or retriever returned nothing.
        wants_fresh = any(w in q_lower for w in ("latest", "news", "today", "current"))
        retriever_empty = "no_results" in observations
        return wants_fresh or retriever_empty


class OllamaLLM:  # pragma: no cover - network path, never exercised in tests
    """Local Ollama backend (lazy httpx usage, no module-level import of httpx)."""

    def __init__(self, settings: Settings) -> None:
        self.base_url = settings.ollama_base_url.rstrip("/")
        self.model = settings.ollama_model
        self.timeout = settings.llm_timeout_s

    def complete(self, prompt: str) -> str:
        import httpx  # lazy: keeps import surface light, only needed at call time

        resp = httpx.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return str(resp.json().get("response", "")).strip()


def build_llm(settings: Settings | None = None) -> LLMClient:
    """Factory: pick the LLM backend from settings (defaults to FakeLLM)."""
    settings = settings or get_settings()
    if settings.llm_backend == "ollama":
        return OllamaLLM(settings)
    return FakeLLM()


# ---------------------------------------------------------------------- #
# prompt parsing helpers (shared, pure functions)
# ---------------------------------------------------------------------- #
def _extract_field(prompt: str, label: str) -> str:
    for line in prompt.splitlines():
        if line.startswith(label):
            return line[len(label) :].strip()
    return ""


def _extract_block(prompt: str, label: str) -> str:
    """Return everything after a ``label`` line to the end of the prompt."""
    idx = prompt.find(label)
    if idx == -1:
        return ""
    return prompt[idx + len(label) :].strip()


def _tools_already_called(observations: str) -> set[str]:
    return set(re.findall(r"^([a-z_]+)\(", observations, flags=re.MULTILINE))


def _observation_payloads(observations: str) -> list[tuple[str, str]]:
    """Parse ``tool(input) -> payload`` lines into (tool, payload) pairs."""
    pairs: list[tuple[str, str]] = []
    for line in observations.splitlines():
        m = re.match(r"^([a-z_]+)\(.*?\)\s*->\s*(.*)$", line.strip())
        if m:
            payload = m.group(2).strip()
            if payload and payload != "no_results":
                pairs.append((m.group(1), payload))
    return pairs
