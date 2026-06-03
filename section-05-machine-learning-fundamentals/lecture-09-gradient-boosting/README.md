# Section 5 · Lecture 9 — Gradient Boosting

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE 09 · ~10 PHÚT
- 09
- Gradient Boosting
- XGBoost · LightGBM · CatBoost

### Slide 2

- L09 · BOOSTING VS BAGGING
- Song song vs tuần tự sửa lỗi
- BAGGING
- Song song · độc lập
- Các cây được train riêng rẽ rồi gộp lại — giảm phương sai.
- vs
- BOOSTING
- Tuần tự · sửa lỗi
- Mỗi cây mới học từ sai lầm của các cây trước — giảm độ lệch (bias).

### Slide 3

- L09 · Ý TƯỞNG CỐT LÕI
- Mỗi cây mới sửa phần lỗi còn lại (residual)
- Cây 1
- dự đoán thô
- →
- Cây 2
- sửa lỗi cây 1
- →
- Cây 3
- sửa lỗi còn lại
- →
- Tổng dồn
- mô hình mạnh
- Cộng dồn nhiều cây "yếu" → một mô hình rất mạnh. Residual giảm dần qua từng cây.

### Slide 4

- L09 · XGBOOST
- Chuẩn ngành cho dữ liệu bảng
- xgboost_train.py
- from xgboost import  XGBClassifier
- model =
- XGBClassifier (
- n_estimators=
- 300 ,
- learning_rate=
- 0.05 ,
- max_depth=
- 5 ,
- )
- model.
- fit(X_train, y_train)
- Nhanh, mạnh, có
- regularization
- Chống overfit tốt hơn cây thường
- Lựa chọn an toàn cho dữ liệu bảng
- Là chuẩn ngành trong nhiều năm

### Slide 5

- L09 · LIGHTGBM & CATBOOST
- Khi nào dùng cái nào?
- LIGHTGBM
- Rất nhanh
- Tối ưu cho dữ liệu lớn — huấn luyện nhanh, tốn ít bộ nhớ.
- ·
- CATBOOST
- Giỏi categorical
- Xử lý biến phân loại rất tốt — ít cần encode bằng tay.

### Slide 6

- L09 · THAM SỐ QUAN TRỌNG
- Ba "núm vặn" chính
- LEARNING_RATE
- Tốc độ học
- Nhỏ → học chậm nhưng chắc, thường cần nhiều cây hơn.
- N_ESTIMATORS
- Số cây
- Nhiều cây mạnh hơn nhưng tốn thời gian & dễ overfit.
- MAX_DEPTH
- Độ sâu cây
- Kiểm soát độ phức tạp của từng cây thành phần.
- GHI CHÚ
- Sẽ tinh chỉnh kỹ ba tham số này ở bài Hyperparameter Tuning.

### Slide 7

- L09 · TÓM TẮT
- Gradient Boosting
- 01
- Boosting
- Tuần tự, mỗi cây sửa lỗi cây trước
- 02
- Ba thư viện
- XGBoost · LightGBM · CatBoost
- 03
- Tham số
- learning_rate · n_estimators · max_depth
- BÀI TIẾP
- SVM — tìm ranh giới phân lớp tối ưu
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_