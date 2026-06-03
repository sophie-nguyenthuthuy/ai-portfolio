# Section 5 · Lecture 18 — Xử lý dữ liệu mất cân bằng — SMOTE, class weight

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Dữ liệu mất cân bằng

**🎨 Visual:** `[AI image]` Cán cân lệch nặng 1 bên.
**🎤 Speaker note:** "Fraud 1% — model đoán 'không fraud' vẫn 99% đúng mà vô dụng."

### Slide 2 — Vì sao là vấn đề

- Accuracy đánh lừa
- Model bỏ qua lớp hiếm

**🎨 Visual:** `[Mermaid]` 99% vs 1%.
**🎤 Speaker note:** Lớp hiếm thường là lớp ta quan tâm nhất.

### Slide 3 — Resampling

- Oversampling lớp ít / undersampling lớp nhiều
- SMOTE: sinh mẫu nhân tạo

**🎨 Visual:** `[Mermaid]` SMOTE tạo điểm mới.
**🎤 Speaker note:** SMOTE chỉ áp dụng trên train.

### Slide 4 — Class weight & metric đúng

- Phạt nặng lỗi lớp hiếm
- Dùng F1, recall thay accuracy

**🎨 Visual:** `[Mermaid]` class_weight='balanced'.
**🎤 Speaker note:** Chọn metric đúng quan trọng hơn cả.

### Slide 5 — Tóm tắt & chuyển bài

- imbalance · SMOTE · class weight
- Bài tiếp: hyperparameter tuning →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tinh chỉnh model cho tối ưu."

---

_← [Về Section README](../README.md)_
