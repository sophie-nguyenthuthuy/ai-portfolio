# Section 12 · Lecture 1 — Vì sao cần RAG? Giới hạn của LLM khi thiếu ngữ cảnh

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- RAG — Retrieval-Augmented Generation

**🎨 Visual:** `[AI image]` LLM + kho tài liệu.
**🎤 Speaker note:** "Cách phổ biến nhất đưa LLM vào doanh nghiệp."

### Slide 2 — Giới hạn của LLM

- Không biết dữ liệu nội bộ
- Kiến thức cũ (cutoff)
- Hay bịa (hallucination)

**🎨 Visual:** `[Mermaid]` 3 giới hạn.
**🎤 Speaker note:** Nối lại hallucination Section 11.

### Slide 3 — Ý tưởng RAG

- Tìm tài liệu liên quan
- Đưa vào prompt làm ngữ cảnh

**🎨 Visual:** `[Mermaid]` Retrieve → augment → generate.
**🎤 Speaker note:** "Mở sách ra trả lời" thay vì "nhớ mang máng".

### Slide 4 — RAG vs Fine-tuning

- RAG: kiến thức cập nhật, rẻ
- Fine-tune: phong cách, kỹ năng

**🎨 Visual:** `[Mermaid]` So sánh.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn kinh điển.

### Slide 5 — Tóm tắt & chuyển bài

- giới hạn LLM · ý tưởng RAG · vs fine-tune
- Bài tiếp: embeddings →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học công nghệ tìm tài liệu: embedding."

---

_← [Về Section README](../README.md)_
