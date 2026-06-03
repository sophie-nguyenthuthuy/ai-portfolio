# Section 7 · Lecture 5 — Backpropagation — quy tắc chuỗi

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 05
- SECTION 7 · LECTURE 5
- Backpropagation — quy tắc chuỗi
- ~9 phút · 6 slides

### Slide 2

- Ý TƯỞNG
- Tính loss rồi truyền lỗi ngược
- Tính loss → truyền lỗi ngược về các lớp
- Cập nhật trọng số
- theo gradient
- Mạng học bằng cách “đổ lỗi” ngược về nguồn
- forward →
- →
- loss
- →
- ← backward

### Slide 3

- CHAIN RULE
- Quy tắc chuỗi (chain rule)
- Đạo hàm của hàm hợp
- Nhân gradient qua từng lớp
- Nối lại đạo hàm ở Section 4
- ∂L/∂w = ∂L/∂a · ∂a/∂z · ∂z/∂w

### Slide 4

- COMPUTATIONAL GRAPH
- Biểu diễn phép tính thành đồ thị
- x
- →
- ×W
- →
- +b
- →
- f
- →
- L
- Computational graph là nền tảng của autograd trong PyTorch — tự động tính gradient.

### Slide 5

- NUMPY
- Backprop đơn giản bằng NumPy
- backprop.py
- dz2 = (a2 - y) / m
- dW2 = a1.T @ dz2
- da1 = dz2 @ W2.T
- dz1 = da1 * (z1 >
- 0)              # dao ham ReLU dW1 = x.T @ dz1
- Tự cài một lần bằng tay để hiểu sâu cơ chế học.

### Slide 6

- SECTION 7 · LECTURE 5
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- truyền lỗi ngược
- chain rule
- computational graph
- BÀI TIẾP THEO
- →
- Optimizer

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_