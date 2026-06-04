"""Training core: fit pipeline, evaluate, return a TrainResult.

The orchestrated pipeline (``mlops.pipeline``) calls ``train_core`` then registers
the artifact via the registry. This module also exposes a CLI for a one-shot
train+register run.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Any

from sklearn.metrics import (
    average_precision_score,
    classification_report,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

from . import __version__
from .config import Settings, get_settings
from .data import load_data, split_features_target
from .logging_conf import get_logger
from .model import build_model

logger = get_logger(__name__)


@dataclass
class TrainResult:
    """Outcome of a training run."""

    metrics: dict[str, float]
    params: dict[str, Any]
    report: dict[str, Any]
    pipeline: Any = field(default=None, repr=False)


def train_core(settings: Settings | None = None, df=None) -> TrainResult:
    """Train + evaluate the reference pipeline on (optionally provided) data."""
    settings = settings or get_settings()

    if df is None:
        df = load_data(
            settings.resolved_data_path,
            n=settings.synthetic_rows,
            seed=settings.random_seed,
        )
    x, y = split_features_target(df)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=settings.test_size,
        random_state=settings.random_seed,
        stratify=y if y.nunique() > 1 else None,
    )

    pipeline = build_model(settings.classifier, settings.random_seed)
    pipeline.fit(x_train, y_train)

    proba = pipeline.predict_proba(x_test)[:, 1]
    preds = (proba >= 0.5).astype(int)

    metrics = {
        "roc_auc": float(roc_auc_score(y_test, proba)),
        "pr_auc": float(average_precision_score(y_test, proba)),
        "accuracy": float((preds == y_test.to_numpy()).mean()),
        "n_train": int(len(x_train)),
        "n_test": int(len(x_test)),
    }
    report = classification_report(y_test, preds, output_dict=True, zero_division=0)
    params = {
        "classifier": settings.classifier,
        "random_seed": settings.random_seed,
        "test_size": settings.test_size,
        "synthetic_rows": settings.synthetic_rows,
        "package_version": __version__,
    }

    logger.info("training complete", extra={"metrics": metrics, "params": params})
    return TrainResult(metrics=metrics, params=params, report=report, pipeline=pipeline)


def main(argv: list[str] | None = None) -> int:
    """One-shot train + register + (optional) promote to Production."""
    parser = argparse.ArgumentParser(description="Train + register the reference model")
    parser.add_argument("--classifier", default=None, help="override classifier name")
    parser.add_argument("--promote", action="store_true", help="promote new version to Production")
    args = parser.parse_args(argv)

    from .registry import PRODUCTION, get_registry

    settings = get_settings()
    if args.classifier:
        settings = settings.model_copy(update={"classifier": args.classifier})

    result = train_core(settings)
    reg = get_registry(settings)
    mv = reg.register(result.pipeline, metrics=result.metrics, params=result.params)
    if args.promote:
        reg.promote(mv.version, PRODUCTION)

    print(json.dumps({"metrics": result.metrics, "version": mv.version, "stage": mv.stage if not args.promote else PRODUCTION}, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
