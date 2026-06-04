"""Shared fixtures: offline Settings, FakeLLM/FakeSearch graph, and a TestClient."""

from __future__ import annotations

import pytest

from agent.config import Settings
from agent.graph import build_graph
from agent.llm import FakeLLM
from agent.tools import build_registry


@pytest.fixture(scope="session")
def settings() -> Settings:
    """Fully offline settings: SimpleGraph + FakeLLM + FakeSearch."""
    return Settings(
        graph_backend="simple",
        llm_backend="fake",
        search_backend="fake",
        max_steps=6,
        retriever_top_k=3,
    )


@pytest.fixture(scope="session")
def registry(settings):
    return build_registry(settings)


@pytest.fixture(scope="session")
def fake_llm() -> FakeLLM:
    return FakeLLM()


@pytest.fixture(scope="session")
def graph(settings, fake_llm, registry):
    return build_graph(settings, llm=fake_llm, registry=registry)


@pytest.fixture
def client(settings):
    """FastAPI TestClient with the graph preloaded via lifespan (offline backends)."""
    from fastapi.testclient import TestClient

    from agent.api import main as api_main

    # Force offline backends regardless of ambient env.
    api_main.get_settings.cache_clear()
    with TestClient(api_main.app) as c:
        yield c
    api_main.STATE["graph"] = None
