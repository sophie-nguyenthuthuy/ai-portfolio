# Section 11 · Lecture 12 — Tối ưu chi phí — caching, batching, distillation, quantization

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tối ưu chi phí LLM

**🎨 Visual:** `[AI image]` Đồng hồ chi phí token.
**🎤 Speaker note:** "LLM rất tốn tiền — tối ưu là kỹ năng quý."

### Slide 2 — Caching

- Lưu kết quả truy vấn lặp lại
- Tiết kiệm token & độ trễ

**🎨 Visual:** `[Mermaid]` Cache hit/miss.
**🎤 Speaker note:** Giảm chi phí đáng kể với câu hỏi trùng.

### Slide 3 — Batching

- Gộp nhiều request
- Tăng throughput

**🎨 Visual:** `[Mermaid]` Batch requests.
**🎤 Speaker note:** Hiệu quả khi tải lớn.

### Slide 4 — Distillation & quantization

- Distillation: model nhỏ học model lớn
- Quantization: giảm độ chính xác số

**🎨 Visual:** `[Mermaid]` Model lớn → nhỏ.
**🎤 Speaker note:** Nối lại quantization Section 8.

### Slide 5 — Tóm tắt & chuyển bài

- caching · batching · distillation · quantization
- Bài tiếp: an toàn LLM →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta bảo vệ LLM khỏi tấn công."

---

_← [Về Section README](../README.md)_
