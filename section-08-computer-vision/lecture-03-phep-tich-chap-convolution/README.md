# Section 8 · Lecture 3 — Phép tích chập (convolution)

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 03
- LECTURE 03 · ~9 PHÚT · 6 SLIDES
- Phép tích chập (convolution)
- kernel · stride · padding · receptive field — phép toán làm nên cuộc cách mạng CV

### Slide 2

- L03 · KERNEL / FILTER
- Một cửa sổ nhỏ trượt khắp ảnh
- Phát hiện cạnh, góc, texture
- Mỗi kernel học một loại đặc trưng riêng
- Nhiều kernel → nhiều loại đặc trưng được trích
- →
- ∑
- Kernel 3×3 nhân từng vùng → một giá trị đặc trưng

### Slide 3

- L03 · STRIDE & PADDING
- Hai nút điều khiển kích thước output
- STRIDE
- Bước nhảy của kernel
- Stride 1: trượt từng pixel
- Stride lớn → output nhỏ hơn
- PADDING
- Viền số 0 quanh ảnh
- Giữ nguyên kích thước sau conv
- Bảo toàn thông tin ở rìa ảnh

### Slide 4

- L03 · TÍNH KÍCH THƯỚC OUTPUT
- Công thức từ input, kernel, stride, padding
- output = ⌊ ( W − K + 2P ) / S ⌋ + 1
- ⚠️ Ví dụ hay hỏi: input 224, conv 3×3, stride 1, pad 1 → 224

### Slide 5

- L03 · RECEPTIVE FIELD
- Lớp càng sâu, một nơ-ron nhìn càng rộng
- Lớp đầu
- nhìn thấy: cạnh, góc
- →
- Lớp giữa
- nhìn thấy: hoa văn, bộ phận
- →
- Lớp sâu
- nhìn thấy: cả vật thể
- Receptive field = vùng ảnh gốc mà một nơ-ron tổng hợp được — mở rộng dần theo độ sâu.

### Slide 6

- L03 · TÓM TẮT
- Bộ máy của convolution:
- kernel
- stride / padding
- receptive field
- BÀI TIẾP
- →
- Ráp convolution thành một mạng CNN hoàn chỉnh

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_