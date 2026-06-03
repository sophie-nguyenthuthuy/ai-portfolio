# Section 6 · Lecture 4 — ACF / PACF — chọn bậc cho ARIMA

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 6 · LECTURE 4
- ACF / PACF — chọn bậc cho ARIMA
- ~7 phút · 5 slides

### Slide 2

- ACF
- Tự tương quan (ACF)
- Tương quan của chuỗi với chính nó ở các độ trễ (lags)
- Giúp phát hiện mùa vụ & quan hệ trễ

### Slide 3

- PACF
- Tương quan riêng phần (PACF)
- Loại bỏ ảnh hưởng của các độ trễ trung gian
- Bổ trợ ACF để chọn bậc mô hình

### Slide 4

- ĐỌC BIỂU ĐỒ
- Quy tắc chọn p và q
- acf_pacf.py
- from statsmodels.graphics.tsaplots import  plot_acf, plot_pacf
- plot_acf(series.diff().dropna(),  lags=
- 40 )
- plot_pacf(series.diff().dropna(), lags=
- 40) # PACF cat sau lag p  ->  AR(p) # ACF  cat sau lag q  ->  MA(q)
- PACF cắt sau lag p → bậc AR (p)
- ACF cắt sau lag q → bậc MA (q)
- Quy tắc thực hành — không cần lý thuyết sâu

### Slide 5

- SECTION 6 · LECTURE 4
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- ACF
- PACF
- chọn p, q
- BÀI TIẾP THEO
- →
- ARIMA & SARIMA end-to-end

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_