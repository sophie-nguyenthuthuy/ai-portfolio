"""Shared fixtures: offline Settings, a built RAG pipeline, and an API client."""

from __future__ import annotations

import pytest

from ragbot.config import Settings
from ragbot.pipeline import RAGPipeline


@pytest.fixture(scope="session")
def settings() -> Settings:
    """Fully offline settings: hashing embedder, in-memory store, fake LLM."""
    return Settings(
        embedder="hashing",
        embedding_dim=512,
        vector_store="memory",
        llm="fake",
        top_k=4,
        hybrid=True,
    )


@pytest.fixture()
def pipeline(settings) -> RAGPipeline:
    """A RAG pipeline pre-loaded with the bundled sample corpus."""
    pipe = RAGPipeline(settings)
    pipe.ingest_sample_corpus()
    return pipe


@pytest.fixture()
def client(settings):
    """FastAPI TestClient; lifespan ingests the sample corpus on startup."""
    from fastapi.testclient import TestClient

    from ragbot.api import main as api_main

    with TestClient(api_main.app) as c:
        yield c
    api_main.STATE["pipeline"] = None
