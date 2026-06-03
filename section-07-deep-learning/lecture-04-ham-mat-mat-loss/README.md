# Section 7 · Lecture 4 — Hàm mất mát — Loss

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 7 · LECTURE 4
- Hàm mất mát — Loss
- ~7 phút · 5 slides

### Slide 2

- REGRESSION
- MSE cho bài toán hồi quy
- Sai số bình phương trung bình
- Phạt theo bình phương khoảng cách dự đoán – thực tế
- Nối lại Linear Regression

### Slide 3

- CLASSIFICATION
- Cross-Entropy cho phân loại
- Phạt nặng dự đoán sai mà tự tin
- Đi kèm softmax / sigmoid ở output

### Slide 4

- CUSTOM
- Custom loss — tự thiết kế
- custom_loss.py
- def  weighted_mse(y, yhat, w):
- return np.mean(w * (y - yhat) ** 2) # w: trong so cho tung mau / tung lop
- Khi bài toán đặc thù cần một loss riêng theo nghiệp vụ.

### Slide 5

- SECTION 7 · LECTURE 4
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- MSE
- cross-entropy
- custom loss
- BÀI TIẾP THEO
- →
- Backpropagation

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_