"""Inference: score records with a model from the registry. Used by API + CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd

from .config import Settings, get_settings
from .data import FEATURE_COLUMNS
from .logging_conf import get_logger

logger = get_logger(__name__)


def load_production_model(settings: Settings | None = None, stage: str = "Production"):
    """Load the current model in the given stage from the configured registry."""
    from .registry import get_registry

    settings = settings or get_settings()
    reg = get_registry(settings)
    return reg.load_model(stage=stage)


def _frame(records: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame.from_records(records)
    # Ensure all expected columns exist (missing -> NaN, handled by imputers).
    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            df[col] = None
    return df[FEATURE_COLUMNS]


def predict(
    records: list[dict[str, Any]],
    model,
    threshold: float = 0.5,
) -> list[dict[str, Any]]:
    """Score a batch of records with an explicit fitted pipeline."""
    if not records:
        return []
    x = _frame(records)
    proba = model.predict_proba(x)[:, 1]
    return [
        {"churn_probability": round(float(p), 6), "churn_label": int(p >= threshold)}
        for p in proba
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score records with the Production model")
    parser.add_argument("--input", type=Path, help="JSON file (object or list); defaults to demo record")
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

    model = load_production_model()
    out = predict(records, model=model, threshold=args.threshold)
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
