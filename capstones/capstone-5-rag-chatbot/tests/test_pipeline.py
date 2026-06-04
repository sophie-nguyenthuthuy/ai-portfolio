"""End-to-end RAG: ingest -> retrieve -> answer + sources, plus eval metrics."""

from __future__ import annotations

import numpy as np

from ragbot.embeddings import HashingEmbedder, build_embedder
from ragbot.eval import GOLDEN_SET, evaluate
from ragbot.pipeline import RAGPipeline
from ragbot.store import InMemoryStore


def test_hashing_embedder_unit_norm_and_dim():
    emb = HashingEmbedder(dim=256)
    vecs = emb.embed(["nghi phep", "hoan tien"])
    assert vecs.shape == (2, 256)
    norms = np.linalg.norm(vecs, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-5)


def test_inmemory_store_search_ranks_by_similarity(settings):
    emb = build_embedder(settings)
    store = InMemoryStore(dim=emb.dim)
    from ragbot.data import build_chunks, synthetic_corpus

    chunks = build_chunks(synthetic_corpus(), chunk_size=200, overlap=40)
    store.upsert(chunks, emb.embed([c.text for c in chunks]))
    assert store.count() == len(chunks)
    q = emb.embed(["nghi phep bao nhieu ngay"])[0]
    hits = store.search(q, top_k=3)
    assert len(hits) == 3
    assert hits[0].score >= hits[-1].score  # sorted descending


def test_upsert_dedupes_by_id(settings):
    emb = build_embedder(settings)
    store = InMemoryStore(dim=emb.dim)
    from ragbot.data import build_chunks, synthetic_corpus

    chunks = build_chunks(synthetic_corpus(), chunk_size=200, overlap=40)
    vecs = emb.embed([c.text for c in chunks])
    store.upsert(chunks, vecs)
    store.upsert(chunks, vecs)  # re-upsert same ids
    assert store.count() == len(chunks)


def test_answer_returns_relevant_source(pipeline):
    result = pipeline.answer("Nhan vien duoc bao nhieu ngay nghi phep?")
    assert result["sources"], "expected at least one source"
    top_sources = [s["source"] for s in result["sources"]]
    assert "chinh_sach_nghi_phep.md" in top_sources
    assert isinstance(result["answer"], str) and result["answer"]


def test_answer_grounded_in_context(pipeline):
    # FakeLLM is extractive, so its answer tokens must come from the context.
    from ragbot.retriever import tokenize

    result = pipeline.answer("Khach hang co the hoan tien trong bao lau?")
    context = " ".join(s["text"] for s in result["sources"])
    answer_tokens = set(tokenize(result["answer"]))
    context_tokens = set(tokenize(context))
    assert answer_tokens, "answer should be non-empty"
    # The overwhelming majority of answer tokens must appear in the context.
    overlap = len(answer_tokens & context_tokens) / len(answer_tokens)
    assert overlap >= 0.8


def test_answer_no_results_on_empty_store(settings):
    pipe = RAGPipeline(settings)  # nothing ingested
    result = pipe.answer("bat ky cau hoi nao")
    assert result["sources"] == []
    assert "khong tim thay" in result["answer"].lower()


def test_eval_metrics_are_strong_offline(pipeline):
    report = evaluate(pipeline, cases=GOLDEN_SET)
    metrics = report["metrics"]
    assert metrics["n_cases"] == len(GOLDEN_SET)
    # Hashing + hybrid should retrieve the correct doc for every golden question.
    assert metrics["context_precision"] >= 0.75
    assert 0.0 <= metrics["answer_groundedness"] <= 1.0


def test_ingest_inline_documents(settings):
    pipe = RAGPipeline(settings)
    n = pipe.ingest_texts({"faq.md": "Gio lam viec la tu 9h sang den 18h chieu."})
    assert n >= 1
    result = pipe.answer("Gio lam viec the nao?")
    assert "faq.md" in [s["source"] for s in result["sources"]]
