# Section 6 · Lecture 1 — Khái niệm time-series

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 01
- SECTION 6 · LECTURE 1
- Khái niệm time-series
- ~8 phút · 6 slides

### Slide 2

- TIME-SERIES VS CROSS-SECTIONAL
- Time-series khác gì dữ liệu thường?
- Thứ tự thời gian
- mang ý nghĩa
- Mỗi quan sát gắn với một mốc thời gian cụ thể
- Không được xáo trộn
- dữ liệu
- Shuffle phá vỡ quan hệ phụ thuộc theo thời gian
- Cross-sectional
- Quan sát độc lập nhau
- Thứ tự không quan trọng
- Có thể shuffle tự do
- vs
- Time-series
- Quan sát phụ thuộc quá khứ
- Thứ tự chính là thông tin
- Tuyệt đối không shuffle

### Slide 3

- CẤU TRÚC
- 4 thành phần của chuỗi thời gian
- 01
- Trend
- Xu hướng tăng/giảm dài hạn
- 02
- Seasonality
- Lặp lại theo chu kỳ cố định (tháng, mùa)
- 03
- Cyclical
- Dao động dài, chu kỳ không cố định
- 04
- Noise
- Biến động ngẫu nhiên còn lại
- Hiểu 4 thành phần này là hiểu được bản chất của một chuỗi thời gian.

### Slide 4

- DECOMPOSITION
- Tách chuỗi thành các thành phần
- decompose.py
- from statsmodels.tsa.seasonal import  seasonal_decompose
- result = seasonal_decompose(
- sales, model=
- "additive", period=12 )
- result.plot()
- # trend · seasonal · residual
- Tách chuỗi thành trend + seasonal + residual
- Additive
- vs
- Multiplicative
- Cộng tính: biên độ mùa ổn định · Nhân tính: biên độ tăng theo mức

### Slide 5

- VÍ DỤ VIỆT NAM
- Doanh số bán lẻ có mùa vụ Tết
- Doanh số
- tăng mạnh dịp Tết
- Seasonality lặp lại rõ rệt mỗi năm
- Tăng trưởng dài hạn
- qua các năm
- Trend đi lên ổn định

### Slide 6

- SECTION 6 · LECTURE 1
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- 4 thành phần
- decomposition
- additive / multiplicative
- BÀI TIẾP THEO
- →
- Tính dừng (stationarity) & ADF test

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_