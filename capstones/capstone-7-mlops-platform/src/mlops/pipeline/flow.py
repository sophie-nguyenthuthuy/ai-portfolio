"""The reference MLOps flow: ingest -> validate -> train -> evaluate -> register -> deploy-check.

`build_pipeline` wires these stages into the base DAG runner (default). The stage
functions are plain callables that read/write the shared context, so the SAME
stage logic is reused by the optional Prefect flow.
"""

from __future__ import annotations

from typing import Any

from ..config import Settings, get_settings
from ..data import load_data, split_features_target
from ..logging_conf import get_logger
from ..train import train_core
from ..validation import validate_dataframe
from .runner import Pipeline, PipelineError

logger = get_logger(__name__)


# ---- individual stage functions (context in, dict out) ----
def stage_ingest(ctx: dict[str, Any]) -> dict[str, Any]:
    settings: Settings = ctx["settings"]
    df = load_data(settings.resolved_data_path, n=settings.synthetic_rows, seed=settings.random_seed)
    return {"raw_df": df, "n_rows": int(len(df))}


def stage_validate(ctx: dict[str, Any]) -> dict[str, Any]:
    report = validate_dataframe(ctx["raw_df"], require_target=True)
    if not report.passed:
        raise PipelineError(f"data validation failed: {report.errors}")
    # Confirm the feature/target split is usable downstream.
    x, y = split_features_target(ctx["raw_df"])
    return {"validation": report.as_dict(), "n_features": x.shape[1]}


def stage_train(ctx: dict[str, Any]) -> dict[str, Any]:
    settings: Settings = ctx["settings"]
    result = train_core(settings, df=ctx["raw_df"])
    return {"train_result": result}


def stage_evaluate(ctx: dict[str, Any]) -> dict[str, Any]:
    settings: Settings = ctx["settings"]
    metrics = ctx["train_result"].metrics
    passed = metrics["roc_auc"] >= settings.min_roc_auc
    return {"metrics": metrics, "eval_passed": passed}


def stage_register(ctx: dict[str, Any]) -> dict[str, Any]:
    from ..registry import get_registry

    settings: Settings = ctx["settings"]
    result = ctx["train_result"]
    reg = get_registry(settings)
    mv = reg.register(result.pipeline, metrics=result.metrics, params=result.params)
    return {"registered_version": mv.version, "registry": reg}


def stage_deploy_check(ctx: dict[str, Any]) -> dict[str, Any]:
    """Gate deployment on the eval metric floor; promote to Production if it passes."""
    from ..registry import PRODUCTION, STAGING

    reg = ctx["registry"]
    version = ctx["registered_version"]
    if ctx["eval_passed"]:
        reg.promote(version, PRODUCTION)
        return {"deployed": True, "stage": PRODUCTION}
    # Below the floor: park in Staging for human review rather than going live.
    reg.promote(version, STAGING)
    return {"deployed": False, "stage": STAGING}


# Canonical stage order, exported for the Prefect flow + tests.
STAGE_ORDER = ["ingest", "validate", "train", "evaluate", "register", "deploy-check"]


def build_pipeline() -> Pipeline:
    """Construct the base-runner DAG for the reference flow."""
    p = Pipeline(name="mlops-reference-flow")
    p.add_stage("ingest", stage_ingest)
    p.add_stage("validate", stage_validate, depends_on=["ingest"])
    p.add_stage("train", stage_train, depends_on=["validate"])
    p.add_stage("evaluate", stage_evaluate, depends_on=["train"])
    p.add_stage("register", stage_register, depends_on=["evaluate"])
    p.add_stage("deploy-check", stage_deploy_check, depends_on=["register"])
    return p


def run_flow(settings: Settings | None = None):
    """Run the full flow on the configured backend (base DAG by default)."""
    settings = settings or get_settings()
    backend = (settings.pipeline_backend or "base").lower()
    if backend == "prefect":
        from .prefect_flow import run_prefect_flow  # lazy optional import

        return run_prefect_flow(settings)

    pipeline = build_pipeline()
    return pipeline.run({"settings": settings})
