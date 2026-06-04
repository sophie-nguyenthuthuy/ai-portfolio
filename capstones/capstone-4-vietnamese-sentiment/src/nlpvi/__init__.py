"""nlpvi — Vietnamese product-review sentiment analysis.

Classify Vietnamese review text into negative / neutral / positive using either
a light scikit-learn TF-IDF + LogisticRegression pipeline (default, offline) or
a PhoBERT transformer path (optional, lazy-loaded).
"""

__version__ = "0.1.0"

LABELS = ("negative", "neutral", "positive")

__all__ = ["__version__", "LABELS"]
