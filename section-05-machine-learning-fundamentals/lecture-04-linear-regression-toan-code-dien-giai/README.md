# Section 5 · Lecture 4 — Linear Regression — toán, code, diễn giải

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Linear Regression — model đầu tiên

**🎨 Visual:** `[AI image]` Đường thẳng qua đám điểm.
**🎤 Speaker note:** "Đơn giản nhưng dạy mọi nguyên lý ML."

### Slide 2 — Bài toán hồi quy

- Dự đoán giá trị liên tục
- Vd: giá nhà, doanh thu

**🎨 Visual:** `[Mermaid]` Input → số thực.
**🎤 Speaker note:** Khác phân lớp (dự đoán nhãn).

### Slide 3 — Mô hình tuyến tính

- y = w·x + b
- Tìm đường khớp dữ liệu nhất

**🎨 Visual:** `[Mermaid]` Công thức + đường hồi quy.
**🎤 Speaker note:** w = trọng số, b = bias.

### Slide 4 — Hàm mất mát MSE

- Đo sai số bình phương trung bình
- Mục tiêu: cực tiểu MSE

**🎨 Visual:** `[Mermaid]` Khoảng cách điểm tới đường.
**🎤 Speaker note:** Nối lại gradient descent đã học.

### Slide 5 — Huấn luyện bằng Gradient Descent

- Cập nhật w, b theo gradient

**🎨 Visual:** `[Screen]` Train + vẽ đường khớp dần.
**🎤 Speaker note:** Đây là lúc lý thuyết toán "sống dậy".

### Slide 6 — Code & diễn giải

- sklearn LinearRegression
- Đọc hệ số: ý nghĩa từng feature

**🎨 Visual:** `[Screen]` fit + in coefficients.
**🎤 Speaker note:** Diễn giải hệ số cho stakeholder.

### Slide 7 — Tóm tắt & chuyển bài

- mô hình · MSE · train · diễn giải
- Bài tiếp: Logistic Regression →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta chuyển từ dự đoán số sang phân loại."

---

_← [Về Section README](../README.md)_
