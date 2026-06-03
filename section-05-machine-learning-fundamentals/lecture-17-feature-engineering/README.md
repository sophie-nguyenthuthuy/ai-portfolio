# Section 5 · Lecture 17 — Feature Engineering

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 17 · ~9 PHÚT
- 17
- Feature Engineering
- encoding · scaling · interaction

### Slide 2

- L17 · VÌ SAO QUAN TRỌNG
- Feature tốt quan trọng hơn thuật toán xịn
- Dữ liệu thô
- ↓
- Feature engineering
- ↓
- Feature tinh — model học tốt hơn
- TRỰC GIÁC
- Một model trung bình + feature xuất sắc thường thắng một model xịn + feature kém.

### Slide 3

- L17 · ENCODING CATEGORICAL
- Biến chữ thành số — vì model chỉ hiểu số
- ONE-HOT
- Cột nhị phân
- Mỗi giá trị thành một cột 0/1. Hợp với ít hạng mục.
- LABEL
- Gán số thứ tự
- Mỗi hạng mục một số. Hợp với biến có thứ tự.
- TARGET
- Theo mục tiêu
- Mã hoá theo giá trị target trung bình. Mạnh nhưng dễ leakage.

### Slide 4

- L17 · SCALING
- Đưa các feature về cùng thang đo
- StandardScaler
- (z-score) &
- MinMaxScaler
- [0,1]
- Cần cho KNN, SVM, Neural Network
- Không scale → feature trị lớn lấn át
- Vd: lương (triệu) lấn át tuổi (chục)
- QUY TẮC VÀNG
- Fit scaler trên tập train , rồi transform tập test — tránh data leakage.

### Slide 5

- L17 · TẠO & CHỌN FEATURE
- Nơi kiến thức nghiệp vụ toả sáng
- Tạo feature mới
- Kết hợp / biến đổi feature sẵn có
- Feature thời gian, tỉ lệ, tương tác
- Chọn lọc feature
- Bỏ feature thừa & nhiễu
- Dựa importance & correlation
- Ít feature tốt > nhiều feature rác

### Slide 6

- L17 · TÓM TẮT
- Feature Engineering
- 01
- Encoding
- One-hot · label · target
- 02
- Scaling
- Cùng thang đo, fit trên train
- 03
- Tạo & chọn
- Feature mới & loại feature rác
- BÀI TIẾP
- Dữ liệu mất cân bằng — xử lý lớp lệch
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_