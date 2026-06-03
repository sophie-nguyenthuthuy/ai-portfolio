# Section 7 · Lecture 7 — Regularization — chống overfitting

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 07
- SECTION 7 · LECTURE 7
- Regularization — chống overfitting
- ~8 phút · 6 slides

### Slide 2

- DROPOUT
- Tắt ngẫu nhiên nơ-ron
- Tắt ngẫu nhiên nơ-ron khi train
- Mạng không phụ thuộc một đường duy nhất
- Đơn giản mà rất hiệu quả

### Slide 3

- BATCHNORM
- Chuẩn hoá giữa các lớp
- Layer
- →
- BatchNorm
- →
- Activation
- →
- Layer
- Chuẩn hoá đầu ra giữa các lớp → train ổn định và nhanh hơn. Gần như mặc định trong CNN.

### Slide 4

- WEIGHT DECAY
- Weight decay (L2)
- Phạt các trọng số lớn
- Giữ mô hình đơn giản hơn
- Nối lại norm L2 ở Section 4

### Slide 5

- EARLY STOPPING
- Dừng đúng lúc
- Dừng khi validation loss bắt đầu tăng
- Đơn giản, hiệu quả và miễn phí

### Slide 6

- SECTION 7 · LECTURE 7
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- dropout
- batchnorm
- weight decay
- early stopping
- BÀI TIẾP THEO
- →
- PyTorch cấp tốc

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_