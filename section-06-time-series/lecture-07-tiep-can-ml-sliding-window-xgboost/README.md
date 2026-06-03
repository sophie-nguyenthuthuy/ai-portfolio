# Section 6 · Lecture 7 — Tiếp cận ML — sliding window + XGBoost

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Time-series như bài toán ML

**🎨 Visual:** `[AI image]` Cửa sổ trượt trên chuỗi.
**🎤 Speaker note:** "Dùng lại XGBoost đã học cho dự báo."

### Slide 2 — Sliding window

- Dùng quá khứ làm feature dự đoán tương lai

**🎨 Visual:** `[Mermaid]` Cửa sổ trượt tạo mẫu.
**🎤 Speaker note:** Bước chuẩn bị quan trọng (cả cho LSTM sau).

### Slide 3 — Feature từ thời gian

- lag, rolling mean, ngày/tháng/thứ

**🎨 Visual:** `[Screen]` Tạo lag features.
**🎤 Speaker note:** Nối lại feature thời gian Section 2.

### Slide 4 — Train XGBoost

- Đưa feature vào XGBoost
- So với ARIMA

**🎨 Visual:** `[Screen]` XGBoost dự báo.
**🎤 Speaker note:** Bắt được quan hệ phi tuyến tốt hơn ARIMA.

### Slide 5 — Backtesting

- TimeSeriesSplit (không xáo trộn)
- Vì sao split ngẫu nhiên là SAI

**🎨 Visual:** `[Mermaid]` TimeSeriesSplit.
**🎤 Speaker note:** ⚠️ Lỗi kinh điển: shuffle dữ liệu time-series.

### Slide 6 — Tóm tắt & chuyển bài

- sliding window · lag features · backtesting
- Bài tiếp: LSTM & GRU →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta dùng deep learning cho chuỗi dài."

---

_← [Về Section README](../README.md)_
