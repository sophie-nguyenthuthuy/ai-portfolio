"""CLI training entrypoint: ``python -m forecast.train``.

Runs the pipeline on synthetic-or-real data, logs to MLflow (unless ``--no-mlflow``),
and writes a versioned artifact under ``models/``.
"""

from __future__ import annotations

import argparse

from .config import get_settings
from .logging_conf import get_logger
from .models import available_models
from .pipeline import log_to_mlflow, train_pipeline

log = get_logger(__name__)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Train a time-series forecasting model.")
    p.add_argument("--model", default=None, choices=available_models() + [None], help="model name")
    p.add_argument("--no-mlflow", action="store_true", help="disable MLflow tracking")
    p.add_argument("--no-save", action="store_true", help="do not persist the artifact")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    settings = get_settings()

    result = train_pipeline(settings, model_name=args.model, save=not args.no_save)

    log.info(
        "trained model=%s holdout=%s backtest=%s",
        result.model_name,
        result.metrics,
        result.backtest,
    )

    if settings.use_mlflow and not args.no_mlflow:
        log_to_mlflow(result, settings)

    if result.artifact_path:
        log.info("artifact: %s", result.artifact_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
