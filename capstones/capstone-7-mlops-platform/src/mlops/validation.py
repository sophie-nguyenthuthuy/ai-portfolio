"""Base-deps data-quality / schema validation used by the `validate` stage.

No heavy dependencies (Great Expectations / pandera) are required: the checks
below are explicit and deterministic so the validate stage runs offline.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from .data import CATEGORICAL_FEATURES, FEATURE_COLUMNS, NUMERIC_FEATURES, TARGET
from .logging_conf import get_logger

logger = get_logger(__name__)

# Expected non-negative numeric columns (a negative value is a data error).
NON_NEGATIVE = ["tenure", "monthly_charges", "total_charges", "num_services"]


@dataclass
class ValidationReport:
    """Outcome of a data-quality run."""

    passed: bool
    n_rows: int
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: dict[str, bool] = field(default_factory=dict)

    def as_dict(self) -> dict[str, object]:
        return {
            "passed": self.passed,
            "n_rows": self.n_rows,
            "errors": self.errors,
            "warnings": self.warnings,
            "checks": self.checks,
        }


def validate_dataframe(df: pd.DataFrame, *, require_target: bool = True) -> ValidationReport:
    """Run schema + data-quality checks on a training/scoring frame.

    Errors fail the run; warnings are surfaced but non-fatal.
    """
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, bool] = {}

    # 1) non-empty
    checks["non_empty"] = len(df) > 0
    if not checks["non_empty"]:
        errors.append("dataframe is empty")

    # 2) required feature columns present
    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    checks["schema_features_present"] = not missing
    if missing:
        errors.append(f"missing feature columns: {missing}")

    # 3) target present (training only)
    if require_target:
        checks["target_present"] = TARGET in df.columns
        if TARGET not in df.columns:
            errors.append(f"missing target column: {TARGET!r}")

    # 4) numeric columns are numeric
    bad_numeric = [
        c for c in NUMERIC_FEATURES if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])
    ]
    checks["numeric_dtypes"] = not bad_numeric
    if bad_numeric:
        errors.append(f"non-numeric numeric columns: {bad_numeric}")

    # 5) non-negativity
    negative = [
        c for c in NON_NEGATIVE if c in df.columns and pd.api.types.is_numeric_dtype(df[c])
        and (df[c] < 0).any()
    ]
    checks["non_negative"] = not negative
    if negative:
        errors.append(f"negative values in non-negative columns: {negative}")

    # 6) null-rate (warn above 5% on any feature column)
    high_null = []
    for c in FEATURE_COLUMNS:
        if c in df.columns and len(df):
            rate = float(df[c].isna().mean())
            if rate > 0.05:
                high_null.append(f"{c}={rate:.2%}")
    checks["null_rate_ok"] = not high_null
    if high_null:
        warnings.append(f"high null rate: {high_null}")

    # 7) target balance (training only) — warn if a class is < 1%
    if require_target and TARGET in df.columns and len(df):
        rate = float(df[TARGET].mean())
        checks["target_balanced"] = 0.01 < rate < 0.99
        if not checks["target_balanced"]:
            warnings.append(f"degenerate target balance: positive_rate={rate:.3f}")

    # 8) categorical cardinality sanity (warn if a categorical explodes)
    high_card = [
        c for c in CATEGORICAL_FEATURES if c in df.columns and df[c].nunique(dropna=True) > 50
    ]
    checks["categorical_cardinality_ok"] = not high_card
    if high_card:
        warnings.append(f"unexpectedly high cardinality: {high_card}")

    passed = not errors
    report = ValidationReport(
        passed=passed,
        n_rows=int(len(df)),
        errors=errors,
        warnings=warnings,
        checks=checks,
    )
    logger.info(
        "data validation complete",
        extra={"passed": passed, "n_errors": len(errors), "n_warnings": len(warnings)},
    )
    return report
