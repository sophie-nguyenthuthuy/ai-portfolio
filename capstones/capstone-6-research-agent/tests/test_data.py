"""Tests for the corpus loader and synthetic fallback."""

from __future__ import annotations

from agent.config import Settings
from agent.data import Chunk, load_corpus, synthetic_corpus


def test_synthetic_corpus_nonempty():
    chunks = synthetic_corpus()
    assert len(chunks) >= 3
    assert all(isinstance(c, Chunk) for c in chunks)
    assert all(c.text and c.title and c.doc for c in chunks)


def test_load_corpus_from_bundled_docs():
    # Default settings point at data/corpus which ships 3 .md files.
    chunks = load_corpus(Settings())
    docs = {c.doc for c in chunks}
    assert {"agents.md", "rag.md", "evaluation.md"} <= docs


def test_load_corpus_falls_back_when_missing(tmp_path):
    s = Settings(corpus_dir=str(tmp_path / "does-not-exist"))
    chunks = load_corpus(s)
    # Falls back to the synthetic in-memory corpus rather than returning empty.
    assert len(chunks) >= 3


def test_chunk_tokens():
    c = Chunk(doc="x.md", title="X", text="Hello, World! 123")
    assert c.tokens == ["hello", "world", "123"]
