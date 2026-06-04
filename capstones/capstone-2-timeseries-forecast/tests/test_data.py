"""Tests for data loading + synthetic generation."""

from __future__ import annotations

import numpy as np
import pandas as pd

from forecast.data import generate_synthetic, load_series, train_test_split_series


def test_synthetic_is_deterministic():
    a = generate_synthetic(120, seed=1)
    b = generate_synthetic(120, seed=1)
    pd.testing.assert_series_equal(a, b)


def test_synthetic_shape_and_freq():
    s = generate_synthetic(200, seed=3)
    assert len(s) == 200
    assert isinstance(s.index, pd.DatetimeIndex)
    assert (s.to_numpy() > 0).all()
    # daily frequency, strictly increasing dates
    deltas = np.diff(s.index.values).astype("timedelta64[D]").astype(int)
    assert (deltas == 1).all()


def test_load_series_falls_back_to_synthetic(tmp_path):
    s = load_series(tmp_path / "nope.csv", n_days=90, seed=5)
    assert len(s) == 90


def test_load_series_reads_csv(tmp_path):
    path = tmp_path / "series.csv"
    df = pd.DataFrame(
        {
            "date": pd.date_range("2023-01-01", periods=50, freq="D"),
            "value": np.arange(50, dtype=float) + 10,
        }
    )
    df.to_csv(path, index=False)
    s = load_series(path)
    assert len(s) == 50
    assert s.iloc[0] == 10.0
    assert s.index.name == "date"


def test_train_test_split():
    s = generate_synthetic(100, seed=2)
    train, test = train_test_split_series(s, test_size=20)
    assert len(train) == 80
    assert len(test) == 20
    assert train.index[-1] < test.index[0]
