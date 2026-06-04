"""Inference: load the fitted pipeline and score records. Used by API + CLI."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from .config import Settings, get_settings
from .data import FEATURE_COLUMNS
from .logging_conf import get_logger

logger = get_logger(__name__)


def load_model(settings: Settings | None = None):
    """Load the persisted sklearn Pipeline from disk. Raises if missing."""
    settings = settings or get_settings()
    path = settings.model_path
    if not path.exists():
        raise FileNotFoundError(
            f"model artifact not found at {path}; run `python -m churn.train` first"
        )
    logger.info("loading model", extra={"path": str(path)})
    return joblib.load(path)


@lru_cache
def _cached_model():
    return load_model()


def _frame(records: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame.from_records(records)
    # Ensure all expected columns exist (missing -> NaN, handled by imputers).
    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            df[col] = None
    return df[FEATURE_COLUMNS]


def predict(
    records: list[dict[str, Any]],
    model=None,
    threshold: float = 0.5,
) -> list[dict[str, Any]]:
    """Score a batch of customer records.

    Returns one dict per record: {"churn_probability": float, "churn_label": int}.
    """
    if not records:
        return []
    pipeline = model if model is not None else _cached_model()
    x = _frame(records)
    proba = pipeline.predict_proba(x)[:, 1]
    return [
        {"churn_probability": round(float(p), 6), "churn_label": int(p >= threshold)}
        for p in proba
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score churn for JSON records")
    parser.add_argument(
        "--input",
        type=Path,
        help="path to a JSON file (object or list of objects); defaults to a demo record",
    )
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args(argv)

    if args.input and args.input.exists():
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        records = payload if isinstance(payload, list) else [payload]
    else:
        records = [
            {
                "tenure": 2,
                "monthly_charges": 95.0,
                "total_charges": 190.0,
                "num_services": 2,
                "senior_citizen": 1,
                "contract": "month-to-month",
                "payment_method": "electronic-check",
                "internet_service": "fiber-optic",
                "paperless_billing": "yes",
                "gender": "female",
            }
        ]

    out = predict(records, threshold=args.threshold)
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
