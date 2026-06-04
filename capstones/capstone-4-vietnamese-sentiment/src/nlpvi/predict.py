"""Inference: load the persisted artifact and classify Vietnamese text."""

from __future__ import annotations

import threading
from pathlib import Path
from typing import Any

import joblib
import numpy as np

from .config import Settings, get_settings
from .data import LABEL_NAMES
from .logging_conf import get_logger
from .train import train_model

log = get_logger(__name__)

_LOCK = threading.Lock()
_STATE: dict[str, Any] = {"pipeline": None, "metadata": None, "path": None}


def _load_artifact(path: Path) -> dict[str, Any]:
    payload = joblib.load(path)
    if not isinstance(payload, dict) or "pipeline" not in payload:
        raise ValueError(f"invalid model artifact: {path}")
    return payload


def load_model(settings: Settings | None = None, *, train_if_missing: bool = True):
    """Return the cached sklearn pipeline, loading or training it on demand."""
    settings = settings or get_settings()
    path = settings.model_path
    with _LOCK:
        if _STATE["pipeline"] is not None and _STATE["path"] == str(path):
            return _STATE["pipeline"]
        if not path.exists():
            if not train_if_missing:
                raise FileNotFoundError(f"model artifact not found: {path}")
            log.info("no artifact at %s; training a fresh model", str(path))
            train_model(settings, use_mlflow=False)
        payload = _load_artifact(path)
        _STATE.update(
            pipeline=payload["pipeline"],
            metadata=payload.get("metadata", {}),
            path=str(path),
        )
        log.info("model loaded path=%s", str(path))
        return _STATE["pipeline"]


def reset_cache() -> None:
    """Drop the in-process model cache (used by tests/lifespan)."""
    with _LOCK:
        _STATE.update(pipeline=None, metadata=None, path=None)


def _scores_from_pipeline(pipeline, texts: list[str]) -> np.ndarray:
    proba = pipeline.predict_proba(texts)
    classes = list(getattr(pipeline, "classes_", range(len(LABEL_NAMES))))
    # reorder columns to canonical (negative, neutral, positive) = (0,1,2)
    ordered = np.zeros((len(texts), len(LABEL_NAMES)), dtype=float)
    for col, cls in enumerate(classes):
        ordered[:, int(cls)] = proba[:, col]
    return ordered


def predict(texts: list[str], settings: Settings | None = None) -> list[dict[str, Any]]:
    """Classify Vietnamese review texts.

    Returns one dict per input::

        {"label": "positive",
         "scores": {"negative": 0.02, "neutral": 0.08, "positive": 0.90}}
    """
    if not isinstance(texts, list) or not all(isinstance(t, str) for t in texts):
        raise TypeError("texts must be a list[str]")
    if not texts:
        return []
    pipeline = load_model(settings)
    scores = _scores_from_pipeline(pipeline, texts)
    results: list[dict[str, Any]] = []
    for row in scores:
        idx = int(np.argmax(row))
        results.append(
            {
                "label": LABEL_NAMES[idx],
                "scores": {
                    LABEL_NAMES[0]: round(float(row[0]), 6),
                    LABEL_NAMES[1]: round(float(row[1]), 6),
                    LABEL_NAMES[2]: round(float(row[2]), 6),
                },
            }
        )
    return results


def main(argv: list[str] | None = None) -> int:  # pragma: no cover - CLI glue
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Predict Vietnamese sentiment")
    parser.add_argument("texts", nargs="+", help="review texts to classify")
    args = parser.parse_args(argv)
    print(json.dumps(predict(args.texts), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
