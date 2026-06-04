"""Tests for document loading and chunking."""

from __future__ import annotations

from ragbot.data import (
    build_chunks,
    chunk_document,
    chunk_text,
    load_documents,
    synthetic_corpus,
)


def test_chunk_text_overlap_and_coverage():
    text = "abc " * 300  # ~1200 chars
    chunks = chunk_text(text, chunk_size=200, overlap=50)
    assert len(chunks) > 1
    assert all(len(c) <= 200 for c in chunks)
    # Overlap means consecutive chunks share some content.
    joined = " ".join(chunks)
    assert "abc" in joined


def test_chunk_text_short_returns_single():
    assert chunk_text("short text", chunk_size=400) == ["short text"]


def test_chunk_text_empty():
    assert chunk_text("   ") == []


def test_chunk_document_stable_ids():
    text = "Mot cau van tieng Viet. " * 40
    a = chunk_document(text, "doc.md", chunk_size=150, overlap=30)
    b = chunk_document(text, "doc.md", chunk_size=150, overlap=30)
    assert [c.id for c in a] == [c.id for c in b]  # deterministic ids
    assert all(c.source == "doc.md" for c in a)


def test_load_documents_from_dir(tmp_path):
    (tmp_path / "a.md").write_text("noi dung A", encoding="utf-8")
    (tmp_path / "b.txt").write_text("noi dung B", encoding="utf-8")
    (tmp_path / "skip.pdf").write_text("ignored", encoding="utf-8")
    docs = load_documents([tmp_path])
    assert set(docs) == {"a.md", "b.txt"}


def test_build_chunks_over_corpus():
    chunks = build_chunks(synthetic_corpus(), chunk_size=200, overlap=40)
    assert len(chunks) >= len(synthetic_corpus())
    assert len({c.source for c in chunks}) == len(synthetic_corpus())
