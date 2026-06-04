"""Local knowledge corpus: load bundled .md docs (or synthesize a fallback).

The corpus is intentionally tiny and self-contained so the retriever tool works
offline with base deps only. Each document is split into paragraph "chunks".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .config import Settings, get_settings

# A small synthetic corpus used when no .md files are present on disk.
_SYNTHETIC_DOCS: dict[str, str] = {
    "agents.md": (
        "# AI Agents\n\n"
        "An AI agent is a system that perceives its environment and takes actions "
        "to achieve goals. Modern LLM agents follow a plan-act-observe-reflect loop.\n\n"
        "The ReAct pattern interleaves reasoning traces with tool actions, letting "
        "the model decide which tool to call next based on prior observations.\n\n"
        "Agents stop when they reach a final answer or exhaust a step budget."
    ),
    "rag.md": (
        "# Retrieval Augmented Generation\n\n"
        "Retrieval augmented generation (RAG) grounds an LLM answer in retrieved "
        "documents, reducing hallucination by citing sources.\n\n"
        "A retriever ranks corpus chunks by similarity to the query, typically with "
        "cosine similarity over embeddings or a keyword overlap score.\n\n"
        "RAG pipelines pass the top-k chunks into the prompt as context."
    ),
    "evaluation.md": (
        "# Evaluating Agents\n\n"
        "Agent evaluation tracks task success, the number of steps taken, and which "
        "tools were used. Fewer steps to a correct answer is generally better.\n\n"
        "Tool-usage distribution drift can signal a regression: if an agent suddenly "
        "calls the calculator far more often, behavior has changed.\n\n"
        "Population Stability Index (PSI) quantifies how much a distribution shifts."
    ),
}


@dataclass(frozen=True)
class Chunk:
    """A retrievable unit of text with provenance."""

    doc: str  # source file name (e.g. "rag.md")
    title: str  # human title (first heading or the doc name)
    text: str  # the chunk body

    @property
    def tokens(self) -> list[str]:
        return _tokenize(self.text)


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _title_of(doc_name: str, body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ").strip()
    return doc_name


def _split_chunks(doc_name: str, body: str) -> list[Chunk]:
    title = _title_of(doc_name, body)
    chunks: list[Chunk] = []
    for para in re.split(r"\n\s*\n", body):
        clean = para.strip()
        if not clean or clean.startswith("#") and len(clean.splitlines()) == 1:
            continue
        chunks.append(Chunk(doc=doc_name, title=title, text=clean))
    return chunks


def synthetic_corpus() -> list[Chunk]:
    """Return the in-memory fallback corpus as a flat list of chunks."""
    chunks: list[Chunk] = []
    for name, body in _SYNTHETIC_DOCS.items():
        chunks.extend(_split_chunks(name, body))
    return chunks


def load_corpus(settings: Settings | None = None) -> list[Chunk]:
    """Load .md docs from ``settings.corpus_dir``; fall back to the synthetic set.

    Returns a flat list of paragraph-level :class:`Chunk` objects.
    """
    settings = settings or get_settings()
    corpus_dir: Path = settings.resolved_corpus_dir

    chunks: list[Chunk] = []
    if corpus_dir.exists():
        for md in sorted(corpus_dir.glob("*.md")):
            body = md.read_text(encoding="utf-8")
            chunks.extend(_split_chunks(md.name, body))

    if not chunks:
        chunks = synthetic_corpus()
    return chunks
