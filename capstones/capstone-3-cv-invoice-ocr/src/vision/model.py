"""Classifier models: a numpy ``DummyClassifier`` (base deps) and a lazily
imported torchvision ResNet18 transfer-learning wrapper.

Both expose the same minimal interface so ``train``/``predict`` are
backend-agnostic::

    model.fit(images, labels) -> self
    model.predict_proba(images) -> np.ndarray   # (N, n_classes)
    model.classify_one(image)   -> (label_index, confidence)
    model.label_names           -> list[str]

The DummyClassifier is a genuine scikit-learn pipeline over layout-aware image
features (see ``features.py``) — it learns class boundaries, it is not a
hard-coded rule.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from .features import feature_matrix
from .logging_conf import get_logger

log = get_logger(__name__)


def torch_available() -> bool:
    """True only if both torch and torchvision import cleanly."""
    try:
        import torch  # noqa: F401
        import torchvision  # noqa: F401
    except Exception:
        return False
    return True


def resolve_backend(backend: str) -> str:
    """Map ``auto`` to ``torch`` when available, else ``dummy``."""
    backend = (backend or "auto").lower()
    if backend == "auto":
        return "torch" if torch_available() else "dummy"
    if backend == "torch" and not torch_available():
        log.warning("torch backend requested but unavailable — using dummy")
        return "dummy"
    return backend


class DummyClassifier:
    """Offline classifier: StandardScaler + LogisticRegression over image stats."""

    backend = "dummy"

    def __init__(self, label_names: list[str], *, image_size: int = 64, seed: int = 42):
        self.label_names = list(label_names)
        self.image_size = int(image_size)
        self.seed = int(seed)
        self._pipeline: Any | None = None

    @property
    def n_classes(self) -> int:
        return len(self.label_names)

    def _build_pipeline(self):
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler

        return Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                (
                    "clf",
                    LogisticRegression(
                        max_iter=500,
                        random_state=self.seed,
                    ),
                ),
            ]
        )

    def fit(self, images: list, labels: list[int]) -> "DummyClassifier":
        x = feature_matrix(images, size=self.image_size)
        y = np.asarray(labels, dtype=int)
        if x.shape[0] == 0:
            raise ValueError("cannot fit on an empty dataset")
        self._pipeline = self._build_pipeline()
        # Guard the degenerate single-class case (LogReg needs >=2 classes).
        if len(np.unique(y)) < 2:
            from sklearn.dummy import DummyClassifier as SkDummy

            self._pipeline.steps[-1] = ("clf", SkDummy(strategy="most_frequent"))
        self._pipeline.fit(x, y)
        log.info("DummyClassifier fitted on %d samples", x.shape[0])
        return self

    def predict_proba(self, images: list) -> np.ndarray:
        if self._pipeline is None:
            raise RuntimeError("model is not fitted")
        x = feature_matrix(images, size=self.image_size)
        proba = self._pipeline.predict_proba(x)
        # Re-map onto the full label space in case some classes were absent.
        classes = self._pipeline.named_steps["clf"].classes_
        full = np.zeros((proba.shape[0], self.n_classes), dtype=float)
        for col, cls in enumerate(classes):
            full[:, int(cls)] = proba[:, col]
        return full

    def classify_one(self, image) -> tuple[int, float]:
        proba = self.predict_proba([image])[0]
        idx = int(np.argmax(proba))
        return idx, float(proba[idx])


class ResNetClassifier:
    """ResNet18 transfer-learning wrapper (torch/torchvision imported lazily)."""

    backend = "torch"

    def __init__(
        self,
        label_names: list[str],
        *,
        image_size: int = 224,
        epochs: int = 3,
        batch_size: int = 8,
        learning_rate: float = 1e-3,
        seed: int = 42,
    ):
        self.label_names = list(label_names)
        self.image_size = int(image_size)
        self.epochs = int(epochs)
        self.batch_size = int(batch_size)
        self.learning_rate = float(learning_rate)
        self.seed = int(seed)
        self._net: Any | None = None

    @property
    def n_classes(self) -> int:
        return len(self.label_names)

    def _tensor_batch(self, images: list):
        import numpy as _np
        import torch

        from .features import preprocess

        batch = _np.stack([preprocess(img, size=self.image_size) for img in images])
        return torch.from_numpy(batch).float()

    def _build_net(self):
        import torch.nn as nn
        import torchvision

        torchvision_models = torchvision.models
        try:  # newer torchvision API
            weights = torchvision_models.ResNet18_Weights.DEFAULT
            net = torchvision_models.resnet18(weights=weights)
        except Exception:  # pragma: no cover - older torchvision fallback
            net = torchvision_models.resnet18(pretrained=True)
        # Freeze the backbone, replace + train only the classification head.
        for param in net.parameters():
            param.requires_grad = False
        net.fc = nn.Linear(net.fc.in_features, self.n_classes)
        return net

    def fit(self, images: list, labels: list[int]) -> "ResNetClassifier":
        import torch
        import torch.nn as nn

        torch.manual_seed(self.seed)
        self._net = self._build_net()
        self._net.train()

        x = self._tensor_batch(images)
        y = torch.tensor(labels, dtype=torch.long)
        criterion = nn.CrossEntropyLoss()
        optim = torch.optim.Adam(self._net.fc.parameters(), lr=self.learning_rate)

        n = x.shape[0]
        for epoch in range(self.epochs):
            perm = torch.randperm(n)
            total = 0.0
            for start in range(0, n, self.batch_size):
                idx = perm[start : start + self.batch_size]
                optim.zero_grad()
                out = self._net(x[idx])
                loss = criterion(out, y[idx])
                loss.backward()
                optim.step()
                total += float(loss.item())
            log.info("resnet epoch %d/%d loss=%.4f", epoch + 1, self.epochs, total)
        self._net.eval()
        return self

    def predict_proba(self, images: list) -> np.ndarray:
        import torch

        if self._net is None:
            raise RuntimeError("model is not fitted")
        self._net.eval()
        with torch.no_grad():
            logits = self._net(self._tensor_batch(images))
            proba = torch.softmax(logits, dim=1).cpu().numpy()
        return proba

    def classify_one(self, image) -> tuple[int, float]:
        proba = self.predict_proba([image])[0]
        idx = int(np.argmax(proba))
        return idx, float(proba[idx])


def build_classifier(backend: str, label_names: list[str], *, settings=None):
    """Construct a classifier for the resolved backend."""
    backend = resolve_backend(backend)
    if backend == "torch":
        kwargs: dict[str, Any] = {}
        if settings is not None:
            kwargs = {
                "image_size": settings.resnet_size,
                "epochs": settings.epochs,
                "batch_size": settings.batch_size,
                "learning_rate": settings.learning_rate,
                "seed": settings.seed,
            }
        return ResNetClassifier(label_names, **kwargs)

    kwargs = {}
    if settings is not None:
        kwargs = {"image_size": settings.image_size, "seed": settings.seed}
    return DummyClassifier(label_names, **kwargs)
