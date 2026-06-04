"""Training entrypoint: fit pipeline, evaluate, log to MLflow, persist artifact."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

from . import __version__
from .config import Settings, get_settings
from .data import load_data, split_features_target
from .logging_conf import get_logger
from .model import build_model

logger = get_logger(__name__)


@dataclass
class TrainResult:
    """Outcome of a training run."""

    metrics: dict[str, float]
    params: dict[str, Any]
    report: dict[str, Any]
    model_path: str | None = None
    metadata_path: str | None = None
    pipeline: Any = field(default=None, repr=False)


def train_core(
    settings: Settings | None = None,
    *,
    save: bool = True,
) -> TrainResult:
    """Train + evaluate the pipeline. No MLflow here so tests can call directly."""
    settings = settings or get_settings()

    df = load_data(
        settings.resolved_data_path,
        n=settings.synthetic_rows,
        seed=settings.random_seed,
    )
    x, y = split_features_target(df)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=settings.test_size,
        random_state=settings.random_seed,
        stratify=y if y.nunique() > 1 else None,
    )

    pipeline = build_model(settings.classifier, settings.random_seed)
    pipeline.fit(x_train, y_train)

    proba = pipeline.predict_proba(x_test)[:, 1]
    preds = (proba >= 0.5).astype(int)

    metrics = {
        "roc_auc": float(roc_auc_score(y_test, proba)),
        "pr_auc": float(average_precision_score(y_test, proba)),
        "accuracy": float((preds == y_test.to_numpy()).mean()),
        "n_train": int(len(x_train)),
        "n_test": int(len(x_test)),
    }
    report = classification_report(y_test, preds, output_dict=True, zero_division=0)
    params = {
        "classifier": settings.classifier,
        "random_seed": settings.random_seed,
        "test_size": settings.test_size,
        "synthetic_rows": settings.synthetic_rows,
        "package_version": __version__,
    }

    logger.info("training complete", extra={"metrics": metrics, "params": params})

    result = TrainResult(metrics=metrics, params=params, report=report, pipeline=pipeline)

    if save:
        _persist(pipeline, settings, metrics, params, report)
        result.model_path = str(settings.model_path)
        result.metadata_path = str(settings.metadata_path)

    return result


def _persist(pipeline, settings, metrics, params, report) -> None:
    model_path = settings.model_path
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)

    metadata = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "package_version": __version__,
        "params": params,
        "metrics": metrics,
        "classification_report": report,
    }
    settings.metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    logger.info("artifact saved", extra={"model_path": str(model_path)})


def _log_to_mlflow(result: TrainResult, settings: Settings) -> None:
    """Lazy-import MLflow and log params/metrics. Skipped on import failure."""
    try:
        import mlflow  # lazy optional import
    except ImportError:
        logger.warning("mlflow not installed; skipping tracking")
        return

    mlflow.set_tracking_uri(settings.mlflow_tracking_uri)
    mlflow.set_experiment(settings.mlflow_experiment)
    with mlflow.start_run():
        mlflow.log_params(result.params)
        mlflow.log_metrics(
            {k: v for k, v in result.metrics.items() if isinstance(v, (int, float))}
        )
        if result.metadata_path and Path(result.metadata_path).exists():
            mlflow.log_artifact(result.metadata_path)
        if result.model_path and Path(result.model_path).exists():
            mlflow.log_artifact(result.model_path)
    logger.info("logged run to mlflow", extra={"uri": settings.mlflow_tracking_uri})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Train churn prediction model")
    parser.add_argument("--classifier", default=None, help="override classifier name")
    parser.add_argument("--no-mlflow", action="store_true", help="skip MLflow logging")
    parser.add_argument("--no-save", action="store_true", help="do not persist artifact")
    args = parser.parse_args(argv)

    settings = get_settings()
    if args.classifier:
        settings = settings.model_copy(update={"classifier": args.classifier})

    result = train_core(settings, save=not args.no_save)
    if not args.no_mlflow:
        _log_to_mlflow(result, settings)

    print(json.dumps({"metrics": result.metrics, "model_path": result.model_path}, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
