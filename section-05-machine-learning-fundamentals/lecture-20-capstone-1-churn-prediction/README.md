# Section 5 · Lecture 20 — Capstone 1 — Churn Prediction

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE 20 · ~16 PHÚT · 🏆 CAPSTONE
- 20
- Capstone 1 — Churn Prediction
- dự đoán khách hàng rời bỏ · full pipeline

### Slide 2

- L20 · BÀI TOÁN KINH DOANH
- Dự đoán khách sắp rời bỏ — vì giữ rẻ hơn tìm mới
- Giữ khách
- Tìm khách mới
- Phát hiện sớm khách có nguy cơ rời bỏ
- Để kịp thời có hành động giữ chân
- Đóng khung giá trị kinh doanh trước tiên
- Chi phí giữ khách thấp hơn nhiều tìm mới

### Slide 3

- L20 · BƯỚC 1–2 · EDA → FEATURE
- Khám phá, làm sạch & tạo feature
- EDA & LÀM SẠCH
- Hiểu dữ liệu
- Khám phá phân phối, xử lý missing
- Phát hiện mất cân bằng lớp
- Áp dụng EDA từ Section 4
- FEATURE ENGINEERING
- Chuẩn bị đầu vào
- Encoding, scaling, tạo feature
- Đóng gói thành pipeline
- Cẩn thận tránh data leakage

### Slide 4

- L20 · BƯỚC 3 · XÂY & SO SÁNH MODEL
- Không có model "đúng" — chọn theo metric
- MODEL
- ACCURACY
- RECALL
- F1-SCORE
- Logistic Regression
- 0.81
- 0.64
- 0.68
- Random Forest
- 0.84
- 0.71
- 0.74
- XGBoost ★
- 0.85
- 0.79
- 0.80
- Với churn, ưu tiên Recall (bắt được khách sắp rời) hơn là accuracy thô.

### Slide 5

- L20 · BƯỚC 4 · IMBALANCE & TUNING
- Cân bằng lớp rồi tinh chỉnh bằng Optuna
- SCREEN RECORDING
- Optuna chạy 100 trial — biểu đồ điểm F1 leo dần lên qua từng lần thử, tìm bộ tham số tốt nhất
- Áp dụng SMOTE / class_weight cho lớp churn hiếm
- Chỉ trên tập train
- Tinh chỉnh hyperparameter với Optuna
- Tập trung Recall / F1, không chỉ Accuracy

### Slide 6

- L20 · BƯỚC 5 · DIỄN GIẢI & ĐỀ XUẤT
- Từ model ra quyết định kinh doanh
- tenure (thâm niên)
- cao
- contract: tháng
- cao
- monthly_charges
- vừa
- tech_support: không
- vừa
- Khách hợp đồng tháng & thâm niên thấp dễ rời nhất
- Storytelling từ feature importance
- Đề xuất: ưu đãi gia hạn & chăm sóc nhóm rủi ro
- Biến insight thành hành động giữ khách

### Slide 7

- SECTION 05 · HOÀN THÀNH
- ML Fundamentals + Capstone 1 ✅
- PORTFOLIO
- Project 1 / 7
- CHURN PREDICTION · DONE
- 20 lectures
- ~119 slides
- ~170 phút
- SECTION TIẾP
- Section 6 — Time Series & dữ liệu thời gian
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_