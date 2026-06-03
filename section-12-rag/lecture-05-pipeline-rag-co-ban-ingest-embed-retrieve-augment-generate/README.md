# Section 12 · Lecture 5 — Pipeline RAG cơ bản — ingest → embed → retrieve → augment → generate

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Pipeline RAG cơ bản

**🎨 Visual:** `[Mermaid]` 5 bước RAG.
**🎤 Speaker note:** "Bản đồ tổng thể của mọi hệ RAG."

### Slide 2 — Ingest & chunk

- Nạp tài liệu, cắt chunk

**🎨 Visual:** `[Mermaid]` Docs → chunks.
**🎤 Speaker note:** Áp dụng chunking bài trước.

### Slide 3 — Embed & index

- Tạo embedding → lưu vector DB

**🎨 Visual:** `[Mermaid]` Chunks → vectors → DB.
**🎤 Speaker note:** Làm 1 lần lúc dựng hệ thống.

### Slide 4 — Retrieve

- Embed câu hỏi → tìm chunk gần nhất

**🎨 Visual:** `[Mermaid]` Query → top-k chunks.
**🎤 Speaker note:** Chọn top-k phù hợp.

### Slide 5 — Augment & generate

- Gắn chunk vào prompt → LLM trả lời

**🎨 Visual:** `[Screen]` Prompt + context → answer.
**🎤 Speaker note:** LLM trả lời dựa trên tài liệu thật.

### Slide 6 — Tóm tắt & chuyển bài

- ingest · embed · retrieve · generate
- Bài tiếp: hybrid search →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta nâng cấp phần tìm kiếm."

---

_← [Về Section README](../README.md)_
