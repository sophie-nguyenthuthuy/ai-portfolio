# Section 7 · Lecture 2 — Hàm kích hoạt — Activation

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 02
- SECTION 7 · LECTURE 2
- Hàm kích hoạt — Activation
- ~8 phút · 6 slides

### Slide 2

- PHI TUYẾN
- Vì sao cần phi tuyến?
- Xếp chồng tuyến tính vẫn chỉ là tuyến tính
- Phi tuyến
- mở khoá sức mạnh
- của mạng
- Đây chính là lý do tồn tại của activation

### Slide 3

- SIGMOID / TANH
- Sigmoid & Tanh
- Sigmoid: nén về khoảng [0, 1]
- Tanh: nén về khoảng [−1, 1]
- Dễ vanishing gradient — ít dùng ở lớp ẩn

### Slide 4

- RELU
- ReLU & các biến thể
- ReLU: đơn giản, hiệu quả, ít vanishing
- Biến thể: Leaky ReLU, GELU
- ReLU là mặc định cho lớp ẩn

### Slide 5

- SOFTMAX
- Softmax cho lớp output
- Dùng ở lớp output phân loại nhiều lớp
- Biến điểm số thành xác suất, tổng = 1
- Không dùng ở lớp ẩn

### Slide 6

- SECTION 7 · LECTURE 2
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- ReLU
- Sigmoid / Tanh
- GELU
- Softmax
- BÀI TIẾP THEO
- →
- Forward propagation

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_