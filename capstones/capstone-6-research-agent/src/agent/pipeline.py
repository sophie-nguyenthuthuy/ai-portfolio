"""High-level orchestration: question -> answer + trace + sources.

This is the single entry point used by the API and the CLI. It builds (or reuses)
a graph, runs the agent loop, and returns a JSON-friendly result.
"""

from __future__ import annotations

from typing import Any

from .config import Settings, get_settings
from .graph import Graph, build_graph
from .logging_conf import get_logger
from .state import AgentState

logger = get_logger(__name__)


def run(
    question: str,
    settings: Settings | None = None,
    graph: Graph | None = None,
) -> dict[str, Any]:
    """Answer ``question`` with the research agent.

    Returns a dict: ``{answer, steps, tool_calls, sources, backend}``.
    Uses FakeLLM + SimpleGraph + FakeSearch by default (fully offline).
    """
    settings = settings or get_settings()
    if not question or not question.strip():
        raise ValueError("question must be a non-empty string")

    graph = graph or build_graph(settings)
    state = AgentState(question=question.strip(), max_steps=settings.max_steps)
    state = graph.run(state)

    backend = getattr(graph, "backend", "unknown")
    result: dict[str, Any] = {
        "question": state.question,
        "answer": state.final_answer or "",
        "steps": state.steps,
        "tool_calls": [c.as_dict() for c in state.tool_calls],
        "sources": _dedupe_sources([s.as_dict() for s in state.sources]),
        "backend": backend,
    }
    logger.info(
        "pipeline run",
        extra={"steps": result["steps"], "n_sources": len(result["sources"])},
    )
    return result


def _dedupe_sources(sources: list[dict[str, str]]) -> list[dict[str, str]]:
    """Drop duplicate citations while preserving order."""
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for src in sources:
        key = (src.get("title", ""), src.get("snippet", ""))
        if key in seen:
            continue
        seen.add(key)
        out.append(src)
    return out
