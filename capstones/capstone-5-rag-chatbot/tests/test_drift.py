"""Tests for the RAG query/retrieval-score PSI drift detector."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "monitoring"))

from drift import (  # noqa: E402
    evaluate_drift,
    psi,
    query_length_psi,
    score_psi,
)


def test_psi_zero_for_identical():
    rng = np.random.default_rng(0)
    x = rng.normal(size=2000)
    assert psi(x, x) < 1e-6


def test_psi_detects_shift():
    rng = np.random.default_rng(0)
    ref = rng.normal(0, 1, 5000)
    cur = rng.normal(3, 1, 5000)
    assert psi(ref, cur) > 0.25


def test_query_length_psi_detects_longer_queries():
    # Reference = short, mildly varied queries; current = long verbose ones.
    short = ["nghi phep", "hoan tien the nao", "bao mat", "onboarding ra sao"]
    long = [
        "toi co mot cau hoi rat dai ve nhieu chu de khac nhau trong cong ty",
        "xin vui long giai thich chi tiet day du ve quy trinh phuc tap nay",
        "lam on cho biet toan bo thong tin lien quan den van de phat sinh",
    ]
    ref = [short[i % len(short)] for i in range(200)]
    cur = [long[i % len(long)] for i in range(200)]
    assert query_length_psi(ref, cur) > 0.25


def test_score_psi_and_evaluate():
    rng = np.random.default_rng(1)
    ref = rng.normal(0.8, 0.05, 500).tolist()
    cur = rng.normal(0.4, 0.1, 500).tolist()
    scores = {"retrieval_score": score_psi(ref, cur)}
    summary = evaluate_drift(scores, threshold=0.25)
    assert "retrieval_score" in summary["drifted_signals"]
    assert summary["drift_detected"] is True
