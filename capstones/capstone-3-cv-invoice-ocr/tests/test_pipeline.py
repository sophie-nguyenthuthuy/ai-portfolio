"""Train -> predict on synthetic data; OCR stub + field parsing; drift check."""

from __future__ import annotations

import math

import pytest

from vision.model import DummyClassifier, resolve_backend
from vision.ocr import parse_fields, run_ocr
from vision.pipeline import stratified_split, train_pipeline
from vision.predict import classify, load_model, ocr


def test_resolve_backend_dummy_offline():
    # torch is not installed in the test env, so auto -> dummy.
    assert resolve_backend("auto") == "dummy"
    assert resolve_backend("dummy") == "dummy"


def test_stratified_split_keeps_classes_in_train():
    labels = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    train_idx, test_idx = stratified_split(len(labels), labels, test_fraction=0.34, seed=0)
    train_labels = {labels[i] for i in train_idx}
    assert train_labels == {0, 1, 2}
    assert set(train_idx).isdisjoint(test_idx)


def test_train_pipeline_learns_synthetic(settings):
    result = train_pipeline(settings, backend="dummy", save=True)
    assert result.backend == "dummy"
    assert isinstance(result.model, DummyClassifier)
    # Synthetic classes are designed to be separable -> high accuracy.
    assert result.metrics["accuracy"] >= 0.75
    assert not math.isnan(result.metrics["macro_f1"])
    # Confusion matrix is square over the label space.
    n = len(settings.labels)
    assert len(result.confusion_matrix) == n
    assert all(len(row) == n for row in result.confusion_matrix)
    # Artifact + label map persisted.
    assert result.artifact_path is not None and result.artifact_path.exists()
    assert (settings.resolved_model_dir() / "labels.json").exists()


def test_load_model_trains_when_missing(settings):
    model, metadata = load_model(settings)
    assert metadata["backend"] == "dummy"
    assert metadata["label_names"] == settings.labels


def test_classify_predicts_correct_label(settings, image_bytes_for):
    train_pipeline(settings, backend="dummy", save=True)
    for label in settings.labels:
        data = image_bytes_for(label, size=settings.image_size, seed=7)
        out = classify(data, settings=settings)
        assert out["label"] in settings.labels
        assert 0.0 <= out["confidence"] <= 1.0
        assert pytest.approx(sum(out["probs"].values()), abs=1e-3) == 1.0
    # The invoice image should classify as invoice given the distinct layout.
    inv = classify(image_bytes_for("invoice", size=settings.image_size, seed=1), settings=settings)
    assert inv["label"] == "invoice"


def test_ocr_stub_parses_fields(settings, image_bytes_for):
    data = image_bytes_for("invoice", size=settings.image_size, seed=0)
    out = ocr(data, settings=settings)
    assert out["engine"] == "stub"
    assert "TOTAL" in out["text"]
    assert out["fields"]["total"] is not None
    assert out["fields"]["date"] == "2026-06-04"
    assert out["fields"]["invoice_no"] == "INV-2026-0042"


def test_parse_fields_regex_variants():
    text = "Grand Total: $1,234.56\nDate 04/06/2026\nInvoice No: A-99"
    fields = parse_fields(text)
    assert fields["total"] == 1234.56
    assert fields["date"] == "04/06/2026"
    assert fields["invoice_no"] == "A-99"


def test_run_ocr_default_engine_is_stub(image_bytes_for):
    data = image_bytes_for("receipt", size=48, seed=2)
    out = run_ocr(data, engine="auto")
    assert out["engine"] == "stub"


def test_drift_detects_brightness_shift(synthetic_dataset):
    from monitoring.drift import detect_drift

    ref = synthetic_dataset.images
    report = detect_drift(ref, ref)
    assert report.drift is False
    assert report.severity == "none"
