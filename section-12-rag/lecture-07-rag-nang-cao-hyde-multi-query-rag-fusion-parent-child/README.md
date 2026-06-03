# Section 12 · Lecture 7 — RAG nâng cao — HyDE, multi-query, RAG-Fusion, parent-child

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Advanced RAG

**🎨 Visual:** `[AI image]` Pipeline RAG phức tạp hơn.
**🎤 Speaker note:** "Khi RAG cơ bản chưa đủ tốt."

### Slide 2 — HyDE

- Sinh câu trả lời giả → embed → tìm

**🎨 Visual:** `[Mermaid]` HyDE flow.
**🎤 Speaker note:** Câu trả lời giả gần tài liệu hơn câu hỏi.

### Slide 3 — Multi-query

- Sinh nhiều biến thể câu hỏi
- Tìm rộng hơn

**🎨 Visual:** `[Mermaid]` 1 query → nhiều query.
**🎤 Speaker note:** Bắt được nhiều cách diễn đạt.

### Slide 4 — RAG-Fusion

- Gộp kết quả nhiều query
- Xếp hạng lại

**🎨 Visual:** `[Mermaid]` Fusion ranking.
**🎤 Speaker note:** Kết hợp multi-query + rerank.

### Slide 5 — Parent-child

- Tìm chunk nhỏ, trả về đoạn lớn

**🎨 Visual:** `[Mermaid]` Child match → parent context.
**🎤 Speaker note:** Vừa tìm chính xác, vừa đủ ngữ cảnh.

### Slide 6 — Tóm tắt & chuyển bài

- HyDE · multi-query · fusion · parent-child
- Bài tiếp: multi-hop & graph RAG →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới RAG cho câu hỏi phức tạp."

---

_← [Về Section README](../README.md)_
