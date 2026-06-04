"""Data loading + synthetic series generation.

A "series" is a daily-frequency pandas Series indexed by a DatetimeIndex.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .logging_conf import get_logger

log = get_logger(__name__)


def generate_synthetic(
    n_days: int = 730,
    *,
    seed: int = 42,
    start: str = "2022-01-01",
    base: float = 1000.0,
) -> pd.Series:
    """Generate a realistic daily series: trend + weekly + yearly seasonality + noise.

    Deterministic given ``seed``. Models a VN retail sales pattern: gentle upward
    trend, a weekend uplift (weekly), a yearly bump around Tet / mid-year, and
    multiplicative noise. Values are non-negative.
    """
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start=start, periods=int(n_days), freq="D")
    t = np.arange(n_days, dtype=float)

    # Linear + mild quadratic trend.
    trend = base + 0.6 * t + 0.0004 * t**2

    # Weekly seasonality: weekend uplift (Sat=5, Sun=6 in dayofweek).
    dow = idx.dayofweek.to_numpy()
    weekly = np.where(dow >= 5, 0.18, -0.04) * base * 0.25
    weekly = weekly + 0.05 * base * np.sin(2 * np.pi * dow / 7.0)

    # Yearly seasonality: peak near day-of-year ~30 (Tet) and ~200 (mid-year).
    doy = idx.dayofyear.to_numpy()
    yearly = (
        0.20 * base * np.exp(-((doy - 30) ** 2) / (2 * 18.0**2))
        + 0.10 * base * np.sin(2 * np.pi * doy / 365.0)
    )

    noise = rng.normal(0.0, 0.05 * base, size=n_days)

    values = trend + weekly + yearly + noise
    values = np.clip(values, a_min=1.0, a_max=None)

    series = pd.Series(values, index=idx, name="value")
    series.index.name = "date"
    log.info("generated synthetic series: %d days", n_days)
    return series


def load_series(
    path: str | Path | None,
    *,
    date_col: str = "date",
    value_col: str = "value",
    n_days: int = 730,
    seed: int = 42,
) -> pd.Series:
    """Load a (date,value) CSV if present, else fall back to synthetic data.

    Returns a daily-frequency Series sorted by date. Missing calendar days are
    forward/back filled so downstream models see a regular grid.
    """
    if path is not None and Path(path).exists():
        df = pd.read_csv(path)
        if date_col not in df.columns or value_col not in df.columns:
            raise ValueError(
                f"CSV {path} must have columns '{date_col}' and '{value_col}', "
                f"got {list(df.columns)}"
            )
        df[date_col] = pd.to_datetime(df[date_col])
        df = df.sort_values(date_col).drop_duplicates(subset=date_col)
        series = pd.Series(df[value_col].to_numpy(dtype=float), index=df[date_col].to_numpy())
        series.index = pd.DatetimeIndex(series.index)
        series = series.asfreq("D")
        series = series.interpolate("time").ffill().bfill()
        series.name = "value"
        series.index.name = "date"
        log.info("loaded series from %s: %d rows", path, len(series))
        return series

    log.info("no CSV at %s — using synthetic series", path)
    return generate_synthetic(n_days, seed=seed)


def train_test_split_series(series: pd.Series, test_size: int) -> tuple[pd.Series, pd.Series]:
    """Chronological split: last ``test_size`` points form the holdout."""
    if test_size <= 0 or test_size >= len(series):
        raise ValueError(f"test_size {test_size} out of range for series len {len(series)}")
    return series.iloc[:-test_size], series.iloc[-test_size:]
