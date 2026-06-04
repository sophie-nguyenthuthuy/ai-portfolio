"""Model factory: sklearn TF-IDF + LogisticRegression (default) or PhoBERT.

The sklearn pipeline is the offline default used by tests. The PhoBERT path is
config-selected and imports ``transformers``/``torch`` lazily so importing this
module never requires the heavy dependencies.
"""

from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .config import Settings
from .data import segment


def build_sklearn_pipeline(settings: Settings) -> Pipeline:
    """TF-IDF (word + char n-grams) feeding a multinomial LogisticRegression."""
    vectorizer = TfidfVectorizer(
        preprocessor=segment,
        ngram_range=(1, settings.tfidf_ngram_max),
        max_features=settings.tfidf_max_features,
        min_df=1,
        sublinear_tf=True,
    )
    clf = LogisticRegression(
        C=settings.lr_c,
        max_iter=settings.lr_max_iter,
        class_weight="balanced",
        random_state=settings.random_seed,
    )
    return Pipeline([("tfidf", vectorizer), ("clf", clf)])


class PhoBERTClassifier:
    """Thin wrapper around a PhoBERT sequence-classification model.

    Heavy deps (``transformers``, ``torch``) are imported only when this class is
    instantiated, keeping the default import surface light. Not exercised in the
    offline unit suite — covered by integration tests.
    """

    def __init__(self, settings: Settings) -> None:  # pragma: no cover - integration
        import torch  # noqa: F401
        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
        )

        self.settings = settings
        self.tokenizer = AutoTokenizer.from_pretrained(settings.phobert_model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            settings.phobert_model_name, num_labels=3
        )
        self.model.eval()

    def predict_proba(self, texts: list[str]):  # pragma: no cover - integration
        import torch

        encoded = self.tokenizer(
            [segment(t) for t in texts],
            padding=True,
            truncation=True,
            max_length=self.settings.max_seq_len,
            return_tensors="pt",
        )
        with torch.no_grad():
            logits = self.model(**encoded).logits
            probs = torch.softmax(logits, dim=-1)
        return probs.cpu().numpy()


def build_model(settings: Settings):
    """Return a model object according to ``settings.model_backend``."""
    if settings.model_backend == "phobert":
        return PhoBERTClassifier(settings)
    return build_sklearn_pipeline(settings)
