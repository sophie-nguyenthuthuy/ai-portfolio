"""Tests for the PSI drift detector."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "monitoring"))

from drift import dataframe_psi, evaluate_drift, psi  # noqa: E402

from churn.data import generate_synthetic  # noqa: E402


def test_psi_zero_for_identical():
    rng = np.random.default_rng(0)
    x = rng.normal(size=2000)
    assert psi(x, x) < 1e-6


def test_psi_detects_shift():
    rng = np.random.default_rng(0)
    ref = rng.normal(0, 1, 5000)
    cur = rng.normal(3, 1, 5000)
    assert psi(ref, cur) > 0.25


def test_dataframe_psi_and_evaluate():
    ref = generate_synthetic(n=2000, seed=1)
    cur = generate_synthetic(n=2000, seed=2)
    cur["monthly_charges"] = cur["monthly_charges"] * 1.5 + 20
    scores = dataframe_psi(ref, cur)
    summary = evaluate_drift(scores, threshold=0.25)
    assert "monthly_charges" in summary["drifted_features"]
    assert summary["drift_detected"] is True
