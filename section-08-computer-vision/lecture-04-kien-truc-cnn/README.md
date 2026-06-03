# Section 8 · Lecture 4 — Kiến trúc CNN

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 04
- LECTURE 04 · ~8 PHÚT · 6 SLIDES
- Kiến trúc CNN
- Conv · Pool · FC — cách các thành phần ghép thành mạng hoàn chỉnh

### Slide 2

- L04 · LỚP CONVOLUTION
- Trích đặc trưng, tạo ra nhiều feature map
- Mỗi filter quét ảnh → một feature map
- Nhiều filter → nhiều feature map song song
- ảnh
- →
- maps

### Slide 3

- L04 · POOLING
- Thu nhỏ feature map, giữ phần quan trọng
- Max pool / Average pool
- Giảm tính toán + chống overfit nhẹ
- 1
- 5
- 2
- 3
- 8
- 4
- 6
- 1
- 3
- 2
- 9
- 7
- 1
- 4
- 5
- 2
- →
- max 2×2
- 8
- 6
- 4
- 9

### Slide 4

- L04 · FULLY CONNECTED
- Làm phẳng → lớp dày → ra quyết định
- Feature maps
- →
- Flatten
- thành vector 1 chiều
- →
- FC layers
- →
- Softmax
- xác suất từng lớp

### Slide 5

- L04 · TOÀN CẢNH CNN
- Conv–Pool lặp lại → FC → nhãn
- ảnh
- →
- [ Conv → Pool ] × N
- trích đặc trưng
- →
- Flatten → FC
- →
- Nhãn 🐱
- Hai nửa: trích đặc trưng (Conv/Pool) → phân loại (FC).

### Slide 6

- L04 · TÓM TẮT
- Ba khối xây nên mọi CNN:
- Conv
- Pool
- FC
- BÀI TIẾP
- →
- Các kiến trúc CNN nổi tiếng làm nên lịch sử

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_