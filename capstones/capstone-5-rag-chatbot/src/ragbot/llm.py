"""LLM clients behind a small protocol.

`FakeLLM` (default/tests) is fully deterministic and never touches the network:
it composes an extractive answer from the retrieved context. `OllamaLLM` calls a
local Ollama server over httpx and is selected only via config.
"""

from __future__ import annotations

import re
from typing import Protocol, runtime_checkable

from .config import Settings
from .logging_conf import get_logger

logger = get_logger(__name__)

PROMPT_TEMPLATE = (
    "Ban la tro ly noi bo. Chi tra loi dua tren NGU CANH duoi day. "
    "Neu khong tim thay cau tra loi trong ngu canh, hay noi ban khong biet.\n\n"
    "NGU CANH:\n{context}\n\n"
    "CAU HOI: {question}\n\n"
    "TRA LOI:"
)


def build_prompt(question: str, context: str) -> str:
    """Render the grounded RAG prompt from a question and retrieved context."""
    return PROMPT_TEMPLATE.format(context=context.strip(), question=question.strip())


@runtime_checkable
class LLMClient(Protocol):
    """Generates a completion for a fully-rendered prompt."""

    def generate(self, prompt: str) -> str: ...


class FakeLLM:
    """Deterministic, offline LLM used in every test.

    It does no generation; it summarises the context block of the prompt into a
    short extractive answer so the full RAG path (retrieve -> prompt -> answer ->
    cite) is exercised without any network call.
    """

    def __init__(self, max_sentences: int = 2) -> None:
        self.max_sentences = max_sentences

    # Matches the "[1] (source.md) " citation prefix added per retrieved chunk.
    _CITATION_RE = re.compile(r"\[\d+\]\s*\([^)]*\)\s*")

    def generate(self, prompt: str) -> str:
        context = self._extract_context(prompt)
        if not context:
            return "Toi khong tim thay thong tin trong tai lieu."
        # Drop citation markers and markdown headings so the answer is pure
        # document content drawn verbatim from the retrieved context.
        cleaned = self._CITATION_RE.sub("", context).replace("#", " ")
        sentences = [s.strip() for s in cleaned.replace("\n", " ").split(".") if s.strip()]
        answer = ". ".join(sentences[: self.max_sentences])
        return (answer + ".") if answer else cleaned[:200].strip()

    @staticmethod
    def _extract_context(prompt: str) -> str:
        if "NGU CANH:" in prompt and "CAU HOI:" in prompt:
            return prompt.split("NGU CANH:", 1)[1].split("CAU HOI:", 1)[0].strip()
        return prompt.strip()


class OllamaLLM:
    """Local Ollama chat client over httpx (selected via RAGBOT_LLM=ollama)."""

    def __init__(self, base_url: str, model: str, timeout: float = 60.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> str:  # pragma: no cover - needs a server
        import httpx  # base dep, imported lazily to keep import-time light

        resp = httpx.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return str(resp.json().get("response", "")).strip()


def build_llm(settings: Settings) -> LLMClient:
    """Factory: pick the LLM backend from settings (default fake)."""
    kind = settings.llm.lower()
    if kind in {"fake", "echo", "offline"}:
        logger.info("using FakeLLM (offline)")
        return FakeLLM()
    if kind == "ollama":
        logger.info(
            "using OllamaLLM",
            extra={"base_url": settings.ollama_base_url, "model": settings.ollama_model},
        )
        return OllamaLLM(settings.ollama_base_url, settings.ollama_model, settings.llm_timeout)
    raise ValueError(f"unknown llm: {settings.llm!r}")
