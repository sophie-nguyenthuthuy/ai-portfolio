"""Model factory: a sklearn Pipeline(preprocess + classifier)."""

from __future__ import annotations

from typing import Any

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .features import build_preprocessor


def build_classifier(name: str, random_seed: int = 42) -> Any:
    """Return an unfitted classifier by name.

    "xgboost" is an OPTIONAL dependency, imported lazily so the base install
    (and the unit-test environment) does not require it.
    """
    name = (name or "gradient_boosting").lower()
    if name in {"gradient_boosting", "gbc", "gb"}:
        return GradientBoostingClassifier(random_state=random_seed)
    if name in {"logistic_regression", "logreg", "lr"}:
        return LogisticRegression(max_iter=1000, random_state=random_seed)
    if name in {"xgboost", "xgb"}:
        try:
            from xgboost import XGBClassifier  # lazy optional import
        except ImportError as exc:  # pragma: no cover - exercised only when chosen
            raise ImportError(
                "classifier='xgboost' requires the optional dependency; "
                "install with `pip install '.[ml]'`."
            ) from exc
        return XGBClassifier(
            n_estimators=200,
            max_depth=4,
            learning_rate=0.1,
            eval_metric="logloss",
            random_state=random_seed,
        )
    raise ValueError(f"unknown classifier: {name!r}")


def build_model(name: str = "gradient_boosting", random_seed: int = 42) -> Pipeline:
    """Assemble the full inference pipeline: preprocessing + classifier."""
    return Pipeline(
        steps=[
            ("preprocess", build_preprocessor()),
            ("classifier", build_classifier(name, random_seed)),
        ]
    )
