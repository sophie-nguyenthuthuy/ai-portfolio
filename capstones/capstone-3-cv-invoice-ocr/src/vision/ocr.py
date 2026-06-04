"""Invoice OCR: text extraction + naive field parsing.

Engines are resolved lazily:

* ``pytesseract`` (needs the Tesseract binary) or ``easyocr`` when available;
* otherwise a deterministic ``StubOCR`` that derives text from synthetic-image
  layout stats, so tests and the offline container work without any OCR binary.

``parse_fields`` runs regexes over the extracted text to pull out a total amount
and an invoice date — the kind of light structured extraction a downstream
bookkeeping step would consume.
"""

from __future__ import annotations

import re
from typing import Any

from .features import image_stats, load_image
from .logging_conf import get_logger

log = get_logger(__name__)

# total: currency-ish number following a "total" keyword (USD/VND friendly).
_TOTAL_RE = re.compile(
    r"(?:grand\s+)?total\s*[:\-]?\s*\$?\s*([0-9][0-9.,]*\d)",
    re.IGNORECASE,
)
# date: ISO, dd/mm/yyyy, or dd-mm-yyyy.
_DATE_RE = re.compile(
    r"\b(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b"
)
_INVOICE_NO_RE = re.compile(
    r"invoice\s*(?:no\.?|number|#)\s*[:\-]?\s*([A-Za-z0-9\-]+)",
    re.IGNORECASE,
)


def pytesseract_available() -> bool:
    try:
        import pytesseract  # noqa: F401
    except Exception:
        return False
    try:  # the python pkg can import without the binary present
        import pytesseract

        pytesseract.get_tesseract_version()
    except Exception:
        return False
    return True


def easyocr_available() -> bool:
    try:
        import easyocr  # noqa: F401
    except Exception:
        return False
    return True


def resolve_engine(engine: str) -> str:
    """Map ``auto`` onto the best available engine, else the stub."""
    engine = (engine or "auto").lower()
    if engine == "auto":
        if pytesseract_available():
            return "pytesseract"
        if easyocr_available():
            return "easyocr"
        return "stub"
    return engine


def _normalize_amount(raw: str) -> float | None:
    """Parse a currency-ish string into a float, handling thousands separators."""
    cleaned = raw.strip().replace(" ", "")
    if "," in cleaned and "." in cleaned:
        # Assume comma = thousands, dot = decimal (e.g. 1,234.56).
        cleaned = cleaned.replace(",", "")
    elif "," in cleaned:
        # Ambiguous: treat trailing ",dd" as decimal else thousands.
        if re.search(r",\d{2}$", cleaned):
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
    try:
        return round(float(cleaned), 2)
    except ValueError:
        return None


def parse_fields(text: str) -> dict[str, Any]:
    """Extract ``total``, ``date`` and ``invoice_no`` from OCR text via regex."""
    total: float | None = None
    m = _TOTAL_RE.search(text)
    if m:
        total = _normalize_amount(m.group(1))

    date_m = _DATE_RE.search(text)
    invoice_m = _INVOICE_NO_RE.search(text)
    return {
        "total": total,
        "date": date_m.group(1) if date_m else None,
        "invoice_no": invoice_m.group(1) if invoice_m else None,
    }


class StubOCR:
    """Deterministic offline OCR.

    Produces a small synthetic invoice text whose total is derived from image
    brightness/contrast, so it is reproducible and exercises ``parse_fields``
    end-to-end without a Tesseract install.
    """

    engine = "stub"

    def extract_text(self, image_bytes: bytes) -> str:
        img = load_image(image_bytes)
        stats = image_stats(img)
        # Map brightness/contrast deterministically into a plausible total.
        total = round(10.0 + (stats["brightness"] % 90) + stats["contrast"] / 10.0, 2)
        return (
            "ACME SUPPLIES CO\n"
            "Invoice No: INV-2026-0042\n"
            "Date: 2026-06-04\n"
            "Item A .......... 12.00\n"
            "Item B .......... 18.00\n"
            f"TOTAL: ${total:.2f}\n"
        )


class TesseractOCR:
    engine = "pytesseract"

    def __init__(self, lang: str = "eng"):
        self.lang = lang

    def extract_text(self, image_bytes: bytes) -> str:  # pragma: no cover - needs binary
        import pytesseract

        img = load_image(image_bytes)
        return pytesseract.image_to_string(img, lang=self.lang)


class EasyOCR:
    engine = "easyocr"

    def __init__(self, lang: str = "en"):
        self.lang = lang
        self._reader = None

    def _get_reader(self):  # pragma: no cover - heavy optional dep
        if self._reader is None:
            import easyocr

            self._reader = easyocr.Reader([self.lang], gpu=False)
        return self._reader

    def extract_text(self, image_bytes: bytes) -> str:  # pragma: no cover - heavy dep
        import numpy as np

        img = load_image(image_bytes)
        reader = self._get_reader()
        results = reader.readtext(np.asarray(img), detail=0)
        return "\n".join(results)


def build_ocr_engine(engine: str = "auto", *, lang: str = "eng"):
    """Construct an OCR engine instance for the resolved engine name."""
    resolved = resolve_engine(engine)
    if resolved == "pytesseract":
        return TesseractOCR(lang=lang)
    if resolved == "easyocr":
        return EasyOCR(lang="en" if lang == "eng" else lang)
    return StubOCR()


def run_ocr(image_bytes: bytes, *, engine: str = "auto", lang: str = "eng") -> dict[str, Any]:
    """Extract text and parse fields. Returns ``{engine, text, fields}``."""
    ocr_engine = build_ocr_engine(engine, lang=lang)
    text = ocr_engine.extract_text(image_bytes)
    fields = parse_fields(text)
    log.info("ocr engine=%s chars=%d fields=%s", ocr_engine.engine, len(text), fields)
    return {"engine": ocr_engine.engine, "text": text, "fields": fields}
