# Section 6 · Lecture 3 — Làm mượt & dự báo cơ bản

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 03
- SECTION 6 · LECTURE 3
- Làm mượt & dự báo cơ bản
- ~8 phút · 6 slides

### Slide 2

- MOVING AVERAGE
- Trung bình trượt làm mượt nhiễu
- rolling.py
- df["ma7"]  = df["sales"].rolling(7 ).mean()
- df[
- "ma30"] = df["sales"].rolling(30).mean() # cua so cang lon  ->  cang muot
- Trung bình cửa sổ trượt
- Làm mượt nhiễu, lộ rõ xu hướng
- Nối lại rolling() đã học ở Section 2

### Slide 3

- EXPONENTIAL SMOOTHING
- Trọng số giảm dần về quá khứ
- Trọng số mũ giảm dần theo độ trễ
- Quan sát gần đây quan trọng hơn
- Phản ứng nhanh với thay đổi mới

### Slide 4

- HOLT
- Holt — thêm thành phần xu hướng
- Mở rộng cho chuỗi có trend
- Dự báo nối tiếp theo độ dốc hiện tại

### Slide 5

- HOLT-WINTERS
- Thêm cả mùa vụ (seasonality)
- holtwinters.py
- from statsmodels.tsa.holtwinters import  ExponentialSmoothing
- model = ExponentialSmoothing(
- sales, trend=
- "add", seasonal="add" ,
- seasonal_periods=
- 12 ).fit()
- forecast = model.forecast(
- 12)
- Bộ ba: level + trend + seasonal
- Mạnh cho dữ liệu mùa vụ rõ rệt

### Slide 6

- SECTION 6 · LECTURE 3
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- moving average
- exponential smoothing
- Holt-Winters
- BÀI TIẾP THEO
- →
- ACF / PACF — chọn bậc cho ARIMA

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_