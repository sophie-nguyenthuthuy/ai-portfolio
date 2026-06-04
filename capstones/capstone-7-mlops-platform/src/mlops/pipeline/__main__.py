"""CLI: `python -m mlops.pipeline run` — execute the full reference flow."""

from __future__ import annotations

import argparse
import json

from ..config import get_settings
from .flow import run_flow
from .runner import PipelineRun


def _summarize(result) -> dict:
    if isinstance(result, PipelineRun):
        return {
            "backend": "base",
            "success": result.success,
            "order": result.order,
            "stages": [{"name": s.name, "status": s.status, "error": s.error} for s in result.stage_runs],
            "metrics": result.context.get("metrics"),
            "registered_version": result.context.get("registered_version"),
            "deployed": result.context.get("deployed"),
            "stage": result.context.get("stage"),
        }
    # Prefect backend returns the raw context dict.
    return {
        "backend": "prefect",
        "metrics": result.get("metrics"),
        "registered_version": result.get("registered_version"),
        "deployed": result.get("deployed"),
        "stage": result.get("stage"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mlops.pipeline", description="Run the MLOps flow")
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="run the full ingest->...->deploy-check flow")
    p_run.add_argument("--backend", default=None, choices=["base", "prefect"], help="override backend")
    p_run.add_argument("--classifier", default=None)

    args = parser.parse_args(argv)
    settings = get_settings()
    overrides = {}
    if args.backend:
        overrides["pipeline_backend"] = args.backend
    if args.classifier:
        overrides["classifier"] = args.classifier
    if overrides:
        settings = settings.model_copy(update=overrides)

    result = run_flow(settings)
    summary = _summarize(result)
    print(json.dumps(summary, indent=2, default=str))
    ok = summary.get("success", True)
    return 0 if ok else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
