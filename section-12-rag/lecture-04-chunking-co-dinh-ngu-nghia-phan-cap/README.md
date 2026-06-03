# Section 12 · Lecture 4 — Chunking — cố định, ngữ nghĩa, phân cấp

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Document Chunking

**🎨 Visual:** `[AI image]` Tài liệu cắt thành mảnh.
**🎤 Speaker note:** "Chunk sai = RAG hỏng. Bước bị xem nhẹ nhất."

### Slide 2 — Vì sao chunk

- Tài liệu dài quá context
- Tìm đúng đoạn liên quan

**🎨 Visual:** `[Mermaid]` Tài liệu → chunks.
**🎤 Speaker note:** Chunk = đơn vị tìm kiếm.

### Slide 3 — Cố định vs ngữ nghĩa

- Fixed: cắt theo số token
- Semantic: cắt theo nghĩa

**🎨 Visual:** `[Mermaid]` So sánh 2 cách.
**🎤 Speaker note:** Semantic giữ ngữ cảnh tốt hơn.

### Slide 4 — Overlap & phân cấp

- Chồng lấn giữ ngữ cảnh
- Parent-child chunk

**🎨 Visual:** `[Mermaid]` Chunk overlap.
**🎤 Speaker note:** Overlap tránh cắt đứt ý giữa chừng.

### Slide 5 — Tóm tắt & chuyển bài

- fixed/semantic · overlap · phân cấp
- Bài tiếp: pipeline RAG cơ bản →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp thành pipeline RAG hoàn chỉnh."

---

_← [Về Section README](../README.md)_
