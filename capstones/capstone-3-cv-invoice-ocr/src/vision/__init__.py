"""Computer-vision capstone: document image classification + invoice OCR.

Light import surface: heavy/optional libs (torch, torchvision, pytesseract,
easyocr, mlflow) are imported lazily inside functions so ``import vision`` works
with base deps only. When torch is absent a numpy ``DummyClassifier`` is used,
and OCR falls back to a deterministic stub so the unit tests run fully offline.
"""

__version__ = "0.1.0"
