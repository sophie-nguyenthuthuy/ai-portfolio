"""Model registry abstraction.

The default `LocalRegistry` is a base-deps implementation: versioned joblib
artifacts plus a JSON manifest tracking stage transitions (None -> Staging ->
Production / Archived). An optional MLflow Model Registry backend is provided
behind a lazy import and selected via `Settings.registry_backend`.
"""

from __future__ import annotations

from .base import (
    PRODUCTION,
    STAGES,
    STAGING,
    LocalRegistry,
    ModelVersion,
    RegistryError,
)

__all__ = [
    "PRODUCTION",
    "STAGES",
    "STAGING",
    "LocalRegistry",
    "ModelVersion",
    "RegistryError",
    "get_registry",
]


def get_registry(settings=None):
    """Factory: return the configured registry backend.

    `local` (default) -> LocalRegistry. `mlflow` -> lazily-imported MLflow backend.
    """
    from ..config import get_settings

    settings = settings or get_settings()
    backend = (settings.registry_backend or "local").lower()
    if backend == "local":
        return LocalRegistry(settings.resolved_registry_dir, model_name=settings.model_name)
    if backend == "mlflow":
        from .mlflow_backend import MlflowRegistry  # lazy optional import

        return MlflowRegistry(settings)
    raise RegistryError(f"unknown registry backend: {backend!r}")
