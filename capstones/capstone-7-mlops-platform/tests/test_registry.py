"""Tests for the LocalRegistry: versioning, stage transitions, load."""

from __future__ import annotations

import pytest

from mlops.registry import PRODUCTION, STAGING, LocalRegistry, RegistryError
from mlops.train import train_core


def _fit(settings, synth_df):
    return train_core(settings, df=synth_df).pipeline


def test_register_increments_versions(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    v1 = reg.register(_fit(settings, synth_df), metrics={"roc_auc": 0.8})
    v2 = reg.register(_fit(settings, synth_df), metrics={"roc_auc": 0.82})
    assert v1.version == 1 and v2.version == 2
    assert v1.stage == "None"
    versions = reg.list_versions()
    assert [v.version for v in versions] == [1, 2]


def test_promote_to_production_archives_previous(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    reg.register(_fit(settings, synth_df), metrics={"roc_auc": 0.8})
    reg.register(_fit(settings, synth_df), metrics={"roc_auc": 0.82})

    reg.promote(1, PRODUCTION)
    assert reg.current(PRODUCTION).version == 1

    reg.promote(2, PRODUCTION)
    # v2 is now live; v1 was archived automatically.
    assert reg.current(PRODUCTION).version == 2
    assert reg.get_version(1).stage == "Archived"


def test_promote_to_staging(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    reg.register(_fit(settings, synth_df))
    reg.promote(1, STAGING)
    assert reg.current(STAGING).version == 1
    assert reg.current(PRODUCTION) is None


def test_load_production_model_roundtrip(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    reg.register(_fit(settings, synth_df))
    reg.promote(1, PRODUCTION)
    model = reg.load_model(stage=PRODUCTION)
    proba = model.predict_proba(synth_df.drop(columns=["churn"]).head(3))
    assert proba.shape == (3, 2)


def test_invalid_stage_and_missing_version(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    reg.register(_fit(settings, synth_df))
    with pytest.raises(RegistryError):
        reg.promote(1, "Nonsense")
    with pytest.raises(RegistryError):
        reg.get_version(99)
    with pytest.raises(RegistryError):
        LocalRegistry(settings.resolved_registry_dir, model_name="empty").load_model(stage=PRODUCTION)


def test_persistence_across_instances(settings, synth_df):
    reg = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    reg.register(_fit(settings, synth_df))
    reg.promote(1, PRODUCTION)
    # A fresh instance reads the same on-disk manifest.
    reopened = LocalRegistry(settings.resolved_registry_dir, model_name="m")
    assert reopened.current(PRODUCTION).version == 1
