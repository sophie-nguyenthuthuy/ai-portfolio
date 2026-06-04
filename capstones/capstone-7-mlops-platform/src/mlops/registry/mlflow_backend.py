"""Optional MLflow Model Registry backend (lazy import).

Selected via ``MLOPS_REGISTRY_BACKEND=mlflow``. MLflow is NOT a base dependency;
it lives in the ``[mlflow]`` optional group and is imported lazily here so the
default install and the test suite never require it. The public surface mirrors
``LocalRegistry`` (register / list_versions / promote / current / load_model).
"""

from __future__ import annotations

from typing import Any

from ..logging_conf import get_logger
from .base import PRODUCTION, STAGES, ModelVersion, RegistryError

logger = get_logger(__name__)


class MlflowRegistry:
    """Thin adapter over ``mlflow.tracking.MlflowClient`` + Model Registry."""

    def __init__(self, settings) -> None:
        try:
            import mlflow  # noqa: F401  (lazy optional import)
            from mlflow.tracking import MlflowClient
        except ImportError as exc:  # pragma: no cover - only when backend chosen
            raise ImportError(
                "registry_backend='mlflow' requires the optional dependency; "
                "install with `pip install '.[mlflow]'`."
            ) from exc

        import mlflow

        mlflow.set_tracking_uri(settings.mlflow_tracking_uri)
        self._mlflow = mlflow
        self._client = MlflowClient(tracking_uri=settings.mlflow_tracking_uri)
        self.model_name = settings.model_name
        self.experiment = settings.mlflow_experiment

    def register(
        self,
        model: Any,
        metrics: dict[str, float] | None = None,
        params: dict[str, Any] | None = None,
        run_id: str | None = None,
    ) -> ModelVersion:  # pragma: no cover - exercised only with mlflow installed
        mlflow = self._mlflow
        mlflow.set_experiment(self.experiment)
        with mlflow.start_run() as run:
            if params:
                mlflow.log_params(params)
            if metrics:
                mlflow.log_metrics({k: v for k, v in metrics.items() if isinstance(v, (int, float))})
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                registered_model_name=self.model_name,
            )
            run_id = run.info.run_id
        mv = self._client.get_latest_versions(self.model_name)[-1]
        return ModelVersion(
            version=int(mv.version),
            stage="None",
            created_at=str(mv.creation_timestamp),
            metrics=metrics or {},
            params=params or {},
            run_id=run_id,
        )

    def list_versions(self) -> list[ModelVersion]:  # pragma: no cover
        out = []
        for mv in self._client.search_model_versions(f"name='{self.model_name}'"):
            out.append(
                ModelVersion(
                    version=int(mv.version),
                    stage=mv.current_stage,
                    created_at=str(mv.creation_timestamp),
                    metrics={},
                    params={},
                    run_id=mv.run_id,
                )
            )
        return sorted(out, key=lambda v: v.version)

    def promote(self, version: int, stage: str) -> ModelVersion:  # pragma: no cover
        if stage not in STAGES:
            raise RegistryError(f"invalid stage {stage!r}")
        self._client.transition_model_version_stage(
            name=self.model_name,
            version=str(version),
            stage=stage,
            archive_existing_versions=(stage == PRODUCTION),
        )
        return self.get_version(version)

    def get_version(self, version: int) -> ModelVersion:  # pragma: no cover
        for v in self.list_versions():
            if v.version == version:
                return v
        raise RegistryError(f"version {version} not found")

    def current(self, stage: str = PRODUCTION) -> ModelVersion | None:  # pragma: no cover
        matches = [v for v in self.list_versions() if v.stage == stage]
        return max(matches, key=lambda v: v.version) if matches else None

    def load_model(self, version: int | None = None, stage: str = PRODUCTION) -> Any:  # pragma: no cover
        if version is None:
            uri = f"models:/{self.model_name}/{stage}"
        else:
            uri = f"models:/{self.model_name}/{version}"
        return self._mlflow.sklearn.load_model(uri)
