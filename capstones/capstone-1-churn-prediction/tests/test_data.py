"""Tests for synthetic data generation and loading."""

from __future__ import annotations

import pandas as pd

from churn.data import (
    FEATURE_COLUMNS,
    TARGET,
    generate_synthetic,
    load_data,
    split_features_target,
)


def test_synthetic_schema_and_determinism():
    a = generate_synthetic(n=500, seed=42)
    b = generate_synthetic(n=500, seed=42)
    pd.testing.assert_frame_equal(a, b)  # deterministic seed
    assert len(a) == 500
    for col in FEATURE_COLUMNS + [TARGET]:
        assert col in a.columns


def test_synthetic_has_learnable_signal():
    df = generate_synthetic(n=2000, seed=42)
    rate = df[TARGET].mean()
    assert 0.05 < rate < 0.95  # both classes present, not degenerate
    # Month-to-month should churn more than two-year — confirms real signal.
    m2m = df.loc[df.contract == "month-to-month", TARGET].mean()
    two_year = df.loc[df.contract == "two-year", TARGET].mean()
    assert m2m > two_year


def test_load_data_falls_back_to_synthetic(tmp_path):
    df = load_data(tmp_path / "missing.csv", n=300, seed=1)
    assert len(df) == 300
    x, y = split_features_target(df)
    assert list(x.columns) == FEATURE_COLUMNS
    assert set(y.unique()).issubset({0, 1})


def test_load_data_reads_csv(tmp_path):
    src = generate_synthetic(n=100, seed=3)
    path = tmp_path / "data.csv"
    src.to_csv(path, index=False)
    loaded = load_data(path)
    assert len(loaded) == 100
