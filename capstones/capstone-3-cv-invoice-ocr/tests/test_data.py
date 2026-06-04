"""Tests for synthetic image generation, dataset building, and features."""

from __future__ import annotations

import numpy as np
import pytest

from vision.data import (
    build_synthetic_dataset,
    generate_synthetic_image,
    load_dataset,
    materialize_dataset,
)
from vision.features import extract_features, feature_matrix, image_stats, preprocess


def test_generate_is_deterministic(labels):
    a = generate_synthetic_image("invoice", size=48, seed=3)
    b = generate_synthetic_image("invoice", size=48, seed=3)
    assert np.array_equal(np.asarray(a), np.asarray(b))
    assert a.size == (48, 48)
    assert a.mode == "RGB"


def test_classes_are_visually_distinct(labels):
    # Mean brightness differs across classes -> separable features.
    brightness = {
        lab: image_stats(generate_synthetic_image(lab, size=48, seed=0))["brightness"]
        for lab in labels
    }
    assert len(set(round(v) for v in brightness.values())) >= 3


def test_unknown_label_raises():
    with pytest.raises(ValueError):
        generate_synthetic_image("passport")


def test_build_synthetic_dataset(labels):
    ds = build_synthetic_dataset(labels, samples_per_class=5, size=32, seed=1)
    assert len(ds) == len(labels) * 5
    assert ds.label_names == labels
    assert set(ds.labels) == set(range(len(labels)))


def test_load_dataset_roundtrip_from_folder(tmp_path, labels):
    ds = build_synthetic_dataset(labels, samples_per_class=3, size=32, seed=1)
    root = materialize_dataset(ds, tmp_path / "imgs")
    loaded = load_dataset(root, labels=labels, size=32)
    assert len(loaded) == len(ds)
    assert loaded.label_names == labels


def test_load_dataset_falls_back_to_synthetic(tmp_path, labels):
    ds = load_dataset(tmp_path / "missing", labels=labels, samples_per_class=4, size=32)
    assert len(ds) == len(labels) * 4


def test_feature_extraction_shapes(labels):
    img = generate_synthetic_image("receipt", size=48, seed=0)
    feats = extract_features(img, size=48)
    assert feats.ndim == 1 and feats.shape[0] == 7
    ds = build_synthetic_dataset(labels, samples_per_class=2, size=32, seed=0)
    mat = feature_matrix(ds.images, size=32)
    assert mat.shape == (len(ds), 7)


def test_preprocess_channel_first_normalized():
    img = generate_synthetic_image("id_card", size=64, seed=0)
    arr = preprocess(img, size=64, normalize=True)
    assert arr.shape == (3, 64, 64)
    assert arr.dtype == np.float32
    # Normalized values should be roughly zero-mean, not in [0,255].
    assert arr.max() < 10.0
