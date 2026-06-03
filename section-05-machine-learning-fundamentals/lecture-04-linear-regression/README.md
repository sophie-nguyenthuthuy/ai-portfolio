# Section 5 · Lecture 4 — Linear Regression

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE 04 · ~10 PHÚT
- 04
- Linear Regression
- toán · code · diễn giải — model đầu tiên

### Slide 2

- L04 · BÀI TOÁN HỒI QUY
- Dự đoán một giá trị liên tục
- Đầu ra là số thực, không phải nhãn
- Ví dụ: giá nhà, doanh thu, nhiệt độ
- Khác với phân lớp (dự đoán nhãn rời rạc)
- Hồi quy → số · Phân lớp → loại
- Input
- diện tích, vị trí…
- ↓
- Số thực
- vd: 4.2 tỉ đồng

### Slide 3

- L04 · MÔ HÌNH TUYẾN TÍNH
- Tìm đường thẳng khớp dữ liệu nhất
- y =
- w
- ·x +
- b
- w = trọng số (slope) · b = bias (intercept)
- Huấn luyện = tìm cặp w, b sao cho đường đi qua đám điểm "khít" nhất.

### Slide 4

- L04 · HÀM MẤT MÁT
- MSE — sai số bình phương trung bình
- MSE =
- 1/n
- Σ (yᵢ − ŷᵢ)²
- Trung bình bình phương khoảng cách điểm → đường
- Đo tổng mức "lệch" của dự đoán so với thực tế
- Bình phương → phạt nặng lỗi lớn
- Mục tiêu huấn luyện:
- cực tiểu hoá MSE
- Nối lại gradient descent đã học ở Section 4

### Slide 5

- L04 · HUẤN LUYỆN
- Gradient Descent cập nhật w, b
- SCREEN RECORDING
- Vòng lặp train: đường hồi quy dịch dần tới vị trí khớp nhất, MSE giảm qua từng bước
- Mỗi bước, w & b dịch ngược hướng gradient
- Đi xuống "dốc" của hàm mất mát
- Lặp tới khi MSE gần như không giảm nữa
- Lý thuyết toán "sống dậy" thành đường khớp

### Slide 6

- L04 · CODE & DIỄN GIẢI
- sklearn LinearRegression
- linear_regression.py
- from sklearn.linear_model import  LinearRegression
- model =
- LinearRegression ()
- model.
- fit(X_train, y_train)         # học w, b # diễn giải hệ số cho stakeholder print(model.coef_)                 # w — ảnh hưởng từng feature print(model.intercept_)            # b — giá trị nền y_pred = model.predict(X_test)
- Hệ số dương/âm & độ lớn cho biết mỗi feature kéo dự đoán lên hay xuống — rất dễ diễn giải.

### Slide 7

- L04 · TÓM TẮT
- Linear Regression từ đầu đến cuối
- 01
- Mô hình
- y = w·x + b
- 02
- MSE
- Hàm mất mát cần cực tiểu
- 03
- Train + diễn giải
- Gradient descent & đọc hệ số
- BÀI TIẾP
- Logistic Regression — từ dự đoán số sang phân loại
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_