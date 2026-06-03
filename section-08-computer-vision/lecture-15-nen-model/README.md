# Section 8 · Lecture 15 — Nén model

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 15
- LECTURE 15 · ~7 PHÚT · 5 SLIDES
- Nén model
- Quantization & pruning — nhỏ hơn, nhanh hơn, ít tốn điện hơn

### Slide 2

- L15 · QUANTIZATION
- Giảm độ chính xác số — nhỏ & nhanh hơn nhiều
- float32
- 32 bit / số · nặng
- →
- int8
- 8 bit / số · gọn
- Nhỏ hơn ~4×, nhanh hơn — mà mất rất ít độ chính xác.

### Slide 3

- L15 · PRUNING
- Cắt bỏ phần "thừa" của mạng
- Loại trọng số / nơ-ron ít quan trọng
- Mạng thưa hơn, nhẹ hơn
- →
- Mạng đầy đủ → mạng đã tỉa thưa

### Slide 4

- L15 · TRADE-OFF
- Luôn đo lại accuracy sau khi nén
- Tốc độ ↑ · Kích thước ↓
- lợi ích khi nén
- ⇄
- Độ chính xác có thể ↓
- cái giá phải cân
- Nén tới đâu là đủ? Đo accuracy để tìm điểm cân bằng.

### Slide 5

- L15 · TÓM TẮT
- Làm model gọn nhẹ:
- quantization
- pruning
- trade-off
- BÀI TIẾP
- →
- Capstone 3 — ráp tất cả vào một dự án CV thật

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_