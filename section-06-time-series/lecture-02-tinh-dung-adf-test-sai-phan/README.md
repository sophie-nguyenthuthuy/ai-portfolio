# Section 6 · Lecture 2 — Tính dừng, ADF test & sai phân

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 02
- SECTION 6 · LECTURE 2
- Tính dừng, ADF test & sai phân
- ~8 phút · 6 slides

### Slide 2

- STATIONARITY
- Chuỗi dừng (stationary) là gì?
- Trung bình ổn định theo thời gian
- Phương sai ổn định theo thời gian
- Không còn trend hay seasonality sót lại
- Chuỗi dừng thì dễ dự báo hơn nhiều

### Slide 3

- ADF TEST
- Kiểm định Augmented Dickey-Fuller
- adf.py
- from statsmodels.tsa.stattools import  adfuller
- stat, pval, *_ = adfuller(series)
- print(f"p-value = {pval:.4f}") # p-value < 0.05  ->  chuoi DUNG
- p-value < 0.05 → chuỗi dừng
- Ngược lại → cần xử lý thêm
- Nối lại khái niệm p-value ở Section 4

### Slide 4

- DIFFERENCING
- Sai phân để khử trend
- Trừ giá trị kỳ trước: y_t − y_{t-1}
- Biến chuỗi không dừng → dừng
- Chính là chữ “I” trong ARIMA

### Slide 5

- BAO NHIÊU LẦN?
- Sai phân bao nhiêu lần là đủ?
- diff.py
- for d in [0, 1, 2 ]:
- p = adfuller(series.diff(d).dropna())[
- 1 ]
- print(d, round(p, 4)) # 0 0.6213   1 0.0102   2 0.0006
- Thường 1–2 lần là đủ
- Sai phân quá nhiều = mất thông tin
- Kiểm tra lại ADF sau mỗi lần

### Slide 6

- SECTION 6 · LECTURE 2
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- stationarity
- ADF test
- differencing (d)
- BÀI TIẾP THEO
- →
- Smoothing & Holt-Winters

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_