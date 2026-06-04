"""Load a saved artifact (or train a fresh baseline) and produce forecasts.

``forecast(horizon)`` returns a list of dicts with date / yhat / yhat_lower /
yhat_upper — used by both the API and the CLI.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import joblib

from .config import Settings, get_settings
from .logging_conf import get_logger
from .models import ForecastModel
from .pipeline import train_pipeline

log = get_logger(__name__)


def _latest_paths(model_dir: Path) -> tuple[Path, Path]:
    return model_dir / "latest.joblib", model_dir / "latest.json"


def load_model(settings: Settings | None = None) -> tuple[ForecastModel, dict[str, Any]]:
    """Return (model, metadata). Trains a baseline if no artifact exists."""
    settings = settings or get_settings()
    model_path, meta_path = _latest_paths(settings.resolved_model_dir())

    if model_path.exists():
        model: ForecastModel = joblib.load(model_path)
        metadata = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        log.info("loaded model from %s", model_path)
        return model, metadata

    log.info("no saved artifact — training a baseline model on first use")
    result = train_pipeline(settings, model_name="baseline", save=True)
    return result.model, result.metadata


def forecast(
    horizon: int,
    *,
    settings: Settings | None = None,
    model: ForecastModel | None = None,
) -> list[dict[str, Any]]:
    """Forecast ``horizon`` future points as a list of records."""
    if horizon < 1:
        raise ValueError("horizon must be >= 1")
    settings = settings or get_settings()
    if model is None:
        model, _ = load_model(settings)

    result = model.predict(horizon)
    points: list[dict[str, Any]] = []
    for ts, yhat, lo, hi in zip(result.index, result.yhat, result.yhat_lower, result.yhat_upper):
        points.append(
            {
                "date": ts.strftime("%Y-%m-%d"),
                "yhat": round(float(yhat), 4),
                "yhat_lower": round(float(lo), 4),
                "yhat_upper": round(float(hi), 4),
            }
        )
    return points


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Forecast future points.")
    parser.add_argument("--horizon", type=int, default=None, help="number of steps ahead")
    args = parser.parse_args(argv)
    settings = get_settings()
    horizon = args.horizon or settings.horizon
    points = forecast(horizon, settings=settings)
    print(json.dumps(points, indent=2))  # noqa: T201 - CLI output is intentional
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
