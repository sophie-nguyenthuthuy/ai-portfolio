"""Tests for the drift-detection module."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "monitoring"))

from drift import detect_drift, population_stability_index  # noqa: E402

from forecast.data import generate_synthetic  # noqa: E402


def test_psi_zero_for_identical_distributions():
    rng = np.random.default_rng(0)
    x = rng.normal(size=2000)
    assert population_stability_index(x, x) < 1e-6


def test_psi_large_for_shifted_distributions():
    rng = np.random.default_rng(0)
    ref = rng.normal(0, 1, size=2000)
    recent = rng.normal(5, 1, size=2000)
    assert population_stability_index(ref, recent) > 0.25


def test_detect_drift_on_stable_series():
    s = generate_synthetic(400, seed=11)
    report = detect_drift(s, window=60)
    assert report.severity in {"none", "minor", "major"}
    assert report.recent_n > 0


def test_detect_drift_flags_injected_shift():
    s = generate_synthetic(300, seed=11)
    s.iloc[-60:] = s.iloc[-60:] * 5 + 5000  # inject a big level shift
    report = detect_drift(s, window=60)
    assert report.drift is True
