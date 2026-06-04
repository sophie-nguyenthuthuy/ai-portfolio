"""Pipeline orchestration package.

Default backend is a dependency-free DAG runner (``runner.Pipeline``). The
reference flow (ingest -> validate -> train -> evaluate -> register ->
deploy-check) is defined in ``flow`` and reused by an optional Prefect backend.
"""

from __future__ import annotations

from .flow import STAGE_ORDER, build_pipeline, run_flow
from .runner import Pipeline, PipelineError, PipelineRun, Stage, StageRun

__all__ = [
    "STAGE_ORDER",
    "Pipeline",
    "PipelineError",
    "PipelineRun",
    "Stage",
    "StageRun",
    "build_pipeline",
    "run_flow",
]
