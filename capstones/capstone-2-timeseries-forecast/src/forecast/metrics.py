"""Forecast accuracy metrics (numpy only)."""

from __future__ import annotations

import numpy as np


def _arrays(y_true, y_pred) -> tuple[np.ndarray, np.ndarray]:
    yt = np.asarray(y_true, dtype=float)
    yp = np.asarray(y_pred, dtype=float)
    if yt.shape != yp.shape:
        raise ValueError(f"shape mismatch: {yt.shape} vs {yp.shape}")
    return yt, yp


def mae(y_true, y_pred) -> float:
    yt, yp = _arrays(y_true, y_pred)
    return float(np.mean(np.abs(yt - yp)))


def rmse(y_true, y_pred) -> float:
    yt, yp = _arrays(y_true, y_pred)
    return float(np.sqrt(np.mean((yt - yp) ** 2)))


def mape(y_true, y_pred, *, eps: float = 1e-8) -> float:
    """Mean absolute percentage error in percent. Guards against zero denominators."""
    yt, yp = _arrays(y_true, y_pred)
    denom = np.where(np.abs(yt) < eps, eps, yt)
    return float(np.mean(np.abs((yt - yp) / denom)) * 100.0)


def evaluate(y_true, y_pred) -> dict[str, float]:
    return {"mae": mae(y_true, y_pred), "rmse": rmse(y_true, y_pred), "mape": mape(y_true, y_pred)}
