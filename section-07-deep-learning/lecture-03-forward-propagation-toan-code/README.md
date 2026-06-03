# Section 7 · Lecture 3 — Forward propagation — toán + code

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 03
- SECTION 7 · LECTURE 3
- Forward propagation — toán + code
- ~8 phút · 5 slides

### Slide 2

- MỘT LỚP
- Một lớp tính những gì?
- 1
- z = W·x + b
- Tổ hợp tuyến tính của input
- 2
- a = f(z)
- Đưa qua hàm kích hoạt
- Nối lại phép nhân ma trận đã học ở Section 4.

### Slide 3

- XẾP CHỒNG
- Output lớp này = input lớp sau
- Cứ thế truyền tiếp cho tới lớp output → ra dự đoán.

### Slide 4

- NUMPY
- Forward pass bằng NumPy
- forward.py
- def  forward(x, W1, b1, W2, b2):
- z1 = x @ W1 + b1
- a1 = np.maximum(
- 0, z1)        # ReLU     z2 = a1 @ W2 + b2
- return softmax(z2)
- Thấy rõ: neural network về bản chất chỉ là toán ma trận.

### Slide 5

- SECTION 7 · LECTURE 3
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- z = Wx + b
- activation
- xếp lớp
- BÀI TIẾP THEO
- →
- Hàm mất mát (Loss)

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_