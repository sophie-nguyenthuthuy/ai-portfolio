# Section 5 · Lecture 20 — 🏆 Capstone 1 — Dự đoán khách hàng rời bỏ (churn) full pipeline

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 8 · ~16 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 🏆 Capstone 1: Churn Prediction

**🎨 Visual:** `[AI image]` Dashboard giữ chân khách hàng.
**🎤 Speaker note:** "Dự án portfolio đầu tiên — ráp toàn bộ Section 5."

### Slide 2 — Bài toán kinh doanh

- Dự đoán khách sắp rời bỏ
- Vì sao quan trọng: giữ rẻ hơn tìm mới

**🎨 Visual:** `[Mermaid]` Chi phí giữ vs tìm khách.
**🎤 Speaker note:** Đóng khung giá trị kinh doanh trước.

### Slide 3 — EDA & làm sạch

- Khám phá dữ liệu, xử lý missing
- Phát hiện mất cân bằng lớp

**🎨 Visual:** `[Screen]` EDA churn dataset.
**🎤 Speaker note:** Áp dụng EDA Section 4.

### Slide 4 — Feature engineering

- Encoding, scaling, tạo feature

**🎨 Visual:** `[Screen]` Pipeline feature.
**🎤 Speaker note:** Cẩn thận tránh data leakage.

### Slide 5 — Xây & so sánh model

- Logistic, Random Forest, XGBoost
- So sánh hiệu năng

**🎨 Visual:** `[Screen]` Bảng so sánh model.
**🎤 Speaker note:** Không có model "đúng" — chọn theo metric.

### Slide 6 — Xử lý imbalance & tuning

- SMOTE / class weight
- Optuna tinh chỉnh

**🎨 Visual:** `[Screen]` Tuning với Optuna.
**🎤 Speaker note:** Tập trung Recall/F1, không chỉ Accuracy.

### Slide 7 — Diễn giải & đề xuất

- Feature quan trọng nhất
- Đề xuất hành động giữ khách

**🎨 Visual:** `[Screen]` Feature importance + insight.
**🎤 Speaker note:** Storytelling: từ model ra quyết định kinh doanh.

### Slide 8 — Tổng kết Section 5

- ML Fundamentals + Capstone 1 ✅
- Bài tiếp: Section 6 — Time Series →

**🎨 Visual:** `[AI image]` Badge "Project 1/7 Done".
**🎤 Speaker note:** "Bạn có dự án portfolio đầu tiên! Tiếp tục với dữ liệu thời gian."

---

_← [Về Section README](../README.md)_
