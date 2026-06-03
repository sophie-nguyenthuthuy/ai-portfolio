# Section 5 · Lecture 5 — Logistic Regression — sigmoid, decision boundary, log-loss

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Logistic Regression — phân loại

**🎨 Visual:** `[AI image]` Đường cong sigmoid.
**🎤 Speaker note:** "Tên có 'regression' nhưng dùng để phân loại."

### Slide 2 — Bài toán phân loại nhị phân

- Dự đoán có/không (0/1)
- Vd: spam, gian lận, churn

**🎨 Visual:** `[Mermaid]` Input → 0 hoặc 1.
**🎤 Speaker note:** Cực phổ biến trong kinh doanh.

### Slide 3 — Hàm sigmoid

- Ép giá trị về [0,1] = xác suất

**🎨 Visual:** `[Mermaid]` Đường sigmoid.
**🎤 Speaker note:** Output là xác suất, không phải nhãn cứng.

### Slide 4 — Decision boundary

- Ngưỡng (vd 0.5) chia 2 lớp

**🎨 Visual:** `[Mermaid]` Ranh giới phân lớp.
**🎤 Speaker note:** Có thể chỉnh ngưỡng theo bài toán.

### Slide 5 — Log-loss (cross-entropy)

- Phạt nặng dự đoán sai tự tin

**🎨 Visual:** `[Mermaid]` Đường log-loss.
**🎤 Speaker note:** Vì sao không dùng MSE cho phân loại.

### Slide 6 — Tóm tắt & chuyển bài

- sigmoid · boundary · log-loss
- Bài tiếp: KNN →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học model dựa trên 'hàng xóm'."

---

_← [Về Section README](../README.md)_
