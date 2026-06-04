"""Integration tests for optional backends; skipped unless the dep is present.

These never run in the default offline `pytest -q` (the heavy libs are not
installed), keeping the base suite green on a laptop.
"""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_sentence_transformers_embedder():
    pytest.importorskip("sentence_transformers")
    from ragbot.config import Settings
    from ragbot.embeddings import build_embedder

    settings = Settings(embedder="sentence-transformers")
    emb = build_embedder(settings)
    vecs = emb.embed(["nghi phep", "hoan tien"])
    assert vecs.shape[0] == 2
    assert emb.dim > 0


@pytest.mark.integration
def test_qdrant_store_roundtrip():
    pytest.importorskip("qdrant_client")
    from ragbot.config import Settings
    from ragbot.data import build_chunks, synthetic_corpus
    from ragbot.embeddings import build_embedder
    from ragbot.store import build_store

    settings = Settings(vector_store="qdrant")
    emb = build_embedder(settings)
    store = build_store(settings, emb.dim)
    chunks = build_chunks(synthetic_corpus())
    store.upsert(chunks, emb.embed([c.text for c in chunks]))
    assert store.count() >= 1


@pytest.mark.integration
def test_ragas_available():
    pytest.importorskip("ragas")
    import ragas  # noqa: F401


@pytest.mark.integration
def test_ollama_generation():
    pytest.importorskip("httpx")
    import httpx

    from ragbot.config import Settings
    from ragbot.llm import build_llm, build_prompt

    settings = Settings(llm="ollama")
    llm = build_llm(settings)
    try:
        out = llm.generate(build_prompt("xin chao", "ngu canh thu nghiem"))
    except (httpx.HTTPError, OSError) as exc:  # server not running
        pytest.skip(f"Ollama server unavailable: {exc}")
    assert isinstance(out, str)
