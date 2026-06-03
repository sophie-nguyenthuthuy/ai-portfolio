# Section 5 · Lecture 18 — Dữ liệu mất cân bằng

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- LECTURE 18 · ~7 PHÚT
- 18
- Dữ liệu mất cân bằng
- SMOTE · class weight · metric đúng

### Slide 2

- L18 · VÌ SAO LÀ VẤN ĐỀ
- Accuracy có thể đánh lừa
- 99% · không fraud
- 1% · fraud
- Model đoán "không fraud" luôn → vẫn 99% đúng
- …nhưng hoàn toàn vô dụng
- Lớp hiếm thường là lớp ta
- quan tâm nhất
- Gian lận, bệnh hiếm, churn…

### Slide 3

- L18 · RESAMPLING
- Cân bằng lại dữ liệu train
- OVERSAMPLING
- Nhân lớp ít
- Tăng số mẫu của lớp hiếm lên.
- UNDERSAMPLING
- Giảm lớp nhiều
- Bớt mẫu của lớp đa số xuống.
- SMOTE
- Sinh mẫu nhân tạo
- Tạo điểm mới giữa các mẫu lớp hiếm. Chỉ áp dụng trên train.

### Slide 4

- L18 · CLASS WEIGHT & METRIC ĐÚNG
- Phạt nặng lỗi lớp hiếm & chọn metric đúng
- imbalanced.py
- model = RandomForestClassifier (
- class_weight=
- "balanced"   # phạt nặng lỗi lớp hiếm ) # đánh giá bằng F1 / recall, KHÔNG dùng accuracy print(classification_report(y_test, y_pred))
- class_weight='balanced'
- phạt nặng lỗi lớp hiếm
- Không cần resampling thủ công
- Dùng
- F1, recall
- thay vì accuracy
- Chọn metric đúng quan trọng hơn cả

### Slide 5

- L18 · TÓM TẮT
- Xử lý dữ liệu mất cân bằng
- 01
- Vấn đề
- Accuracy đánh lừa với lớp lệch
- 02
- SMOTE
- Resampling, sinh mẫu — chỉ trên train
- 03
- Class weight + metric
- F1 / recall thay accuracy
- BÀI TIẾP
- Hyperparameter Tuning — tinh chỉnh model
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_