"""Load a saved artifact (or train a fresh tiny model) and serve predictions.

Two public helpers used by both the API and the CLI:

* ``classify(image_bytes) -> {"label", "confidence", "probs"}``
* ``ocr(image_bytes) -> {"engine", "text", "fields"}``
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import joblib

from .config import Settings, get_settings
from .logging_conf import get_logger
from .ocr import run_ocr
from .pipeline import train_pipeline

log = get_logger(__name__)


def _latest_paths(model_dir: Path) -> tuple[Path, Path]:
    return model_dir / "latest.joblib", model_dir / "latest.json"


def load_model(settings: Settings | None = None) -> tuple[Any, dict[str, Any]]:
    """Return (model, metadata). Trains a tiny model if no artifact exists."""
    settings = settings or get_settings()
    model_path, meta_path = _latest_paths(settings.resolved_model_dir())

    if model_path.exists():
        model = joblib.load(model_path)
        metadata = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        log.info("loaded model from %s", model_path)
        return model, metadata

    log.info("no saved artifact — training a tiny model on first use")
    result = train_pipeline(settings, save=True)
    return result.model, result.metadata


def classify(
    image_bytes: bytes,
    *,
    settings: Settings | None = None,
    model: Any | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Classify a document image into one of the configured classes."""
    settings = settings or get_settings()
    if model is None:
        model, metadata = load_model(settings)
    label_names = list(getattr(model, "label_names", (metadata or {}).get("label_names", [])))

    from .features import load_image

    image = load_image(image_bytes)
    idx, confidence = model.classify_one(image)
    proba = model.predict_proba([image])[0]
    label = label_names[idx] if idx < len(label_names) else str(idx)
    return {
        "label": label,
        "confidence": round(float(confidence), 4),
        "probs": {label_names[i] if i < len(label_names) else str(i): round(float(p), 4)
                  for i, p in enumerate(proba)},
        "backend": getattr(model, "backend", "unknown"),
    }


def ocr(
    image_bytes: bytes,
    *,
    settings: Settings | None = None,
) -> dict[str, Any]:
    """Run OCR + field parsing on an invoice image."""
    settings = settings or get_settings()
    return run_ocr(image_bytes, engine=settings.ocr_engine, lang=settings.ocr_lang)


def _read_bytes(path: str) -> bytes:
    return Path(path).read_bytes()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Classify a document or OCR an invoice.")
    parser.add_argument("image", help="path to an image file")
    parser.add_argument("--ocr", action="store_true", help="run OCR instead of classification")
    args = parser.parse_args(argv)

    settings = get_settings()
    image_bytes = _read_bytes(args.image)
    out = ocr(image_bytes, settings=settings) if args.ocr else classify(image_bytes, settings=settings)
    print(json.dumps(out, indent=2))  # noqa: T201 - CLI output is intentional
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
