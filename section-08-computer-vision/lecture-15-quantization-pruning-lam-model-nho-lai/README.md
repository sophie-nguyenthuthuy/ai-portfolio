# Section 8 · Lecture 15 — Quantization & pruning — làm model nhỏ lại

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Nén model

**🎨 Visual:** `[AI image]` Model lớn → model nhỏ gọn.
**🎤 Speaker note:** "Nhỏ hơn, nhanh hơn, ít tốn điện hơn."

### Slide 2 — Quantization

- Giảm độ chính xác số (float32 → int8)
- Nhỏ & nhanh hơn nhiều

**🎨 Visual:** `[Mermaid]` float32 → int8.
**🎤 Speaker note:** Mất rất ít độ chính xác.

### Slide 3 — Pruning

- Cắt bỏ trọng số/nơ-ron ít quan trọng

**🎨 Visual:** `[Mermaid]` Mạng bị tỉa thưa.
**🎤 Speaker note:** Loại bỏ phần "thừa" của mạng.

### Slide 4 — Trade-off

- Tốc độ/kích thước vs độ chính xác

**🎨 Visual:** `[Mermaid]` Cân bằng nén vs accuracy.
**🎤 Speaker note:** Đo lại accuracy sau khi nén.

### Slide 5 — Tóm tắt & chuyển bài

- quantization · pruning · trade-off
- Bài tiếp: Capstone 3 →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả vào dự án CV thật."

---

_← [Về Section README](../README.md)_
