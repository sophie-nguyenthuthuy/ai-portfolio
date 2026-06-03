# Section 12 · Lecture 5 — Pipeline RAG cơ bản — ingest → embed → retrieve → augment → generate

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 05
- SECTION 12 · LECTURE 05
- Pipeline RAG cơ bản — ingest → embed → retrieve → augment → generate
- ~9 phút · 6 slides

### Slide 2

- L05 · PIPELINE RAG
- Ingest & chunk
- Nạp tài liệu, cắt chunk
- Docs
- →
- Chunks

### Slide 3

- L05 · PIPELINE RAG
- Embed & index
- Tạo embedding → lưu vector DB
- Làm một lần lúc dựng hệ thống
- Chunks
- →
- Vectors
- →
- Vector DB

### Slide 4

- L05 · PIPELINE RAG
- Retrieve
- Embed câu hỏi → tìm chunk gần nhất
- Chọn top-k phù hợp
- Query
- →
- Top-k chunks

### Slide 5

- L05 · PIPELINE RAG
- Augment & generate
- Gắn chunk vào prompt → LLM trả lời
- Trả lời dựa trên tài liệu thật
- Chunks + Prompt
- →
- LLM
- →
- Answer

### Slide 6

- L05 · PIPELINE RAG — TÓM TẮT
- Tóm tắt
- ingest
- embed
- retrieve
- generate
- BÀI TIẾP
- Hybrid search & reranker
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_