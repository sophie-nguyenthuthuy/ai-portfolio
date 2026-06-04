"""Image-distribution drift detection for the document classifier.

Compares per-image statistics (brightness, contrast, size) between a reference
batch and a recent batch using PSI (Population Stability Index) per feature plus
a moment shift on brightness.

CLI: ``python -m monitoring.drift`` (or ``python monitoring/drift.py``) builds a
reference vs. a brightness-shifted recent batch from synthetic images and prints
a JSON verdict.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np

# Allow running as a loose script (python monitoring/drift.py).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vision.config import DEFAULT_LABELS  # noqa: E402
from vision.data import build_synthetic_dataset  # noqa: E402
from vision.features import image_stats  # noqa: E402
from vision.logging_conf import get_logger  # noqa: E402

log = get_logger("vision.drift")

# Conventional PSI interpretation thresholds.
PSI_MINOR = 0.10
PSI_MAJOR = 0.25

_FEATURES = ("brightness", "contrast", "row_variation")


@dataclass
class DriftReport:
    psi_per_feature: dict[str, float]
    max_psi: float
    brightness_shift: float
    drift: bool
    severity: str  # none | minor | major
    reference_n: int
    recent_n: int
    drifted_features: list[str] = field(default_factory=list)


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


def _stats_table(images, *, size: int = 64) -> dict[str, np.ndarray]:
    rows = [image_stats(img, size=size) for img in images]
    return {feat: np.array([r[feat] for r in rows], dtype=float) for feat in _FEATURES}


def detect_drift(reference_images, recent_images, *, bins: int = 10, size: int = 64) -> DriftReport:
    """Compare image-stat distributions between two batches."""
    ref_tbl = _stats_table(reference_images, size=size)
    rec_tbl = _stats_table(recent_images, size=size)

    psi_per_feature = {
        feat: round(population_stability_index(ref_tbl[feat], rec_tbl[feat], bins=bins), 6)
        for feat in _FEATURES
    }
    max_psi = max(psi_per_feature.values()) if psi_per_feature else 0.0

    ref_b = ref_tbl["brightness"].mean() if ref_tbl["brightness"].size else 0.0
    rec_b = rec_tbl["brightness"].mean() if rec_tbl["brightness"].size else 0.0
    brightness_shift = abs(rec_b - ref_b) / (abs(ref_b) + 1e-9)

    if max_psi >= PSI_MAJOR:
        severity = "major"
    elif max_psi >= PSI_MINOR:
        severity = "minor"
    else:
        severity = "none"
    drifted = [f for f, v in psi_per_feature.items() if v >= PSI_MINOR]
    drift = severity != "none" or brightness_shift > 0.20

    report = DriftReport(
        psi_per_feature=psi_per_feature,
        max_psi=round(float(max_psi), 6),
        brightness_shift=round(float(brightness_shift), 6),
        drift=bool(drift),
        severity=severity,
        reference_n=len(reference_images),
        recent_n=len(recent_images),
        drifted_features=drifted,
    )
    log.info("drift report: %s", asdict(report))
    return report


def main(argv: list[str] | None = None) -> int:
    ref = build_synthetic_dataset(DEFAULT_LABELS, samples_per_class=20, seed=42)
    rec = build_synthetic_dataset(DEFAULT_LABELS, samples_per_class=20, seed=999)
    report = detect_drift(ref.images, rec.images)
    print(json.dumps(asdict(report), indent=2))  # noqa: T201 - CLI output
    return 1 if report.drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
