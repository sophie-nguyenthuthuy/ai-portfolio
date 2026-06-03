# Section 12 · Lecture 6 — Hybrid search — BM25 + vector + reranker

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Hybrid Search & Reranker

**🎨 Visual:** `[AI image]` Kết hợp 2 cách tìm.
**🎤 Speaker note:** "Nâng chất lượng retrieve — phần quyết định RAG tốt hay dở."

### Slide 2 — Vì sao chỉ vector chưa đủ

- Miss từ khoá chính xác (mã, tên)

**🎨 Visual:** `[Mermaid]` Vector miss keyword.
**🎤 Speaker note:** Vector giỏi nghĩa, kém khớp chính xác.

### Slide 3 — Hybrid: BM25 + vector

- BM25 (keyword) + dense (nghĩa)
- Kết hợp điểm

**🎨 Visual:** `[Mermaid]` Hybrid score.
**🎤 Speaker note:** Nối lại hybrid search Section 9.

### Slide 4 — Reranker

- Xếp lại top kết quả chính xác hơn
- BGE-reranker

**🎨 Visual:** `[Mermaid]` Retrieve → rerank.
**🎤 Speaker note:** Cải thiện đáng kể chất lượng cuối.

### Slide 5 — Pipeline nâng cấp

- Hybrid retrieve → rerank → generate

**🎨 Visual:** `[Mermaid]` Pipeline có reranker.
**🎤 Speaker note:** Đây là chuẩn cho RAG production.

### Slide 6 — Tóm tắt & chuyển bài

- hybrid · BM25+vector · reranker
- Bài tiếp: RAG nâng cao →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới các kỹ thuật RAG hiện đại."

---

_← [Về Section README](../README.md)_
