"""Typed application settings (pydantic-settings).

Values resolve from (in order): env vars (prefix ``VISION_``), the values in
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

# Canonical document classes used across data / train / predict.
DEFAULT_LABELS: tuple[str, ...] = ("invoice", "receipt", "id_card", "other")


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
        env_prefix="VISION_",
        env_file=".env",
        extra="ignore",
        protected_namespaces=(),
    )

    # --- data ---
    data_path: str = Field(default="data/documents", description="image-folder dataset root")
    labels: list[str] = Field(default_factory=lambda: list(DEFAULT_LABELS))
    samples_per_class: int = 24
    seed: int = 42

    # --- image preprocessing ---
    image_size: int = 64  # square side after resize (dummy path)
    resnet_size: int = 224  # torchvision ResNet expected input

    # --- training ---
    backend: str = "auto"  # auto | torch | dummy
    epochs: int = 3
    batch_size: int = 8
    learning_rate: float = 1e-3
    test_fraction: float = 0.25

    # --- ocr ---
    ocr_engine: str = "auto"  # auto | pytesseract | easyocr | stub
    ocr_lang: str = "eng"

    # --- artifacts / tracking ---
    model_dir: str = "models"
    mlflow_tracking_uri: str = "file:./mlruns"
    mlflow_experiment: str = "cv-invoice-ocr"
    use_mlflow: bool = True

    # --- service ---
    app_name: str = "cv-invoice-ocr"
    log_level: str = "INFO"
    max_upload_bytes: int = 8 * 1024 * 1024  # 8 MiB

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
