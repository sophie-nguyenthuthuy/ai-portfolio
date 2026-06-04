"""Train -> predict on synthetic data, plus drift checks."""

from __future__ import annotations

from pathlib import Path

import pytest
from monitoring.drift import detect_drift

from nlpvi import predict as predict_mod
from nlpvi.data import generate_synthetic
from nlpvi.predict import predict
from nlpvi.train import train_model


def test_train_produces_artifact_and_scores(settings):
    result = train_model(settings, use_mlflow=False)
    assert Path(result.model_path).exists()
    assert Path(result.model_path).with_suffix(".meta.json").exists()
    # synthetic signal is strong -> model should learn it well
    assert result.macro_f1 >= 0.8
    assert result.accuracy >= 0.8
    assert set(result.per_class.keys()) == {"negative", "neutral", "positive"}
    assert result.n_train > 0 and result.n_test > 0


def test_predict_returns_well_formed_scores(trained_model):
    settings, _ = trained_model
    predict_mod.reset_cache()
    out = predict(
        [
            "Sản phẩm tuyệt vời, rất hài lòng, sẽ mua lại",
            "Hàng tệ hại, kém chất lượng, thất vọng",
        ],
        settings=settings,
    )
    assert len(out) == 2
    for item in out:
        assert item["label"] in {"negative", "neutral", "positive"}
        s = item["scores"]
        assert set(s.keys()) == {"negative", "neutral", "positive"}
        assert abs(sum(s.values()) - 1.0) < 1e-3
    assert out[0]["label"] == "positive"
    assert out[1]["label"] == "negative"


def test_predict_empty_list(trained_model):
    settings, _ = trained_model
    assert predict([], settings=settings) == []


def test_predict_type_validation(trained_model):
    settings, _ = trained_model
    with pytest.raises(TypeError):
        predict("not a list", settings=settings)  # type: ignore[arg-type]


def test_drift_no_drift_same_distribution():
    df = generate_synthetic(600, seed=1)
    texts = df["text"].tolist()
    report = detect_drift(texts[:300], texts[300:])
    assert not report.drifted
    assert report.length_psi < 0.25
    assert report.vocab_psi < 0.25


def test_drift_flags_distribution_shift():
    ref = generate_synthetic(120, seed=1)["text"].tolist()
    current = ["x" * 300 for _ in range(120)]  # very different length + vocab
    report = detect_drift(ref, current)
    assert report.drifted
    assert report.vocab_psi > 0.25
