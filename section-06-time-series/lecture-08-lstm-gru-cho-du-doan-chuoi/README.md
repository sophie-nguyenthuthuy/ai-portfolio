# Section 6 · Lecture 8 — LSTM & GRU cho dự đoán chuỗi

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 08
- SECTION 6 · LECTURE 8
- LSTM & GRU cho dự đoán chuỗi
- ~9 phút · 6 slides

### Slide 2

- MOTIVATION
- Vì sao cần “bộ nhớ”?
- Regression thường quên quá khứ
- Chuỗi cần
- nhớ ngữ cảnh
- dài
- Thông tin phải truyền qua các bước thời gian
- t₁
- →
- t₂
- →
- t₃
- →
- t₄

### Slide 3

- RNN
- RNN & vấn đề vanishing gradient
- RNN chỉ có trí nhớ ngắn hạn
- Vanishing gradient
- qua nhiều bước
- Gradient mờ dần → khó nhớ quan hệ xa

### Slide 4

- LSTM
- Cơ chế cổng (gates)
- ⌫
- Forget gate
- Quyết định quên thông tin nào
- +
- Input gate
- Quyết định ghi thông tin mới
- →
- Output gate
- Quyết định xuất ra gì
- Cell state mang thông tin xuyên suốt; các cổng kiểm soát nhớ và quên.

### Slide 5

- CHUẨN BỊ
- GRU & chuẩn bị dữ liệu
- lstm_prep.py
- from sklearn.preprocessing import  MinMaxScaler
- scaled = MinMaxScaler().fit_transform(series)
- # [samples, timesteps, features] X = X.reshape((X.shape[0], window, 1))
- GRU gọn hơn LSTM, ít tham số
- ⚠ LSTM bắt buộc scale về [0, 1]
- ARIMA thì không cần scale

### Slide 6

- SECTION 6 · LECTURE 8
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- RNN
- LSTM
- GRU
- scaling
- BÀI TIẾP THEO
- →
- 🏆 Capstone 2 — Dự báo time-series

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_