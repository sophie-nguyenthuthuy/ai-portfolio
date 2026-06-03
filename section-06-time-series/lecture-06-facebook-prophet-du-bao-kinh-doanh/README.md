# Section 6 · Lecture 6 — Facebook Prophet — dự báo kinh doanh

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 06
- SECTION 6 · LECTURE 6
- Facebook Prophet — dự báo kinh doanh
- ~8 phút · 6 slides

### Slide 2

- VÌ SAO PROPHET
- Ưu điểm cho dân kinh doanh
- Robust
- Xử lý tốt missing & outlier
- Holidays
- Thêm ngày lễ dễ dàng
- Dễ dùng
- Ít cần thống kê sâu
- Sản phẩm của Meta — được dân kinh doanh ưa chuộng vì dễ dùng.

### Slide 3

- MÔ HÌNH CỘNG TÍNH
- Prophet = tổng các thành phần
- Trend
- →
- Seasonality
- →
- Holidays
- →
- Forecast
- Mô hình cộng tính (additive) nên rất dễ diễn giải.

### Slide 4

- HOLIDAYS
- Thêm ngày lễ Việt Nam
- prophet_tet.py
- from prophet import  Prophet
- tet = pd.DataFrame({
- "holiday": "tet" ,
- "ds": ["2024-02-10", "2025-01-29" ]})
- m = Prophet(holidays=tet, yearly_seasonality=
- True )
- m.fit(df)
- # df: cot ds, y
- Khai báo Tết & lễ VN
- Cải thiện dự báo mùa cao điểm
- Cực hữu ích cho bán lẻ VN

### Slide 5

- UNCERTAINTY
- Trực quan & khoảng tin cậy
- prophet_plot.py
- future   = m.make_future_dataframe(periods=90 )
- forecast = m.predict(future)
- m.plot(forecast)
- # yhat + uncertainty
- Biểu đồ dự báo kèm khoảng tin cậy
- Giúp ra quyết định thận trọng hơn

### Slide 6

- SECTION 6 · LECTURE 6
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- Prophet
- holidays
- uncertainty
- BÀI TIẾP THEO
- →
- Tiếp cận ML: sliding window + XGBoost

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_