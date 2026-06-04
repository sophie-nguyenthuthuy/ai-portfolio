"""Tests for the calculator, retriever, web_search tools, and the registry."""

from __future__ import annotations

import pytest

from agent.config import Settings
from agent.data import load_corpus
from agent.tools import (
    CalculatorTool,
    FakeSearch,
    RetrieverTool,
    safe_eval,
)


def test_safe_eval_arithmetic():
    assert safe_eval("2 * (3 + 4)") == 14.0
    assert safe_eval("10 / 4") == 2.5
    assert safe_eval("2 ^ 8") == 256.0  # caret normalized to power


def test_safe_eval_rejects_names_and_calls():
    for bad in ["__import__('os')", "x + 1", "len([1,2])", "1; 2"]:
        with pytest.raises(ValueError):
            safe_eval(bad)


def test_calculator_tool_renders_int():
    res = CalculatorTool()("3 * 7")
    assert res.observation == "21"


def test_calculator_tool_error_is_caught():
    res = CalculatorTool()("frobnicate(2)")
    assert res.observation.startswith("error:")


def test_retriever_finds_relevant_chunk():
    chunks = load_corpus(Settings())
    tool = RetrieverTool(chunks, top_k=3)
    res = tool("What is retrieval augmented generation and citing sources?")
    assert res.observation != "no_results"
    assert res.sources
    # The top hit should come from the RAG document.
    assert any("rag.md" in s["title"] for s in res.sources)


def test_retriever_no_results_on_gibberish():
    chunks = load_corpus(Settings())
    tool = RetrieverTool(chunks, top_k=3)
    res = tool("zzqq xxyy plover")
    assert res.observation == "no_results"


def test_fake_search_is_deterministic():
    search = FakeSearch()
    a = search("latest agent news")
    b = search("latest agent news")
    assert a.observation == b.observation
    assert a.sources and a.sources[0]["origin"] == "web_search"


def test_fake_search_canned():
    search = FakeSearch(canned={"mars": "Mars is the fourth planet."})
    res = search("How big is Mars today?")
    assert "Mars is the fourth planet." in res.observation


def test_registry_dispatch(registry):
    assert set(registry.names()) == {"calculator", "retriever", "web_search"}
    assert registry.run("calculator", "1 + 1").observation == "2"
    assert registry.run("unknown_tool", "x").observation.startswith("error:")
