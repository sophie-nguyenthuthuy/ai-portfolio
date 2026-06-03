# Section 5 · Lecture 5 — Logistic Regression

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 05 · ~9 PHÚT
- 05
- Logistic Regression
- sigmoid · decision boundary · log-loss

### Slide 2

- L05 · BÀI TOÁN PHÂN LOẠI NHỊ PHÂN
- Dự đoán có / không (0 / 1)
- Đầu ra là một trong hai lớp rời rạc
- Tên có "regression" nhưng dùng để phân loại
- Cực phổ biến trong kinh doanh
- Spam · gian lận · churn (rời bỏ)
- Input
- features
- ↓
- 0 hoặc 1
- nhãn lớp

### Slide 3

- L05 · HÀM SIGMOID
- Ép mọi giá trị về khoảng [0, 1] = xác suất
- Hàm S "bóp" đầu ra của hồi quy tuyến tính
- σ(z) = 1 / (1 + e⁻ᶻ)
- Output là
- xác suất
- , không phải nhãn cứng
- Vd: 0.82 → 82% khả năng thuộc lớp 1

### Slide 4

- L05 · DECISION BOUNDARY
- Ngưỡng chia xác suất thành hai lớp
- Xác suất ≥ ngưỡng → lớp 1, ngược lại → lớp 0
- Ngưỡng mặc định thường là 0.5
- Có thể
- chỉnh ngưỡng
- theo bài toán
- Vd: y tế cần "thà báo nhầm còn hơn bỏ sót"

### Slide 5

- L05 · LOG-LOSS (CROSS-ENTROPY)
- Phạt nặng dự đoán sai mà tự tin
- Hàm mất mát cho bài toán phân loại
- Đoán sai với xác suất cao → phạt rất lớn
- Vì sao không dùng MSE cho phân loại?
- MSE tạo mặt mất mát không lồi, khó tối ưu
- TRỰC GIÁC
- "Tự tin 99% mà sai" bị phạt nặng hơn nhiều so với "lưỡng lự 55% mà sai".

### Slide 6

- L05 · TÓM TẮT
- Logistic Regression
- 01
- Sigmoid
- Biến đầu ra thành xác suất [0,1]
- 02
- Decision boundary
- Ngưỡng chia hai lớp
- 03
- Log-loss
- Phạt nặng dự đoán sai tự tin
- BÀI TIẾP
- K-Nearest Neighbors — model dựa trên "hàng xóm"
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_