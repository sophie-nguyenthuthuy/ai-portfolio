"""Data loading + synthetic document-image generation.

Each document class has a distinct, *deterministic* visual signature so that
both the numpy ``DummyClassifier`` and a real ResNet can separate them:

* ``invoice``  — bright page, dark header band + many thin text rows (top-heavy).
* ``receipt``  — tall narrow bright strip, dense centred rows.
* ``id_card``  — mid-grey card, a coloured photo block on the left.
* ``other``    — low-contrast noisy background, no structured layout.

Images are returned as ``PIL.Image`` (RGB). ``load_dataset`` reads an
image-folder layout (``root/<label>/*.png``) when present, else builds a
synthetic dataset in memory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .config import DEFAULT_LABELS
from .logging_conf import get_logger

log = get_logger(__name__)

_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp"}


@dataclass
class ImageDataset:
    """A simple in-memory dataset: parallel lists of PIL images + integer labels."""

    images: list  # list[PIL.Image.Image]
    labels: list[int]
    label_names: list[str]

    def __len__(self) -> int:
        return len(self.images)


def _require_pil():
    try:
        from PIL import Image  # noqa: F401
    except Exception as exc:  # pragma: no cover - Pillow is a base dep
        raise RuntimeError("Pillow is required for image handling") from exc
    from PIL import Image

    return Image


def generate_synthetic_image(label: str, *, size: int = 64, seed: int | None = None):
    """Create a deterministic synthetic ``PIL.Image`` for ``label``.

    The same ``(label, size, seed)`` always yields identical pixels, which keeps
    the unit tests reproducible without any downloads.
    """
    Image = _require_pil()
    if label not in DEFAULT_LABELS:
        raise ValueError(f"unknown label {label!r}; expected one of {DEFAULT_LABELS}")

    # Seed deterministically from the label so a fixed dataset is reproducible.
    base_seed = (DEFAULT_LABELS.index(label) + 1) * 1000 + (seed or 0)
    rng = np.random.default_rng(base_seed)
    h = w = int(size)
    arr = np.zeros((h, w, 3), dtype=np.float32)

    if label == "invoice":
        arr[:] = 235.0  # bright page
        arr[: h // 6, :, :] = 40.0  # dark header band
        # thin text rows in the upper half (top-heavy layout)
        for r in range(h // 5, h // 2, 4):
            arr[r, w // 8 : w - w // 8, :] = 60.0
    elif label == "receipt":
        arr[:] = 245.0
        strip = slice(w // 3, 2 * w // 3)  # narrow centred strip
        arr[:, :, :] = 120.0
        arr[:, strip, :] = 250.0
        for r in range(h // 12, h - h // 12, 3):  # dense rows
            arr[r, strip, :] = 70.0
    elif label == "id_card":
        arr[:] = 150.0  # mid grey card
        arr[h // 8 : h - h // 8, w // 8 : w - w // 8, :] = 180.0
        # coloured photo block on the left
        arr[h // 4 : 3 * h // 4, w // 6 : w // 2, 0] = 200.0
        arr[h // 4 : 3 * h // 4, w // 6 : w // 2, 1] = 120.0
        arr[h // 4 : 3 * h // 4, w // 6 : w // 2, 2] = 90.0
    else:  # other — low-contrast noisy background
        arr[:] = 110.0

    # Per-class deterministic noise keeps within-class variety small but nonzero.
    arr = arr + rng.normal(0.0, 6.0, size=arr.shape)
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode="RGB")


def build_synthetic_dataset(
    labels=DEFAULT_LABELS,
    *,
    samples_per_class: int = 24,
    size: int = 64,
    seed: int = 42,
) -> ImageDataset:
    """Build an in-memory synthetic dataset spanning all labels."""
    label_names = list(labels)
    images: list = []
    label_ids: list[int] = []
    for idx, name in enumerate(label_names):
        for s in range(samples_per_class):
            img = generate_synthetic_image(name, size=size, seed=seed + s)
            images.append(img)
            label_ids.append(idx)
    log.info(
        "built synthetic dataset: %d images across %d classes",
        len(images),
        len(label_names),
    )
    return ImageDataset(images=images, labels=label_ids, label_names=label_names)


def load_dataset(
    path: str | Path | None,
    *,
    labels=DEFAULT_LABELS,
    samples_per_class: int = 24,
    size: int = 64,
    seed: int = 42,
) -> ImageDataset:
    """Load an image-folder dataset if present, else build a synthetic one.

    Image-folder layout::

        root/
          invoice/ a.png b.png ...
          receipt/ ...
          id_card/ ...
          other/   ...
    """
    if path is not None and Path(path).exists() and any(Path(path).iterdir()):
        Image = _require_pil()
        root = Path(path)
        present = [d.name for d in sorted(root.iterdir()) if d.is_dir()]
        label_names = [name for name in labels if name in present] or present
        images: list = []
        label_ids: list[int] = []
        for idx, name in enumerate(label_names):
            class_dir = root / name
            for fp in sorted(class_dir.iterdir()):
                if fp.suffix.lower() in _IMAGE_EXTS:
                    images.append(Image.open(fp).convert("RGB"))
                    label_ids.append(idx)
        if images:
            log.info("loaded %d images from %s", len(images), root)
            return ImageDataset(images=images, labels=label_ids, label_names=label_names)
        log.warning("no images found under %s — falling back to synthetic", root)

    log.info("no dataset at %s — using synthetic images", path)
    return build_synthetic_dataset(
        labels, samples_per_class=samples_per_class, size=size, seed=seed
    )


def materialize_dataset(dataset: ImageDataset, root: str | Path) -> Path:
    """Persist an in-memory dataset to an image-folder layout on disk."""
    root = Path(root)
    for idx, (img, lab) in enumerate(zip(dataset.images, dataset.labels)):
        class_dir = root / dataset.label_names[lab]
        class_dir.mkdir(parents=True, exist_ok=True)
        img.save(class_dir / f"{idx:05d}.png")
    log.info("materialized %d images under %s", len(dataset), root)
    return root
