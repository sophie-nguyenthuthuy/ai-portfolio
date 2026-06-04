"""LocalRegistry: a base-deps model registry (versioned joblib + JSON manifest).

Layout on disk::

    <registry_dir>/<model_name>/
        manifest.json                # registry state (versions + stages)
        v1/model.joblib              # the fitted sklearn Pipeline
        v1/metadata.json            # params/metrics for that version
        v2/...

Stage transitions mirror MLflow's Model Registry semantics: a version is
registered with stage ``None`` and can be promoted to ``Staging`` or
``Production``. Promoting a version to ``Production`` archives any other
version currently in ``Production`` so exactly one is live at a time.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import joblib

from ..logging_conf import get_logger

logger = get_logger(__name__)

NONE = "None"
STAGING = "Staging"
PRODUCTION = "Production"
ARCHIVED = "Archived"
STAGES = (NONE, STAGING, PRODUCTION, ARCHIVED)


class RegistryError(RuntimeError):
    """Raised on invalid registry operations (missing version, bad stage, ...)."""


@dataclass
class ModelVersion:
    """A single registered model version."""

    version: int
    stage: str
    created_at: str
    metrics: dict[str, float]
    params: dict[str, Any]
    run_id: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class LocalRegistry:
    """File-backed model registry with stage transitions (no external services)."""

    def __init__(self, root: str | Path, model_name: str = "model") -> None:
        self.root = Path(root)
        self.model_name = model_name
        self.model_root = self.root / model_name
        self.model_root.mkdir(parents=True, exist_ok=True)
        self.manifest_path = self.model_root / "manifest.json"
        if not self.manifest_path.exists():
            self._write_manifest({"model_name": model_name, "versions": []})

    # ----- manifest io -----
    def _read_manifest(self) -> dict[str, Any]:
        return json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def _write_manifest(self, data: dict[str, Any]) -> None:
        self.manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _version_dir(self, version: int) -> Path:
        return self.model_root / f"v{version}"

    # ----- public api -----
    def register(
        self,
        model: Any,
        metrics: dict[str, float] | None = None,
        params: dict[str, Any] | None = None,
        run_id: str | None = None,
    ) -> ModelVersion:
        """Persist a fitted model as a new version (stage=None)."""
        manifest = self._read_manifest()
        next_version = 1 + max((v["version"] for v in manifest["versions"]), default=0)

        vdir = self._version_dir(next_version)
        vdir.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, vdir / "model.joblib")

        mv = ModelVersion(
            version=next_version,
            stage=NONE,
            created_at=datetime.now(UTC).isoformat(),
            metrics=metrics or {},
            params=params or {},
            run_id=run_id,
        )
        (vdir / "metadata.json").write_text(json.dumps(mv.as_dict(), indent=2), encoding="utf-8")

        manifest["versions"].append(mv.as_dict())
        self._write_manifest(manifest)
        logger.info("registered model version", extra={"version": next_version})
        return mv

    def list_versions(self) -> list[ModelVersion]:
        manifest = self._read_manifest()
        return [ModelVersion(**v) for v in sorted(manifest["versions"], key=lambda v: v["version"])]

    def get_version(self, version: int) -> ModelVersion:
        for v in self.list_versions():
            if v.version == version:
                return v
        raise RegistryError(f"version {version} not found for model {self.model_name!r}")

    def promote(self, version: int, stage: str) -> ModelVersion:
        """Transition a version to a new stage.

        Promoting to Production archives any other current Production version.
        """
        if stage not in STAGES:
            raise RegistryError(f"invalid stage {stage!r}; expected one of {STAGES}")

        manifest = self._read_manifest()
        versions = {v["version"]: v for v in manifest["versions"]}
        if version not in versions:
            raise RegistryError(f"version {version} not found")

        if stage == PRODUCTION:
            for v in manifest["versions"]:
                if v["version"] != version and v["stage"] == PRODUCTION:
                    v["stage"] = ARCHIVED
                    logger.info("archived previous production", extra={"version": v["version"]})

        versions[version]["stage"] = stage
        self._write_manifest(manifest)
        self._sync_version_metadata(versions[version])
        logger.info("promoted version", extra={"version": version, "stage": stage})
        return ModelVersion(**versions[version])

    def _sync_version_metadata(self, version_dict: dict[str, Any]) -> None:
        vdir = self._version_dir(version_dict["version"])
        (vdir / "metadata.json").write_text(json.dumps(version_dict, indent=2), encoding="utf-8")

    def current(self, stage: str = PRODUCTION) -> ModelVersion | None:
        """Return the (latest) version in the given stage, or None."""
        matches = [v for v in self.list_versions() if v.stage == stage]
        return max(matches, key=lambda v: v.version) if matches else None

    def load_model(self, version: int | None = None, stage: str = PRODUCTION) -> Any:
        """Load a fitted model: by explicit version, else the current stage version."""
        if version is None:
            mv = self.current(stage)
            if mv is None:
                raise RegistryError(f"no model in stage {stage!r}")
            version = mv.version
        path = self._version_dir(version) / "model.joblib"
        if not path.exists():
            raise RegistryError(f"model artifact missing for version {version}")
        logger.info("loaded model from registry", extra={"version": version})
        return joblib.load(path)
