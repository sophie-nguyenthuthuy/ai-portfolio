"""Image preprocessing + feature extraction (PIL + numpy, base deps only).

Two preprocessing paths share these helpers:

* ``preprocess`` resizes/normalizes an image to a ``CxHxW`` float tensor-like
  numpy array — usable to feed either a ResNet (via torch later) or the dummy
  path.
* ``image_stats`` / ``extract_features`` compute compact, layout-aware numeric
  features the ``DummyClassifier`` learns on, so the offline path is real ML and
  not a hard-coded rule.
"""

from __future__ import annotations

import io

import numpy as np

# ImageNet normalization constants (used for the real ResNet path).
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


def _require_pil():
    from PIL import Image

    return Image


def load_image(image_bytes: bytes):
    """Decode raw image bytes into an RGB ``PIL.Image``."""
    Image = _require_pil()
    img = Image.open(io.BytesIO(image_bytes))
    return img.convert("RGB")


def to_array(image, *, size: int) -> np.ndarray:
    """Resize ``image`` to ``size x size`` and return an ``HxWx3`` uint8 array."""
    Image = _require_pil()
    if not isinstance(image, Image.Image):
        raise TypeError("expected a PIL.Image")
    resized = image.resize((int(size), int(size)))
    return np.asarray(resized, dtype=np.uint8)


def preprocess(image, *, size: int, normalize: bool = True) -> np.ndarray:
    """Return a normalized ``3 x size x size`` float32 array (channel-first).

    With ``normalize=True`` applies ImageNet mean/std — matching what a
    torchvision ResNet expects.
    """
    arr = to_array(image, size=size).astype(np.float32) / 255.0
    if normalize:
        arr = (arr - IMAGENET_MEAN) / IMAGENET_STD
    return np.transpose(arr, (2, 0, 1)).astype(np.float32)


def image_stats(image, *, size: int = 64) -> dict[str, float]:
    """Human-readable per-image statistics (used by drift + features)."""
    arr = to_array(image, size=size).astype(np.float32)
    gray = arr.mean(axis=2)
    h, w = gray.shape
    top = gray[: h // 2, :].mean()
    bottom = gray[h // 2 :, :].mean()
    left = gray[:, : w // 2].mean()
    right = gray[:, w // 2 :].mean()
    # vertical structure: row-to-row variation captures dense "text rows".
    row_means = gray.mean(axis=1)
    return {
        "brightness": float(gray.mean()),
        "contrast": float(gray.std()),
        "top_bottom_ratio": float((top + 1.0) / (bottom + 1.0)),
        "left_right_ratio": float((left + 1.0) / (right + 1.0)),
        "row_variation": float(row_means.std()),
        "channel_spread": float(arr.reshape(-1, 3).std(axis=0).mean()),
        "aspect": float(w / max(h, 1)),
    }


_FEATURE_ORDER = (
    "brightness",
    "contrast",
    "top_bottom_ratio",
    "left_right_ratio",
    "row_variation",
    "channel_spread",
    "aspect",
)


def extract_features(image, *, size: int = 64) -> np.ndarray:
    """Flatten ``image_stats`` into a fixed-order feature vector."""
    stats = image_stats(image, size=size)
    return np.array([stats[k] for k in _FEATURE_ORDER], dtype=np.float32)


def feature_matrix(images, *, size: int = 64) -> np.ndarray:
    """Stack ``extract_features`` over a list of images into an ``N x F`` matrix."""
    if not images:
        return np.empty((0, len(_FEATURE_ORDER)), dtype=np.float32)
    return np.vstack([extract_features(img, size=size) for img in images])
