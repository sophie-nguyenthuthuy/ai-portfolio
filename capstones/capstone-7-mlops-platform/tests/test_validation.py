"""Tests for the base-deps data validation (validate stage logic)."""

from __future__ import annotations

from mlops.data import generate_synthetic
from mlops.validation import validate_dataframe


def test_validate_passes_on_clean_data():
    df = generate_synthetic(n=400, seed=3)
    report = validate_dataframe(df)
    assert report.passed is True
    assert report.errors == []
    assert report.checks["schema_features_present"] is True
    assert report.checks["target_present"] is True


def test_validate_fails_on_missing_feature():
    df = generate_synthetic(n=200, seed=3).drop(columns=["tenure"])
    report = validate_dataframe(df)
    assert report.passed is False
    assert any("tenure" in e for e in report.errors)


def test_validate_fails_on_negative_values():
    df = generate_synthetic(n=200, seed=3)
    df.loc[0, "monthly_charges"] = -5.0
    report = validate_dataframe(df)
    assert report.passed is False
    assert report.checks["non_negative"] is False


def test_validate_missing_target_when_required():
    df = generate_synthetic(n=200, seed=3).drop(columns=["churn"])
    assert validate_dataframe(df, require_target=True).passed is False
    # Without the target requirement (scoring), the same frame is valid.
    assert validate_dataframe(df, require_target=False).passed is True
