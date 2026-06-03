# Section 6 · Lecture 9 — Dự báo doanh số / chứng khoán Việt Nam 🏆 **Capstone**

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 8

---

## Nội dung slide

### Slide 1

- 🏆
- SECTION 6 · CAPSTONE 2 🏆
- Dự báo doanh số / chứng khoán Việt Nam
- ~14 phút · 7 slides · screen recording

### Slide 2

- BÀI TOÁN
- Bài toán & dữ liệu
- Dữ liệu doanh số / cổ phiếu VN
- Mục tiêu: dự báo N kỳ tới
- Xác định rõ khung thời gian đánh giá

### Slide 3

- EDA
- EDA & decomposition
- eda.py
- decomp = seasonal_decompose(y, period=12 )
- decomp.plot()
- print("ADF p =", adfuller(y)[1])
- Tách trend / seasonality
- Kiểm tra tính dừng (ADF)
- Hiểu dữ liệu trước khi mô hình hoá

### Slide 4

- MÔ HÌNH HOÁ
- Đa phương pháp — để so sánh
- 01
- ARIMA / SARIMA
- Mô hình thống kê kinh điển
- 02
- Prophet
- Mạnh về ngày lễ, dễ dùng
- 03
- LSTM
- Deep learning cho chuỗi dài
- Mục tiêu là so sánh, không phải chọn sẵn một mô hình.

### Slide 5

- ĐÁNH GIÁ
- Đánh giá đúng cách
- MAE
- Mean Abs Error
- Trung bình sai số tuyệt đối
- RMSE
- Root MSE
- Phạt nặng sai số lớn
- MAPE
- Mean Abs % Error
- Sai số theo phần trăm
- ⚠ Backtesting bằng TimeSeriesSplit — không bao giờ shuffle.

### Slide 6

- KẾT LUẬN
- So sánh & trade-off
- MÔ HÌNH
- ĐIỂM MẠNH
- ĐÁNH ĐỔI
- ARIMA / SARIMA
- Nền tảng thống kê vững, xử lý mùa vụ
- Cần chuỗi dừng, dò tham số thủ công
- Prophet
- Ngày lễ, dễ dùng, robust với outlier
- Kém với quan hệ phi tuyến phức tạp
- LSTM
- Bắt phi tuyến, mạnh với chuỗi dài
- Cần nhiều dữ liệu, bắt buộc scale

### Slide 7

- PROJECT 2 / 7 ✓
- Section 6 hoàn thành
- Time Series — 9 lectures · Capstone 2 dự báo doanh số / chứng khoán VN
- SECTION TIẾP THEO
- →
- Section 7 · Nhập môn Deep Learning

### Slide 8

- 07
- SECTION 7 · 12 LECTURES · DEEP LEARNING
- Nhập môn Deep Learning
- Hiểu cách neural network hoạt động — forward, loss, backpropagation, optimizer; áp dụng regularization và xây mạng từ đầu bằng NumPy rồi tái hiện bằng PyTorch.

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_