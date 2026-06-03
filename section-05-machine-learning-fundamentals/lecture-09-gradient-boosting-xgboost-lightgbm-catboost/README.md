# Section 5 · Lecture 9 — Gradient Boosting — XGBoost, LightGBM, CatBoost

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Gradient Boosting

**🎨 Visual:** `[AI image]` Các cây nối tiếp sửa lỗi.
**🎤 Speaker note:** "Vô địch Kaggle cho dữ liệu bảng (tabular)."

### Slide 2 — Boosting vs Bagging

- Bagging: song song, độc lập
- Boosting: tuần tự, sửa lỗi cây trước

**🎨 Visual:** `[Mermaid]` So sánh 2 cách.
**🎤 Speaker note:** Boosting học từ sai lầm.

### Slide 3 — Ý tưởng cốt lõi

- Mỗi cây mới sửa lỗi còn lại (residual)

**🎨 Visual:** `[Mermaid]` Residual giảm dần qua các cây.
**🎤 Speaker note:** Cộng dồn nhiều cây yếu thành mạnh.

### Slide 4 — XGBoost

- Nhanh, mạnh, có regularization
- Chuẩn ngành nhiều năm

**🎨 Visual:** `[Screen]` Train XGBoost.
**🎤 Speaker note:** Lựa chọn an toàn cho dữ liệu bảng.

### Slide 5 — LightGBM & CatBoost

- LightGBM: rất nhanh, dữ liệu lớn
- CatBoost: xử lý categorical tốt

**🎨 Visual:** `[Mermaid]` Khi nào dùng cái nào.
**🎤 Speaker note:** CatBoost ít cần encode tay.

### Slide 6 — Tham số quan trọng

- learning_rate, n_estimators, max_depth

**🎨 Visual:** `[Screen]` Ví dụ tham số.
**🎤 Speaker note:** Sẽ tinh chỉnh ở bài hyperparameter tuning.

### Slide 7 — Tóm tắt & chuyển bài

- boosting · XGBoost/LightGBM/CatBoost
- Bài tiếp: SVM →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ học model tìm ranh giới tối ưu — SVM."

---

_← [Về Section README](../README.md)_
