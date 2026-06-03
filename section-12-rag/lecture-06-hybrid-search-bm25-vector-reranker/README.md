# Section 12 · Lecture 6 — Hybrid search — BM25 + vector + reranker

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 06
- SECTION 12 · LECTURE 06
- Hybrid search — BM25 + vector + reranker
- ~8 phút · 6 slides

### Slide 2

- L06 · HYBRID SEARCH
- Vì sao chỉ vector chưa đủ
- Miss từ khoá chính xác (mã, tên)
- Vector: giỏi nghĩa · kém khớp chính xác
- mã sản phẩm "SKU-8842" dễ bị bỏ sót

### Slide 3

- L06 · HYBRID SEARCH
- Hybrid: BM25 + vector
- BM25 (keyword) + dense (nghĩa)
- Kết hợp điểm
- BM25 + Dense vector
- khớp từ khoá × hiểu ngữ nghĩa

### Slide 4

- L06 · HYBRID SEARCH
- Reranker
- Xếp lại top kết quả chính xác hơn
- BGE-reranker
- Top-50 thô
- →
- Reranker
- →
- Top-5 tinh

### Slide 5

- L06 · HYBRID SEARCH
- Pipeline nâng cấp
- Chuẩn cho RAG production
- Hybrid retrieve
- →
- Rerank
- →
- Generate

### Slide 6

- L06 · HYBRID SEARCH — TÓM TẮT
- Tóm tắt
- hybrid
- BM25 + vector
- reranker
- BÀI TIẾP
- RAG nâng cao
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_