"""Data loading + synthetic Telco-churn generator with a learnable signal."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .logging_conf import get_logger

logger = get_logger(__name__)

TARGET = "churn"

NUMERIC_FEATURES = [
    "tenure",
    "monthly_charges",
    "total_charges",
    "num_services",
    "senior_citizen",
]

CATEGORICAL_FEATURES = [
    "contract",
    "payment_method",
    "internet_service",
    "paperless_billing",
    "gender",
]

FEATURE_COLUMNS = NUMERIC_FEATURES + CATEGORICAL_FEATURES

CONTRACTS = ["month-to-month", "one-year", "two-year"]
PAYMENT_METHODS = [
    "electronic-check",
    "mailed-check",
    "bank-transfer",
    "credit-card",
]
INTERNET = ["dsl", "fiber-optic", "none"]


def generate_synthetic(n: int = 4000, seed: int = 42) -> pd.DataFrame:
    """Generate a deterministic, realistic, *learnable* Telco churn dataset.

    The churn label is produced from a logistic function of the features so a
    classifier scores clearly above 0.5 AUC, then a little label noise is added.
    """
    rng = np.random.default_rng(seed)

    tenure = rng.integers(0, 73, size=n)  # months
    senior = rng.binomial(1, 0.16, size=n)
    gender = rng.choice(["male", "female"], size=n)
    contract = rng.choice(CONTRACTS, size=n, p=[0.55, 0.25, 0.20])
    payment = rng.choice(PAYMENT_METHODS, size=n, p=[0.35, 0.22, 0.22, 0.21])
    internet = rng.choice(INTERNET, size=n, p=[0.35, 0.45, 0.20])
    paperless = rng.choice(["yes", "no"], size=n, p=[0.6, 0.4])
    num_services = rng.integers(1, 8, size=n)

    base_charge = np.where(internet == "fiber-optic", 70, np.where(internet == "dsl", 45, 20))
    monthly_charges = (
        base_charge + num_services * 4.0 + rng.normal(0, 6, size=n)
    ).clip(15, 130)
    total_charges = (monthly_charges * np.maximum(tenure, 1) * rng.uniform(0.9, 1.1, n)).round(2)

    # Linear logit with hand-tuned weights -> a clean learnable signal.
    contract_w = pd.Series(contract).map(
        {"month-to-month": 1.4, "one-year": -0.3, "two-year": -1.2}
    ).to_numpy()
    payment_w = pd.Series(payment).map(
        {
            "electronic-check": 0.8,
            "mailed-check": 0.1,
            "bank-transfer": -0.2,
            "credit-card": -0.3,
        }
    ).to_numpy()
    internet_w = pd.Series(internet).map(
        {"fiber-optic": 0.7, "dsl": 0.0, "none": -0.5}
    ).to_numpy()

    logit = (
        -1.0
        + contract_w
        + payment_w
        + internet_w
        + 0.45 * senior
        - 0.035 * tenure
        + 0.012 * (monthly_charges - 65.0)
        - 0.06 * num_services
        + 0.2 * (paperless == "yes")
    )
    prob = 1.0 / (1.0 + np.exp(-logit))
    churn = rng.binomial(1, prob)

    df = pd.DataFrame(
        {
            "tenure": tenure,
            "monthly_charges": monthly_charges.round(2),
            "total_charges": total_charges,
            "num_services": num_services,
            "senior_citizen": senior,
            "contract": contract,
            "payment_method": payment,
            "internet_service": internet,
            "paperless_billing": paperless,
            "gender": gender,
            TARGET: churn.astype(int),
        }
    )
    logger.info(
        "generated synthetic data",
        extra={"rows": n, "churn_rate": round(float(df[TARGET].mean()), 4)},
    )
    return df


def load_data(path: str | Path | None = None, n: int = 4000, seed: int = 42) -> pd.DataFrame:
    """Load churn data from CSV if present, else fall back to synthetic generation."""
    if path is not None:
        p = Path(path)
        if p.exists():
            logger.info("loading data from csv", extra={"path": str(p)})
            df = pd.read_csv(p)
            return _normalize(df)
        logger.warning("csv not found, using synthetic", extra={"path": str(p)})
    return generate_synthetic(n=n, seed=seed)


def _normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Coerce a real CSV to the expected schema (lowercase target values etc.)."""
    df = df.copy()
    if TARGET in df.columns and df[TARGET].dtype == object:
        df[TARGET] = (
            df[TARGET].astype(str).str.strip().str.lower().map({"yes": 1, "no": 0}).fillna(df[TARGET])
        )
        df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce").fillna(0).astype(int)
    return df


def split_features_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return (X, y) using the canonical feature columns."""
    x = df[[c for c in FEATURE_COLUMNS if c in df.columns]].copy()
    y = df[TARGET].astype(int)
    return x, y
