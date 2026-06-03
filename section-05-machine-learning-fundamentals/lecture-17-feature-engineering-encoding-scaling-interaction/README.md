# Section 5 · Lecture 17 — Feature engineering — encoding, scaling, interaction

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Feature Engineering

**🎨 Visual:** `[AI image]` Dữ liệu thô → feature tinh.
**🎤 Speaker note:** "Feature tốt quan trọng hơn thuật toán xịn."

### Slide 2 — Encoding categorical

- One-hot, label, target encoding

**🎨 Visual:** `[Mermaid]` Chữ → số.
**🎤 Speaker note:** Model chỉ hiểu số.

### Slide 3 — Scaling

- StandardScaler, MinMaxScaler
- Vì sao cần (KNN, SVM, NN)

**🎨 Visual:** `[Mermaid]` Trước/sau scale.
**🎤 Speaker note:** Fit trên train, transform test (tránh leakage).

### Slide 4 — Tạo feature mới

- Kết hợp, biến đổi feature
- Feature thời gian, tỉ lệ

**🎨 Visual:** `[Screen]` Tạo feature tương tác.
**🎤 Speaker note:** Đây là nơi kiến thức nghiệp vụ toả sáng.

### Slide 5 — Feature selection

- Bỏ feature thừa/nhiễu
- Importance, correlation

**🎨 Visual:** `[Mermaid]` Chọn feature tốt.
**🎤 Speaker note:** Ít feature tốt hơn nhiều feature rác.

### Slide 6 — Tóm tắt & chuyển bài

- encoding · scaling · tạo/chọn feature
- Bài tiếp: dữ liệu mất cân bằng →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xử lý dữ liệu lệch lớp."

---

_← [Về Section README](../README.md)_
