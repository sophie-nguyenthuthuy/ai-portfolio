"""Tests for the base DAG runner and the end-to-end reference flow."""

from __future__ import annotations

import pytest

from mlops.pipeline import STAGE_ORDER, Pipeline, PipelineError, build_pipeline
from mlops.pipeline.flow import run_flow


# ---- the generic DAG runner ----
def test_runner_executes_in_topological_order():
    calls: list[str] = []

    def make(name):
        def fn(ctx):
            calls.append(name)
            return {name: True}

        return fn

    p = Pipeline("t")
    p.add_stage("c", make("c"), depends_on=["a", "b"])
    p.add_stage("a", make("a"))
    p.add_stage("b", make("b"), depends_on=["a"])

    run = p.run()
    assert run.success is True
    # a before b before c; deterministic frontier ordering.
    assert calls == ["a", "b", "c"]
    assert run.order == ["a", "b", "c"]
    assert run.context["c"] is True


def test_runner_detects_cycle():
    p = Pipeline("cyc")
    p.add_stage("a", lambda ctx: None, depends_on=["b"])
    p.add_stage("b", lambda ctx: None, depends_on=["a"])
    with pytest.raises(PipelineError, match="cycle"):
        p.topological_order()


def test_runner_unknown_dependency():
    p = Pipeline("u")
    p.add_stage("a", lambda ctx: None, depends_on=["missing"])
    with pytest.raises(PipelineError, match="unknown"):
        p.topological_order()


def test_runner_stops_on_failure():
    seen: list[str] = []

    def boom(ctx):
        raise RuntimeError("kaboom")

    p = Pipeline("f")
    p.add_stage("ok", lambda ctx: seen.append("ok") or {})
    p.add_stage("bad", boom, depends_on=["ok"])
    p.add_stage("never", lambda ctx: seen.append("never") or {}, depends_on=["bad"])

    run = p.run()
    assert run.success is False
    assert "never" not in seen
    assert run.stage_runs[-1].status == "failed"


def test_reference_pipeline_stage_graph():
    p = build_pipeline()
    assert p.topological_order() == STAGE_ORDER


# ---- the real reference flow (base backend) ----
def test_full_flow_trains_registers_and_deploys(settings):
    run = run_flow(settings)
    assert run.success is True
    assert run.order == STAGE_ORDER
    assert run.context["metrics"]["roc_auc"] > 0.7
    assert run.context["registered_version"] == 1
    assert run.context["deployed"] is True
    assert run.context["stage"] == "Production"

    # The flow promoted version 1 to Production in the registry.
    from mlops.registry import get_registry

    reg = get_registry(settings)
    cur = reg.current("Production")
    assert cur is not None and cur.version == 1


def test_flow_parks_in_staging_when_metric_floor_not_met(settings):
    # Impossible floor -> deploy-check should park in Staging, not Production.
    strict = settings.model_copy(update={"min_roc_auc": 1.5})
    run = run_flow(strict)
    assert run.success is True
    assert run.context["deployed"] is False
    assert run.context["stage"] == "Staging"
