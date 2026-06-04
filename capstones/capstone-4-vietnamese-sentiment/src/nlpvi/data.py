"""Data loading, synthetic generation and Vietnamese word segmentation.

The synthetic generator builds deterministic Vietnamese-ish product reviews with
a strong sentiment-lexicon signal so that a small TF-IDF + LogisticRegression
model learns the three classes reliably and tests stay fully offline.
"""

from __future__ import annotations

import random
import re
from pathlib import Path

import pandas as pd

from .logging_conf import get_logger

log = get_logger(__name__)

# label ids are aligned with nlpvi.LABELS ordering
NEGATIVE, NEUTRAL, POSITIVE = 0, 1, 2
LABEL_NAMES = ("negative", "neutral", "positive")

# Vietnamese sentiment lexicon (kept ASCII-tone-free where possible but real VN
# diacritics are fine — the tokenizer and TF-IDF handle unicode).
_POS_WORDS = [
    "tuyệt vời", "rất tốt", "hài lòng", "chất lượng cao", "đáng tiền",
    "giao hàng nhanh", "đóng gói cẩn thận", "sẽ mua lại", "yêu thích", "xuất sắc",
    "bền đẹp", "giá hợp lý", "dịch vụ chu đáo", "ưng ý", "vượt mong đợi",
]
_NEG_WORDS = [
    "tệ hại", "rất kém", "thất vọng", "kém chất lượng", "không đáng tiền",
    "giao hàng chậm", "đóng gói cẩu thả", "không mua lại", "ghét", "tồi tệ",
    "mau hỏng", "giá quá đắt", "dịch vụ tệ", "không ưng", "dưới mong đợi",
]
_NEU_WORDS = [
    "bình thường", "tạm được", "không có gì đặc biệt", "đúng như mô tả",
    "ở mức trung bình", "chấp nhận được", "không quá nổi bật", "ổn",
    "giống hình", "đủ dùng", "không tệ cũng không hay", "vừa phải",
]
_PRODUCTS = [
    "sản phẩm", "chiếc áo", "đôi giày", "điện thoại", "cái túi",
    "máy lọc nước", "bộ nồi", "tai nghe", "quyển sách", "cái ghế",
]
_OPENERS = [
    "Mình thấy {p} này", "{p} nhìn chung", "Sau khi dùng {p}",
    "Đặt mua {p} và", "Theo cảm nhận của tôi {p}",
]


def segment(text: str) -> str:
    """Vietnamese word segmentation.

    Uses ``underthesea.word_tokenize`` when the optional dependency is present;
    otherwise falls back to a lowercase regex/whitespace tokenizer. The fallback
    is deterministic and keeps unit tests offline.
    """
    try:  # optional heavy dep, lazy import
        from underthesea import word_tokenize  # type: ignore

        return " ".join(word_tokenize(text))
    except Exception:  # pragma: no cover - exercised only with dep absent
        tokens = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
        return " ".join(tokens)


def _compose(rng: random.Random, sentiment: int) -> str:
    pool = {NEGATIVE: _NEG_WORDS, NEUTRAL: _NEU_WORDS, POSITIVE: _POS_WORDS}[sentiment]
    product = rng.choice(_PRODUCTS)
    opener = rng.choice(_OPENERS).format(p=product)
    phrases = rng.sample(pool, k=min(2, len(pool)))
    body = ", ".join(phrases)
    tail = {
        NEGATIVE: "không nên mua.",
        NEUTRAL: "tùy nhu cầu mỗi người.",
        POSITIVE: "rất đáng để thử.",
    }[sentiment]
    return f"{opener} {body}, {tail}".strip()


def generate_synthetic(n: int = 600, seed: int = 13) -> pd.DataFrame:
    """Generate ``n`` labeled synthetic Vietnamese reviews.

    Returns a DataFrame with columns ``text`` (str) and ``label`` (int in 0..2).
    Deterministic for a given ``seed``; classes are balanced.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    rng = random.Random(seed)
    rows: list[dict[str, object]] = []
    for i in range(n):
        sentiment = i % 3  # balanced round-robin
        rows.append({"text": _compose(rng, sentiment), "label": sentiment})
    rng.shuffle(rows)
    df = pd.DataFrame(rows)
    log.info("generated synthetic dataset rows=%d", len(df))
    return df


def load_data(path: str | Path, *, synthetic_size: int = 600, seed: int = 13) -> pd.DataFrame:
    """Load a CSV with columns ``text,label`` if it exists, else synthesize.

    The label column may be integer ids (0/1/2) or names (negative/neutral/
    positive); names are mapped to ids.
    """
    p = Path(path)
    if p.exists():
        df = pd.read_csv(p)
        missing = {"text", "label"} - set(df.columns)
        if missing:
            raise ValueError(f"CSV missing columns: {sorted(missing)}")
        if not pd.api.types.is_numeric_dtype(df["label"]):
            mapping = {name: idx for idx, name in enumerate(LABEL_NAMES)}
            df["label"] = df["label"].astype(str).str.strip().map(mapping)
        df = df.dropna(subset=["text", "label"]).reset_index(drop=True)
        df["label"] = df["label"].astype(int)
        log.info("loaded dataset path=%s rows=%d", str(p), len(df))
        return df[["text", "label"]]
    log.info("no dataset at %s; using synthetic", str(p))
    return generate_synthetic(synthetic_size, seed=seed)
