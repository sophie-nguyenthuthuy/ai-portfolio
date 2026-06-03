# Section 9 · Lecture 11 — Chiến lược decoding — greedy, beam, top-k, top-p, temperature

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Decoding — cách sinh văn bản

**🎨 Visual:** `[AI image]` Cây các lựa chọn từ.
**🎤 Speaker note:** "Cùng model, decoding khác = văn bản khác hẳn."

### Slide 2 — Greedy search

- Luôn chọn từ xác suất cao nhất
- Đơn điệu, lặp lại

**🎨 Visual:** `[Mermaid]` Chọn từ tốt nhất mỗi bước.
**🎤 Speaker note:** Nhanh nhưng nhàm.

### Slide 3 — Beam search

- Giữ nhiều đường, chọn tổng tốt nhất

**🎨 Visual:** `[Mermaid]` Nhiều beam.
**🎤 Speaker note:** Tốt cho dịch máy.

### Slide 4 — Top-k & Top-p

- Lấy mẫu từ nhóm khả năng cao
- Top-p (nucleus) linh hoạt hơn

**🎨 Visual:** `[Mermaid]` Top-k vs top-p.
**🎤 Speaker note:** Tạo văn bản đa dạng, tự nhiên hơn.

### Slide 5 — Temperature

- Cao: sáng tạo/ngẫu nhiên
- Thấp: an toàn/xác định

**🎨 Visual:** `[Mermaid]` Temperature thấp → cao.
**🎤 Speaker note:** Núm chỉnh độ "liều" của model — gặp lại ở LLM.

### Slide 6 — Tóm tắt & chuyển bài

- greedy/beam · top-k/p · temperature
- Bài tiếp: đánh giá NLP →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta đo chất lượng văn bản sinh ra."

---

_← [Về Section README](../README.md)_
