"""Optional Prefect orchestration backend (lazy import).

Selected via ``MLOPS_PIPELINE_BACKEND=prefect``. Prefect is NOT a base dependency
(it lives in the ``[prefect]`` optional group); it is imported lazily here so the
default install and the test suite never require it. Each Prefect ``@task`` wraps
the SAME stage function used by the base DAG runner, so behaviour is identical.
"""

from __future__ import annotations

from typing import Any

from ..config import Settings, get_settings
from . import flow as _flow


def run_prefect_flow(settings: Settings | None = None) -> dict[str, Any]:  # pragma: no cover - needs prefect
    """Build and run a Prefect flow mirroring the base DAG stage graph."""
    try:
        from prefect import flow, task
    except ImportError as exc:
        raise ImportError(
            "pipeline_backend='prefect' requires the optional dependency; "
            "install with `pip install '.[prefect]'`."
        ) from exc

    settings = settings or get_settings()

    ingest = task(name="ingest")(_flow.stage_ingest)
    validate = task(name="validate")(_flow.stage_validate)
    train = task(name="train")(_flow.stage_train)
    evaluate = task(name="evaluate")(_flow.stage_evaluate)
    register = task(name="register")(_flow.stage_register)
    deploy_check = task(name="deploy-check")(_flow.stage_deploy_check)

    @flow(name="mlops-reference-flow")
    def _pipeline() -> dict[str, Any]:
        ctx: dict[str, Any] = {"settings": settings}
        ctx.update(ingest(ctx))
        ctx.update(validate(ctx))
        ctx.update(train(ctx))
        ctx.update(evaluate(ctx))
        ctx.update(register(ctx))
        ctx.update(deploy_check(ctx))
        return ctx

    return _pipeline()
