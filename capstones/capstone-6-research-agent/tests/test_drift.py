"""Tests for the agent behavioral-drift detectors (step-count + tool-usage PSI)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "monitoring"))

from drift import (  # noqa: E402
    categorical_psi,
    evaluate_drift,
    psi,
    step_count_psi,
    tool_usage_psi,
)


def test_psi_zero_for_identical():
    rng = np.random.default_rng(0)
    x = rng.normal(size=2000)
    assert psi(x, x) < 1e-6


def test_step_count_psi_detects_shift():
    rng = np.random.default_rng(0)
    ref = rng.integers(1, 6, size=2000)   # 1..5 steps
    cur = rng.integers(6, 11, size=2000)  # 6..10 steps (clear shift)
    assert step_count_psi(ref, cur) > 0.25


def test_categorical_psi_zero_for_identical():
    stream = ["a", "b", "a", "c"] * 50
    assert categorical_psi(stream, stream) < 1e-6


def test_tool_usage_psi_detects_shift_and_evaluate():
    ref = (["retriever"] * 300) + (["calculator"] * 200)
    cur = (["calculator"] * 500)
    score = tool_usage_psi(ref, cur)
    summary = evaluate_drift({"tool_usage": score}, threshold=0.25)
    assert summary["drift_detected"] is True
    assert "tool_usage" in summary["drifted_signals"]
