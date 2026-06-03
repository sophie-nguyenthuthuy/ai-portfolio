# Section 8 · Lecture 1 — Ảnh đối với máy tính là gì?

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 01
- LECTURE 01 · ~7 PHÚT · 5 SLIDES
- Ảnh đối với máy tính là gì?
- Pixel · channel · tensor — máy "nhìn" ảnh thế nào

### Slide 2

- L01 · PIXEL & ĐỘ PHÂN GIẢI
- Với máy, ảnh chỉ là một lưới các con số
- Ảnh = lưới điểm ảnh (pixel)
- Độ phân giải = số pixel theo chiều rộng × cao
- Mỗi pixel mang giá trị
- 0 – 255
- 0 = đen tuyệt đối, 255 = trắng tuyệt đối
- 76
- 122
- 180
- 228
- 250
- 40
- 96
- 150
- 210
- 242
- 12
- 72
- 128
- 190
- 232
- 0
- 48
- 110
- 172
- 222
- 24
- 84
- 140
- 200
- 255
- Vùng zoom 5×5 px — mỗi ô là một con số cường độ sáng

### Slide 3

- L01 · CHANNEL MÀU
- Ảnh xám có 1 channel , ảnh màu có 3
- R
- đỏ · 0-255
- +
- G
- lục · 0-255
- +
- B
- lam · 0-255
- →
- RGB
- ảnh màu hoàn chỉnh
- Ba channel chồng lên nhau tạo ra mọi màu — ảnh xám chỉ giữ lại độ sáng.

### Slide 4

- L01 · ẢNH = TENSOR
- Gộp tất cả lại: ảnh là một tensor 3 chiều
- H × W
- shape = ( Height × Width × Channel )
- Nối lại khái niệm tensor — Section 4
- PyTorch quy ước thứ tự (C × H × W)

### Slide 5

- L01 · TÓM TẮT
- Ảnh = số. Ba khái niệm cần nhớ:
- pixel
- channel
- tensor
- BÀI TIẾP
- →
- Tiền xử lý ảnh — chuẩn bị ảnh trước khi đưa vào model

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_