"""Typed application settings (pydantic-settings).

Values resolve from (in order): env vars (prefix ``FORECAST_``), the values in
``conf/config.yaml``, then the field defaults declared here.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

_PKG_ROOT = Path(__file__).resolve().parent
_PROJECT_ROOT = _PKG_ROOT.parent.parent
_DEFAULT_CONFIG = _PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(f"config file {path} must contain a mapping at the top level")
    return data


class Settings(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(
        env_prefix="FORECAST_",
        env_file=".env",
        extra="ignore",
        protected_namespaces=(),
    )

    # --- data ---
    data_path: str = Field(default="data/series.csv", description="CSV with date,value")
    date_col: str = "date"
    value_col: str = "value"
    synthetic_days: int = 730
    seed: int = 42

    # --- forecasting ---
    season_length: int = 7  # weekly seasonality on daily data
    horizon: int = 14
    test_size: int = 28  # holdout days
    backtest_folds: int = 3
    model_name: str = "baseline"  # baseline | naive_seasonal | sarima | prophet | lstm
    conf_level: float = 0.9  # prediction-interval coverage

    # --- artifacts / tracking ---
    model_dir: str = "models"
    mlflow_tracking_uri: str = "file:./mlruns"
    mlflow_experiment: str = "timeseries-forecast"
    use_mlflow: bool = True

    # --- service ---
    app_name: str = "timeseries-forecast"
    log_level: str = "INFO"

    @property
    def project_root(self) -> Path:
        return _PROJECT_ROOT

    def resolved_data_path(self) -> Path:
        p = Path(self.data_path)
        return p if p.is_absolute() else _PROJECT_ROOT / p

    def resolved_model_dir(self) -> Path:
        p = Path(self.model_dir)
        return p if p.is_absolute() else _PROJECT_ROOT / p


@lru_cache
def get_settings() -> Settings:
    """Build Settings layering YAML defaults under env/.env overrides."""
    yaml_values = _load_yaml(_DEFAULT_CONFIG)
    return Settings(**yaml_values)
