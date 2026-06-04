"""Training pipeline: fit, rolling-origin backtest, persist artifact.

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
import pandas as pd

from .config import Settings, get_settings
from .data import load_series, train_test_split_series
from .logging_conf import get_logger
from .metrics import evaluate
from .models import ForecastModel, build_model

log = get_logger(__name__)


@dataclass
class TrainResult:
    model: ForecastModel
    model_name: str
    metrics: dict[str, float]
    backtest: dict[str, float]
    artifact_path: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


def rolling_origin_backtest(
    series: pd.Series,
    *,
    model_name: str,
    season_length: int,
    conf_level: float,
    horizon: int,
    folds: int,
) -> dict[str, float]:
    """Expanding-window backtest.

    For each fold we expand the training window and forecast the next ``horizon``
    points, scoring against actuals. Returns averaged MAE / RMSE / MAPE.
    """
    n = len(series)
    if folds < 1:
        raise ValueError("folds must be >= 1")
    needed = horizon * folds
    if n <= needed + season_length:
        # Series too short for requested config — shrink folds to what fits.
        folds = max(1, (n - season_length) // max(horizon, 1) - 1)
        needed = horizon * folds

    fold_scores: list[dict[str, float]] = []
    first_train = n - needed
    for k in range(folds):
        cut = first_train + k * horizon
        train = series.iloc[:cut]
        actual = series.iloc[cut : cut + horizon]
        if len(actual) < horizon or len(train) <= season_length:
            continue
        model = build_model(model_name, season_length=season_length, conf_level=conf_level)
        model.fit(train)
        fc = model.predict(horizon)
        fold_scores.append(evaluate(actual.to_numpy(), fc.yhat))

    if not fold_scores:
        return {"mae": float("nan"), "rmse": float("nan"), "mape": float("nan"), "folds": 0}

    agg = {
        key: float(np.mean([s[key] for s in fold_scores]))
        for key in ("mae", "rmse", "mape")
    }
    agg["folds"] = float(len(fold_scores))
    log.info("backtest (%d folds): %s", len(fold_scores), agg)
    return agg


def train_pipeline(
    settings: Settings | None = None,
    *,
    model_name: str | None = None,
    save: bool = True,
) -> TrainResult:
    """End-to-end: load data, backtest, fit on train, score holdout, persist."""
    settings = settings or get_settings()
    chosen = (model_name or settings.model_name).lower()

    series = load_series(
        settings.resolved_data_path(),
        date_col=settings.date_col,
        value_col=settings.value_col,
        n_days=settings.synthetic_days,
        seed=settings.seed,
    )

    backtest = rolling_origin_backtest(
        series,
        model_name=chosen,
        season_length=settings.season_length,
        conf_level=settings.conf_level,
        horizon=settings.horizon,
        folds=settings.backtest_folds,
    )

    train, test = train_test_split_series(series, settings.test_size)
    model = build_model(chosen, season_length=settings.season_length, conf_level=settings.conf_level)
    model.fit(train)
    holdout_fc = model.predict(len(test))
    holdout_metrics = evaluate(test.to_numpy(), holdout_fc.yhat)
    log.info("holdout metrics (%s): %s", chosen, holdout_metrics)

    # Refit on the full series so the served model uses all data.
    final_model = build_model(chosen, season_length=settings.season_length, conf_level=settings.conf_level)
    final_model.fit(series)

    metadata = {
        "model_name": getattr(final_model, "name", chosen),
        "requested_model": chosen,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "n_observations": int(len(series)),
        "season_length": settings.season_length,
        "conf_level": settings.conf_level,
        "last_date": str(series.index[-1].date()),
        "holdout_metrics": holdout_metrics,
        "backtest_metrics": backtest,
        "version": _now_version(),
    }

    result = TrainResult(
        model=final_model,
        model_name=metadata["model_name"],
        metrics=holdout_metrics,
        backtest=backtest,
        metadata=metadata,
    )

    if save:
        result.artifact_path = save_artifact(final_model, metadata, settings.resolved_model_dir())
    return result


def _now_version() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def save_artifact(model: ForecastModel, metadata: dict[str, Any], model_dir: Path) -> Path:
    """Persist model + metadata; refresh the ``latest`` pointer files."""
    model_dir.mkdir(parents=True, exist_ok=True)
    version = metadata["version"]
    model_path = model_dir / f"model_{version}.joblib"
    meta_path = model_dir / f"model_{version}.json"
    joblib.dump(model, model_path)
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    joblib.dump(model, model_dir / "latest.joblib")
    (model_dir / "latest.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
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
    with mlflow.start_run(run_name=result.model_name):
        mlflow.log_params(
            {
                "model_name": result.model_name,
                "season_length": settings.season_length,
                "horizon": settings.horizon,
                "test_size": settings.test_size,
                "backtest_folds": settings.backtest_folds,
            }
        )
        mlflow.log_metrics({f"holdout_{k}": v for k, v in result.metrics.items()})
        mlflow.log_metrics(
            {f"backtest_{k}": v for k, v in result.backtest.items() if not np.isnan(v)}
        )
        if result.artifact_path and result.artifact_path.exists():
            mlflow.log_artifact(str(result.artifact_path))
    log.info("logged run to mlflow @ %s", settings.mlflow_tracking_uri)
