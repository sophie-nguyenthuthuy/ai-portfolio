# Section 6 · Lecture 5 — ARIMA & SARIMA end-to-end

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- 05
- SECTION 6 · LECTURE 5
- ARIMA & SARIMA end-to-end
- ~10 phút · 7 slides

### Slide 2

- BA THÀNH PHẦN
- AR · I · MA
- AR
- Auto-Regressive
- Phụ thuộc các giá trị quá khứ
- I
- Integrated
- Sai phân để đạt tính dừng
- MA
- Moving Average
- Phụ thuộc các nhiễu quá khứ
- Ghép ba ý đã học ở các bài trước thành một mô hình thống kê hoàn chỉnh.

### Slide 3

- THAM SỐ
- ARIMA(p, d, q)
- p
- AR order
- Chọn từ PACF
- d
- Differencing
- Số lần sai phân
- q
- MA order
- Chọn từ ACF

### Slide 4

- QUY TRÌNH
- Quy trình ARIMA chuẩn
- Kiểm tra tính dừng (ADF)
- ↓
- Sai phân đến khi dừng → xác định d
- ↓
- Đọc ACF / PACF → chọn p, q
- ↓
- Fit mô hình & kiểm định residual
- ↓
- Dự báo
- Làm theo từng bước, không nhảy cóc.

### Slide 5

- SEASONALITY
- SARIMA — mở rộng cho mùa vụ
- sarima.py
- from statsmodels.tsa.statespace.sarimax import  SARIMAX
- model = SARIMAX(sales, order=(
- 1, 1, 1 ),
- seasonal_order=(
- 1, 1, 1, 12 )).fit()
- pred = model.forecast(
- 12)
- Thêm bộ tham số mùa (P, D, Q, m)
- Dùng khi có mùa vụ rõ — ví dụ Tết

### Slide 6

- AUTOMATION
- Auto-ARIMA — tự dò tham số
- auto_arima.py
- import pmdarima as  pm
- model = pm.auto_arima(sales, seasonal=
- True, m=12 ,
- stepwise=
- True, trace=True) print(model.order, model.seasonal_order)
- pmdarima tự tìm tham số tốt nhất
- Tiết kiệm thời gian so với dò tay

### Slide 7

- SECTION 6 · LECTURE 5
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- ARIMA
- SARIMA
- auto-ARIMA
- BÀI TIẾP THEO
- →
- Facebook Prophet

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_