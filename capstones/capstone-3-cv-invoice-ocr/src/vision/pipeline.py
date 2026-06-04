"""Training pipeline: build dataset, split, fit, score, persist artifact.

``train_pipeline`` is the importable core used by both the CLI (``train.py``) and
the tests — it never touches MLflow unless asked, so tests call it directly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np

from .config import Settings, get_settings
from .data import load_dataset
from .logging_conf import get_logger
from .model import build_classifier, resolve_backend

log = get_logger(__name__)


@dataclass
class TrainResult:
    model: Any
    backend: str
    label_names: list[str]
    metrics: dict[str, float]
    confusion_matrix: list[list[int]]
    artifact_path: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


def stratified_split(
    n: int, labels: list[int], *, test_fraction: float, seed: int
) -> tuple[list[int], list[int]]:
    """Index split keeping at least one sample of each class in train."""
    rng = np.random.default_rng(seed)
    labels_arr = np.asarray(labels)
    train_idx: list[int] = []
    test_idx: list[int] = []
    for cls in np.unique(labels_arr):
        idx = np.where(labels_arr == cls)[0]
        rng.shuffle(idx)
        n_test = int(round(len(idx) * test_fraction))
        n_test = min(n_test, max(len(idx) - 1, 0))  # keep >=1 in train
        test_idx.extend(idx[:n_test].tolist())
        train_idx.extend(idx[n_test:].tolist())
    rng.shuffle(train_idx)
    rng.shuffle(test_idx)
    return train_idx, test_idx


def _confusion(y_true: list[int], y_pred: list[int], n_classes: int) -> list[list[int]]:
    mat = np.zeros((n_classes, n_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        mat[int(t), int(p)] += 1
    return mat.tolist()


def evaluate(model, images: list, labels: list[int]) -> tuple[dict[str, float], list[list[int]]]:
    """Accuracy + macro-F1 + confusion matrix on a held-out split."""
    if not images:
        n = model.n_classes
        return {"accuracy": float("nan"), "macro_f1": float("nan"), "n": 0}, _confusion([], [], n)

    proba = model.predict_proba(images)
    preds = np.argmax(proba, axis=1).tolist()
    truth = list(labels)
    correct = sum(int(p == t) for p, t in zip(preds, truth))
    accuracy = correct / len(truth)

    # macro-F1 (no sklearn import needed; small confusion-based computation).
    n_classes = model.n_classes
    cm = np.array(_confusion(truth, preds, n_classes))
    f1s: list[float] = []
    for c in range(n_classes):
        tp = cm[c, c]
        fp = cm[:, c].sum() - tp
        fn = cm[c, :].sum() - tp
        denom = 2 * tp + fp + fn
        f1s.append(float(2 * tp / denom) if denom else 0.0)
    metrics = {
        "accuracy": round(float(accuracy), 4),
        "macro_f1": round(float(np.mean(f1s)), 4),
        "n": len(truth),
    }
    return metrics, cm.tolist()


def train_pipeline(
    settings: Settings | None = None,
    *,
    backend: str | None = None,
    save: bool = True,
) -> TrainResult:
    """End-to-end: load images, split, fit, score holdout, persist."""
    settings = settings or get_settings()
    chosen_backend = resolve_backend(backend or settings.backend)

    dataset = load_dataset(
        settings.resolved_data_path(),
        labels=settings.labels,
        samples_per_class=settings.samples_per_class,
        size=settings.image_size,
        seed=settings.seed,
    )

    train_idx, test_idx = stratified_split(
        len(dataset),
        dataset.labels,
        test_fraction=settings.test_fraction,
        seed=settings.seed,
    )
    train_images = [dataset.images[i] for i in train_idx]
    train_labels = [dataset.labels[i] for i in train_idx]
    test_images = [dataset.images[i] for i in test_idx]
    test_labels = [dataset.labels[i] for i in test_idx]

    model = build_classifier(chosen_backend, dataset.label_names, settings=settings)
    model.fit(train_images, train_labels)
    metrics, cm = evaluate(model, test_images, test_labels)
    log.info("holdout metrics (%s): %s", chosen_backend, metrics)

    metadata = {
        "backend": getattr(model, "backend", chosen_backend),
        "label_names": dataset.label_names,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "n_train": len(train_images),
        "n_test": len(test_images),
        "image_size": settings.image_size,
        "metrics": metrics,
        "confusion_matrix": cm,
        "version": _now_version(),
    }

    result = TrainResult(
        model=model,
        backend=metadata["backend"],
        label_names=dataset.label_names,
        metrics=metrics,
        confusion_matrix=cm,
        metadata=metadata,
    )

    if save:
        result.artifact_path = save_artifact(model, metadata, settings.resolved_model_dir())
    return result


def _now_version() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def save_artifact(model, metadata: dict[str, Any], model_dir: Path) -> Path:
    """Persist model + metadata + label map; refresh the ``latest`` pointers.

    The torch backend saves its ``state_dict`` separately so the joblib pickle
    stays light; the dummy backend pickles directly.
    """
    model_dir.mkdir(parents=True, exist_ok=True)
    version = metadata["version"]
    model_path = model_dir / f"model_{version}.joblib"
    meta_path = model_dir / f"model_{version}.json"

    joblib.dump(model, model_path)
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    joblib.dump(model, model_dir / "latest.joblib")
    (model_dir / "latest.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    # Standalone label map for downstream tooling.
    (model_dir / "labels.json").write_text(
        json.dumps({i: name for i, name in enumerate(metadata["label_names"])}, indent=2),
        encoding="utf-8",
    )
    log.info("saved artifact -> %s", model_path)
    return model_path


def log_to_mlflow(result: TrainResult, settings: Settings) -> None:
    """Best-effort MLflow logging (lazy import). No-op if mlflow missing."""
    try:
        import mlflow  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dep
        log.warning("mlflow not available (%s) — skipping tracking", exc)
        return

    mlflow.set_tracking_uri(settings.mlflow_tracking_uri)
    mlflow.set_experiment(settings.mlflow_experiment)
    with mlflow.start_run(run_name=result.backend):
        mlflow.log_params(
            {
                "backend": result.backend,
                "n_classes": len(result.label_names),
                "image_size": settings.image_size,
                "epochs": settings.epochs,
                "samples_per_class": settings.samples_per_class,
            }
        )
        mlflow.log_metrics({k: v for k, v in result.metrics.items() if isinstance(v, (int, float))})
        if result.artifact_path and result.artifact_path.exists():
            mlflow.log_artifact(str(result.artifact_path))
    log.info("logged run to mlflow @ %s", settings.mlflow_tracking_uri)
