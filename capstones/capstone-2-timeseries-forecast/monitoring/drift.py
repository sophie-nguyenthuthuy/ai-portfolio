"""Distribution-drift detection for the forecast series.

Two complementary checks:
  * **PSI** (Population Stability Index) between a reference window and a recent
    window — the standard tabular drift score.
  * **Moment shift** — relative change in rolling mean and variance.

CLI: ``python -m monitoring.drift`` (or ``python monitoring/drift.py``) runs the
check on the configured / synthetic series and prints a JSON verdict.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import pandas as pd

# Allow running as a loose script (python monitoring/drift.py).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from forecast.config import get_settings  # noqa: E402
from forecast.data import load_series  # noqa: E402
from forecast.logging_conf import get_logger  # noqa: E402

log = get_logger("forecast.drift")

# Conventional PSI interpretation thresholds.
PSI_MINOR = 0.10
PSI_MAJOR = 0.25


@dataclass
class DriftReport:
    psi: float
    mean_shift: float
    var_shift: float
    drift: bool
    severity: str  # none | minor | major
    reference_n: int
    recent_n: int


def population_stability_index(
    reference: np.ndarray, recent: np.ndarray, *, bins: int = 10, eps: float = 1e-6
) -> float:
    """PSI = sum((recent% - ref%) * ln(recent% / ref%)) over quantile bins."""
    reference = np.asarray(reference, dtype=float)
    recent = np.asarray(recent, dtype=float)
    if reference.size == 0 or recent.size == 0:
        return 0.0

    quantiles = np.linspace(0, 1, bins + 1)
    edges = np.unique(np.quantile(reference, quantiles))
    if edges.size < 2:
        return 0.0
    edges[0], edges[-1] = -np.inf, np.inf

    ref_counts, _ = np.histogram(reference, bins=edges)
    rec_counts, _ = np.histogram(recent, bins=edges)
    ref_pct = ref_counts / max(ref_counts.sum(), 1)
    rec_pct = rec_counts / max(rec_counts.sum(), 1)
    ref_pct = np.clip(ref_pct, eps, None)
    rec_pct = np.clip(rec_pct, eps, None)
    return float(np.sum((rec_pct - ref_pct) * np.log(rec_pct / ref_pct)))


def detect_drift(series: pd.Series, *, window: int = 90, bins: int = 10) -> DriftReport:
    """Compare the most-recent ``window`` points against the prior window."""
    values = series.to_numpy(dtype=float)
    n = len(values)
    window = min(window, n // 2) if n >= 4 else 1
    reference = values[-2 * window : -window] if n >= 2 * window else values[: n // 2]
    recent = values[-window:]

    psi = population_stability_index(reference, recent, bins=bins)
    ref_mean = reference.mean() if reference.size else 0.0
    ref_var = reference.var() if reference.size else 0.0
    mean_shift = abs(recent.mean() - ref_mean) / (abs(ref_mean) + 1e-9)
    var_shift = abs(recent.var() - ref_var) / (abs(ref_var) + 1e-9)

    if psi >= PSI_MAJOR:
        severity = "major"
    elif psi >= PSI_MINOR:
        severity = "minor"
    else:
        severity = "none"
    drift = severity != "none" or mean_shift > 0.25

    report = DriftReport(
        psi=round(psi, 6),
        mean_shift=round(float(mean_shift), 6),
        var_shift=round(float(var_shift), 6),
        drift=bool(drift),
        severity=severity,
        reference_n=int(reference.size),
        recent_n=int(recent.size),
    )
    log.info("drift report: %s", asdict(report))
    return report


def main(argv: list[str] | None = None) -> int:
    settings = get_settings()
    series = load_series(
        settings.resolved_data_path(),
        date_col=settings.date_col,
        value_col=settings.value_col,
        n_days=settings.synthetic_days,
        seed=settings.seed,
    )
    report = detect_drift(series)
    print(json.dumps(asdict(report), indent=2))  # noqa: T201 - CLI output
    return 1 if report.drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
