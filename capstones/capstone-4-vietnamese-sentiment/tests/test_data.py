"""Tests for data generation, loading and segmentation."""

from __future__ import annotations

import pandas as pd

from nlpvi.data import (
    LABEL_NAMES,
    generate_synthetic,
    load_data,
    segment,
)


def test_generate_synthetic_shape_and_labels():
    df = generate_synthetic(99, seed=1)
    assert list(df.columns) == ["text", "label"]
    assert len(df) == 99
    assert set(df["label"].unique()) <= {0, 1, 2}
    # balanced round-robin -> all three classes present
    assert set(df["label"].unique()) == {0, 1, 2}


def test_generate_synthetic_deterministic():
    a = generate_synthetic(50, seed=42)
    b = generate_synthetic(50, seed=42)
    pd.testing.assert_frame_equal(a, b)


def test_synthetic_has_sentiment_signal():
    df = generate_synthetic(60, seed=3)
    pos_text = " ".join(df[df["label"] == 2]["text"].tolist())
    neg_text = " ".join(df[df["label"] == 0]["text"].tolist())
    assert "đáng để thử" in pos_text
    assert "không nên mua" in neg_text


def test_segment_fallback_tokenizes():
    out = segment("Sản phẩm RẤT tốt!!!")
    assert out == out.lower()
    assert "sản" in out and "tốt" in out


def test_load_data_missing_falls_back(tmp_path):
    df = load_data(tmp_path / "nope.csv", synthetic_size=30, seed=5)
    assert len(df) == 30


def test_load_data_reads_csv_with_label_names(tmp_path):
    csv = tmp_path / "reviews.csv"
    pd.DataFrame(
        {
            "text": ["hàng tốt", "tệ quá", "bình thường"],
            "label": ["positive", "negative", "neutral"],
        }
    ).to_csv(csv, index=False)
    df = load_data(csv)
    assert df["label"].tolist() == [2, 0, 1]
    assert len(LABEL_NAMES) == 3
