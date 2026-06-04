"""Document loading, chunking, and a synthetic Vietnamese-friendly corpus.

Everything here uses only base deps so ingestion and tests run fully offline.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SUPPORTED_SUFFIXES = {".txt", ".md"}

# A tiny self-contained SME knowledge base used when no docs are supplied.
# Bilingual (VI/EN) so the chunker/embedder are exercised on Vietnamese text.
SYNTHETIC_DOCS: dict[str, str] = {
    "chinh_sach_nghi_phep.md": (
        "# Chinh sach nghi phep\n\n"
        "Nhan vien chinh thuc duoc huong 12 ngay nghi phep co luong moi nam. "
        "Ngay phep duoc cong don theo thang lam viec, moi thang tuong ung mot ngay. "
        "Nghi phep phai duoc dang ky truoc it nhat ba ngay lam viec qua he thong HR. "
        "Ngay phep chua dung trong nam co the chuyen sang quy mot cua nam sau.\n"
    ),
    "quy_trinh_hoan_tien.md": (
        "# Quy trinh hoan tien\n\n"
        "Khach hang co the yeu cau hoan tien trong vong 30 ngay ke tu ngay mua. "
        "Yeu cau hoan tien duoc xu ly trong 5 den 7 ngay lam viec. "
        "Khoan hoan tien se duoc tra ve dung phuong thuc thanh toan ban dau. "
        "San pham ky thuat so da kich hoat khong duoc hoan tien.\n"
    ),
    "bao_mat_du_lieu.md": (
        "# Bao mat du lieu\n\n"
        "Moi du lieu khach hang duoc ma hoa khi luu tru va khi truyen tai. "
        "Mat khau nguoi dung duoc bam bang thuat toan bcrypt. "
        "Quyen truy cap du lieu tuan theo nguyen tac least privilege. "
        "Su co bao mat phai duoc bao cao cho doi ngu security trong vong 24 gio.\n"
    ),
    "onboarding.md": (
        "# Huong dan onboarding\n\n"
        "Nhan vien moi nhan laptop va tai khoan trong ngay dau tien. "
        "Tuan dau tien tap trung vao dao tao san pham va quy trinh noi bo. "
        "Moi nhan vien moi duoc gan mot mentor trong 30 ngay dau. "
        "Hoan thanh khoa dao tao bao mat bat buoc truoc khi truy cap he thong production.\n"
    ),
}


@dataclass
class Chunk:
    """A retrievable unit of text plus provenance metadata."""

    id: str
    text: str
    source: str
    chunk_index: int
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "source": self.source,
            "chunk_index": self.chunk_index,
            "metadata": self.metadata,
        }


def _normalise_whitespace(text: str) -> str:
    # Collapse runs of whitespace but keep paragraph boundaries readable.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(
    text: str,
    *,
    chunk_size: int = 400,
    overlap: int = 80,
) -> list[str]:
    """Split text into overlapping character windows on whitespace boundaries.

    Sliding window with overlap preserves context across chunk edges, which
    materially improves retrieval recall for questions that straddle a split.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be in [0, chunk_size)")

    text = _normalise_whitespace(text)
    if not text:
        return []
    if len(text) <= chunk_size:
        return [text]

    chunks: list[str] = []
    start = 0
    step = chunk_size - overlap
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        # Prefer to break on a space near the window end (avoid cutting words).
        if end < n:
            window = text[start:end]
            cut = window.rfind(" ")
            if cut > step // 2:  # only honour the boundary if it isn't too early
                end = start + cut
        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= n:
            break
        start = end - overlap if (end - overlap) > start else end
    return chunks


def _chunk_id(source: str, index: int, text: str) -> str:
    digest = hashlib.sha1(f"{source}:{index}:{text}".encode()).hexdigest()
    return digest[:16]


def chunk_document(
    text: str,
    source: str,
    *,
    chunk_size: int = 400,
    overlap: int = 80,
) -> list[Chunk]:
    """Chunk one document's text into Chunk objects with stable ids."""
    pieces = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    return [
        Chunk(
            id=_chunk_id(source, i, piece),
            text=piece,
            source=source,
            chunk_index=i,
            metadata={"source": source, "chunk_index": i},
        )
        for i, piece in enumerate(pieces)
    ]


def load_documents(paths: list[str | Path]) -> dict[str, str]:
    """Read .txt/.md files (or every supported file under a directory).

    Returns a mapping of source-name -> raw text. Unsupported/missing paths are
    skipped silently so a partial corpus still ingests.
    """
    docs: dict[str, str] = {}
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file() and child.suffix.lower() in SUPPORTED_SUFFIXES:
                    docs[child.name] = child.read_text(encoding="utf-8")
        elif path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
            docs[path.name] = path.read_text(encoding="utf-8")
    return docs


def synthetic_corpus() -> dict[str, str]:
    """Return the bundled in-memory fallback corpus (deterministic)."""
    return dict(SYNTHETIC_DOCS)


def build_chunks(
    docs: dict[str, str],
    *,
    chunk_size: int = 400,
    overlap: int = 80,
) -> list[Chunk]:
    """Chunk a mapping of source -> text into a flat list of Chunk objects."""
    chunks: list[Chunk] = []
    for source, text in docs.items():
        chunks.extend(
            chunk_document(text, source, chunk_size=chunk_size, overlap=overlap)
        )
    return chunks
