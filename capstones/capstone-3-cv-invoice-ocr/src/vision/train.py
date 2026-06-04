"""CLI training entrypoint: ``python -m vision.train``.

Fine-tunes a ResNet18 head when torch is available, else trains the numpy
``DummyClassifier`` on synthetic features. Logs params/metrics to MLflow
(unless ``--no-mlflow``) and writes a versioned artifact under ``models/``.
"""

from __future__ import annotations

import argparse

from .config import get_settings
from .logging_conf import get_logger
from .pipeline import log_to_mlflow, train_pipeline

log = get_logger(__name__)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Train the document image classifier.")
    p.add_argument(
        "--backend",
        default=None,
        choices=["auto", "torch", "dummy"],
        help="classifier backend (default: from config / auto-detect)",
    )
    p.add_argument("--no-mlflow", action="store_true", help="disable MLflow tracking")
    p.add_argument("--no-save", action="store_true", help="do not persist the artifact")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    settings = get_settings()

    result = train_pipeline(settings, backend=args.backend, save=not args.no_save)

    log.info(
        "trained backend=%s metrics=%s classes=%s",
        result.backend,
        result.metrics,
        result.label_names,
    )

    if settings.use_mlflow and not args.no_mlflow:
        log_to_mlflow(result, settings)

    if result.artifact_path:
        log.info("artifact: %s", result.artifact_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
