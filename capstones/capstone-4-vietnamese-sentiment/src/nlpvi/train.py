"""Training pipeline: train -> evaluate -> persist artifact (+ optional MLflow).

Importable as a library (``train_model``) for tests, and runnable as a CLI:

    python -m nlpvi.train --no-mlflow
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
)
from sklearn.model_selection import train_test_split

from . import __version__
from .config import Settings, get_settings
from .data import LABEL_NAMES, load_data
from .logging_conf import get_logger
from .model import build_sklearn_pipeline

log = get_logger(__name__)


@dataclass
class TrainResult:
    """Outcome of a training run."""

    accuracy: float
    macro_f1: float
    per_class: dict
    n_train: int
    n_test: int
    model_path: str
    model_version: str


def train_model(
    settings: Settings | None = None,
    *,
    use_mlflow: bool | None = None,
) -> TrainResult:
    """Train the TF-IDF + LR sentiment model and persist it under ``models/``.

    Returns a :class:`TrainResult`. Tests call this directly. MLflow logging is
    lazy and skipped when disabled or unavailable.
    """
    settings = settings or get_settings()
    df = load_data(
        settings.data_path,
        synthetic_size=settings.synthetic_size,
        seed=settings.random_seed,
    )

    x_train, x_test, y_train, y_test = train_test_split(
        df["text"].tolist(),
        df["label"].to_numpy(),
        test_size=settings.test_size,
        random_state=settings.random_seed,
        stratify=df["label"].to_numpy(),
    )

    pipeline = build_sklearn_pipeline(settings)
    pipeline.fit(x_train, y_train)

    preds = pipeline.predict(x_test)
    acc = float(accuracy_score(y_test, preds))
    macro_f1 = float(f1_score(y_test, preds, average="macro"))
    report = classification_report(
        y_test,
        preds,
        labels=list(range(len(LABEL_NAMES))),
        target_names=list(LABEL_NAMES),
        output_dict=True,
        zero_division=0,
    )

    version = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    model_path = settings.model_path
    model_path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "package_version": __version__,
        "model_version": version,
        "backend": settings.model_backend,
        "labels": list(LABEL_NAMES),
        "accuracy": acc,
        "macro_f1": macro_f1,
    }
    joblib.dump({"pipeline": pipeline, "metadata": metadata}, model_path)
    model_path.with_suffix(".meta.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    log.info("saved model path=%s macro_f1=%.4f acc=%.4f", str(model_path), macro_f1, acc)

    result = TrainResult(
        accuracy=acc,
        macro_f1=macro_f1,
        per_class={k: report[k] for k in LABEL_NAMES},
        n_train=len(x_train),
        n_test=len(x_test),
        model_path=str(model_path),
        model_version=version,
    )

    should_log = settings.mlflow_enabled if use_mlflow is None else use_mlflow
    if should_log:
        _log_mlflow(settings, result)

    return result


def _log_mlflow(settings: Settings, result: TrainResult) -> None:
    """Best-effort MLflow logging; never fails the training run."""
    try:  # lazy import — mlflow is an optional dep
        import mlflow

        mlflow.set_tracking_uri(settings.mlflow_tracking_uri)
        mlflow.set_experiment(settings.mlflow_experiment)
        with mlflow.start_run():
            mlflow.log_params(
                {
                    "backend": settings.model_backend,
                    "tfidf_max_features": settings.tfidf_max_features,
                    "tfidf_ngram_max": settings.tfidf_ngram_max,
                    "lr_c": settings.lr_c,
                    "seed": settings.random_seed,
                }
            )
            mlflow.log_metrics(
                {
                    "accuracy": result.accuracy,
                    "macro_f1": result.macro_f1,
                    "n_train": result.n_train,
                    "n_test": result.n_test,
                }
            )
            artifact = Path(result.model_path)
            if artifact.exists():
                mlflow.log_artifact(str(artifact))
        log.info("logged run to mlflow uri=%s", settings.mlflow_tracking_uri)
    except Exception as exc:  # pragma: no cover - mlflow optional/offline
        log.warning("mlflow logging skipped: %s", exc)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Train Vietnamese sentiment model")
    parser.add_argument("--config", default=None, help="path to config.yaml")
    parser.add_argument("--no-mlflow", action="store_true", help="disable MLflow logging")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    settings = get_settings(args.config)
    result = train_model(settings, use_mlflow=not args.no_mlflow)
    np.set_printoptions(suppress=True)
    log.info(
        "training complete macro_f1=%.4f accuracy=%.4f version=%s",
        result.macro_f1,
        result.accuracy,
        result.model_version,
    )
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
