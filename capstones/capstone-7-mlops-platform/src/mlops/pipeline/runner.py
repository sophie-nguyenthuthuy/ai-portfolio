"""A small, dependency-free DAG executor for orchestrating pipeline stages.

This is the default ``base`` orchestration backend. It models a flow as a set of
named ``Stage`` callables with declared upstream dependencies, validates the DAG
(no cycles, all deps known), computes a topological order, and runs each stage
exactly once — passing a shared mutable ``context`` dict between them. Stage
return values are merged into the context so downstream stages can consume them.

It is intentionally tiny and deterministic so unit tests can assert execution
order without any external orchestrator. The optional Prefect flow
(``mlops.pipeline.prefect_flow``) mirrors the same stage graph.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from ..logging_conf import get_logger

logger = get_logger(__name__)

# A stage receives the shared context and returns a dict merged back into it.
StageFn = Callable[[dict[str, Any]], dict[str, Any] | None]


class PipelineError(RuntimeError):
    """Raised on invalid DAGs or failing stages."""


@dataclass
class Stage:
    """A named unit of work with declared upstream dependencies."""

    name: str
    fn: StageFn
    depends_on: tuple[str, ...] = ()


@dataclass
class StageRun:
    """Record of a single executed stage."""

    name: str
    status: str  # "success" | "failed"
    output: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


@dataclass
class PipelineRun:
    """Result of a full pipeline execution."""

    order: list[str]
    stage_runs: list[StageRun]
    context: dict[str, Any]
    success: bool

    def output(self, key: str, default: Any = None) -> Any:
        return self.context.get(key, default)


class Pipeline:
    """A DAG of stages executed in topological order with a shared context."""

    def __init__(self, name: str = "pipeline") -> None:
        self.name = name
        self._stages: dict[str, Stage] = {}

    def add_stage(
        self,
        name: str,
        fn: StageFn,
        depends_on: tuple[str, ...] | list[str] = (),
    ) -> Pipeline:
        """Register a stage; returns self for chaining."""
        if name in self._stages:
            raise PipelineError(f"duplicate stage: {name!r}")
        self._stages[name] = Stage(name=name, fn=fn, depends_on=tuple(depends_on))
        return self

    def topological_order(self) -> list[str]:
        """Kahn's algorithm — raises PipelineError on unknown deps or cycles."""
        indeg: dict[str, int] = {n: 0 for n in self._stages}
        adj: dict[str, list[str]] = {n: [] for n in self._stages}
        for stage in self._stages.values():
            for dep in stage.depends_on:
                if dep not in self._stages:
                    raise PipelineError(f"stage {stage.name!r} depends on unknown stage {dep!r}")
                adj[dep].append(stage.name)
                indeg[stage.name] += 1

        # Deterministic ordering: sort the zero-indegree frontier by name.
        queue: deque[str] = deque(sorted(n for n, d in indeg.items() if d == 0))
        order: list[str] = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in sorted(adj[node]):
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(self._stages):
            raise PipelineError("cycle detected in pipeline DAG")
        return order

    def run(self, context: dict[str, Any] | None = None) -> PipelineRun:
        """Execute all stages in topological order."""
        ctx: dict[str, Any] = dict(context or {})
        order = self.topological_order()
        runs: list[StageRun] = []
        logger.info("pipeline start", extra={"pipeline": self.name, "order": order})

        for name in order:
            stage = self._stages[name]
            try:
                out = stage.fn(ctx) or {}
                if not isinstance(out, dict):
                    raise PipelineError(f"stage {name!r} must return a dict or None")
                ctx.update(out)
                runs.append(StageRun(name=name, status="success", output=out))
                logger.info("stage ok", extra={"stage": name})
            except Exception as exc:  # noqa: BLE001 - we record and stop the flow
                runs.append(StageRun(name=name, status="failed", error=str(exc)))
                logger.error("stage failed", extra={"stage": name, "error": str(exc)})
                return PipelineRun(order=order, stage_runs=runs, context=ctx, success=False)

        return PipelineRun(order=order, stage_runs=runs, context=ctx, success=True)
