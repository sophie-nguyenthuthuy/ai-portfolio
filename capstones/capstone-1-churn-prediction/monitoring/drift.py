"""Population Stability Index (PSI) data-drift check with a CLI.

PSI rule of thumb:
  < 0.1  : no significant population change
  0.1-0.25: moderate change (investigate)
  > 0.25 : significant change (likely retrain)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Allow running both as a module and as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn.data import NUMERIC_FEATURES, generate_synthetic  # noqa: E402


def psi(
    reference: np.ndarray | pd.Series,
    current: np.ndarray | pd.Series,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Compute PSI between a reference and current 1-D numeric distribution.

    Bin edges are derived from quantiles of the reference distribution.
    """
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    ref = ref[~np.isnan(ref)]
    cur = cur[~np.isnan(cur)]
    if ref.size == 0 or cur.size == 0:
        return 0.0

    quantiles = np.linspace(0, 1, bins + 1)
    edges = np.unique(np.quantile(ref, quantiles))
    if edges.size < 2:  # degenerate (constant) feature
        return 0.0
    edges[0], edges[-1] = -np.inf, np.inf

    ref_counts, _ = np.histogram(ref, bins=edges)
    cur_counts, _ = np.histogram(cur, bins=edges)

    ref_pct = ref_counts / ref_counts.sum() + epsilon
    cur_pct = cur_counts / cur_counts.sum() + epsilon

    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def dataframe_psi(
    reference: pd.DataFrame,
    current: pd.DataFrame,
    columns: list[str] | None = None,
    bins: int = 10,
) -> dict[str, float]:
    """Per-column PSI for the shared numeric columns of two frames."""
    cols = columns or [c for c in NUMERIC_FEATURES if c in reference.columns and c in current.columns]
    return {c: psi(reference[c], current[c], bins=bins) for c in cols}


def evaluate_drift(scores: dict[str, float], threshold: float = 0.25) -> dict[str, object]:
    """Summarize PSI scores against a drift threshold."""
    drifted = {c: s for c, s in scores.items() if s > threshold}
    return {
        "psi": scores,
        "threshold": threshold,
        "drifted_features": sorted(drifted),
        "drift_detected": bool(drifted),
        "max_psi": max(scores.values()) if scores else 0.0,
    }


def _read(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="PSI data-drift check")
    parser.add_argument("--reference", type=Path, help="reference CSV")
    parser.add_argument("--current", type=Path, help="current CSV")
    parser.add_argument("--threshold", type=float, default=0.25)
    parser.add_argument("--bins", type=int, default=10)
    args = parser.parse_args(argv)

    if args.reference and args.current:
        ref, cur = _read(args.reference), _read(args.current)
    else:
        # Demo mode: reference vs. a shifted synthetic sample.
        ref = generate_synthetic(n=2000, seed=1)
        cur = generate_synthetic(n=2000, seed=2)
        cur["monthly_charges"] = cur["monthly_charges"] * 1.4 + 10
        cur["tenure"] = (cur["tenure"] * 0.5).astype(int)

    scores = dataframe_psi(ref, cur, bins=args.bins)
    summary = evaluate_drift(scores, threshold=args.threshold)
    print(json.dumps(summary, indent=2))
    return 1 if summary["drift_detected"] else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
