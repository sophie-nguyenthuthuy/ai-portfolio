"""End-to-end agent tests on the offline SimpleGraph + FakeLLM + FakeSearch stack."""

from __future__ import annotations

import pytest

from agent.graph import SimpleGraph, build_graph
from agent.llm import FakeLLM, build_prompt
from agent.pipeline import run
from agent.state import AgentState


def test_build_graph_defaults_to_simple(settings, fake_llm, registry):
    g = build_graph(settings, llm=fake_llm, registry=registry)
    assert isinstance(g, SimpleGraph)
    assert g.backend == "simple"


def test_run_knowledge_question_cites_sources(settings):
    out = run("What is retrieval augmented generation?", settings=settings)
    assert out["answer"]
    assert out["steps"] >= 1
    assert out["backend"] == "simple"
    # Knowledge question should ground the answer in the retriever corpus.
    assert any(s["origin"] == "retriever" for s in out["sources"])
    assert any(c["tool"] == "retriever" for c in out["tool_calls"])


def test_run_arithmetic_question_uses_calculator(settings):
    out = run("What is 12 * (3 + 4)?", settings=settings)
    tools_used = [c["tool"] for c in out["tool_calls"]]
    assert "calculator" in tools_used
    # The computed value should surface in the answer.
    assert "84" in out["answer"]


def test_run_fresh_question_uses_web_search(settings):
    out = run("What is the latest news on AI agents today?", settings=settings)
    tools_used = [c["tool"] for c in out["tool_calls"]]
    assert "web_search" in tools_used
    assert any(s["origin"] == "web_search" for s in out["sources"])


def test_run_respects_step_budget():
    from agent.config import Settings

    s = Settings(graph_backend="simple", llm_backend="fake", search_backend="fake", max_steps=2)
    out = run("Tell me everything about agents and rag and evaluation forever", settings=s)
    assert out["steps"] <= 2
    assert out["answer"]  # forced synthesis on budget exhaustion


def test_run_rejects_empty_question(settings):
    with pytest.raises(ValueError):
        run("   ", settings=settings)


def test_fake_llm_finishes_after_tools():
    # Drive the FakeLLM directly: once retriever has run, it should not loop forever.
    llm = FakeLLM()
    obs = "retriever(q) -> RAG grounds an LLM answer in retrieved documents."
    prompt = build_prompt("explain rag", obs, ["plan"])
    directive = llm.complete(prompt)
    assert directive.startswith("FINAL:")


def test_state_roundtrip():
    st = AgentState(question="q", max_steps=3)
    st.plan = ["a", "b"]
    st.record_tool_call("calculator", "1+1", "2")
    st.add_source("t", "s", "retriever")
    st.final_answer = "done"
    restored = AgentState.from_dict(st.as_dict())
    assert restored.question == "q"
    assert restored.plan == ["a", "b"]
    assert restored.tool_calls[0].tool == "calculator"
    assert restored.sources[0].origin == "retriever"
    assert restored.final_answer == "done"
