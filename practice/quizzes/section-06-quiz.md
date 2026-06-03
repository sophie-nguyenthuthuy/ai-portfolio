# Quiz — Section 6: TIME SERIES

_8 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Vì sao KHÔNG được dùng `train_test_split(shuffle=True)` cho time-series?
- A. Vì chạy chậm
- B. ✅ Vì xáo trộn làm rò rỉ tương lai vào quá khứ, phá vỡ thứ tự thời gian
- C. Vì dữ liệu quá lớn
- D. Vì không có nhãn
*Giải thích: time-series phải giữ thứ tự — dùng TimeSeriesSplit.*

**Câu 2.** "Stationarity" (tính dừng) nghĩa là gì?
- A. Dữ liệu không thay đổi
- B. ✅ Trung bình và phương sai ổn định theo thời gian
- C. Không có nhiễu
- D. Chuỗi tăng đều
*Giải thích: nhiều mô hình (ARIMA) yêu cầu chuỗi dừng.*

**Câu 3.** Chữ "I" trong ARIMA tương ứng với kỹ thuật nào?
- A. Interpolation
- B. ✅ Integrated — sai phân (differencing)
- C. Index
- D. Inference
*Giải thích: differencing biến chuỗi không dừng thành dừng.*

**Câu 4.** Mô hình nào xử lý ngày lễ (vd Tết) tốt nhất một cách dễ dàng?
- A. ARIMA
- B. ✅ Facebook Prophet
- C. Linear Regression
- D. KNN
*Giải thích: Prophet cho phép khai báo holidays trực tiếp.*

**Câu 5.** ADF test dùng để kiểm tra điều gì?
- A. Tính tuyến tính
- B. ✅ Tính dừng của chuỗi thời gian
- C. Tương quan giữa 2 chuỗi
- D. Phân phối chuẩn
*Giải thích: p-value < 0.05 → chuỗi dừng.*

**Câu 6.** ACF và PACF dùng để làm gì trong ARIMA?
- A. Đánh giá model
- B. ✅ Giúp chọn bậc p (AR) và q (MA)
- C. Làm sạch dữ liệu
- D. Vẽ dự báo
*Giải thích: đọc ACF/PACF để chọn tham số ARIMA.*

**Câu 7.** Khi dùng LSTM cho time-series, bước bắt buộc nào KHÁC với ARIMA?
- A. Không cần dữ liệu
- B. ✅ Phải scale dữ liệu về [0,1]
- C. Phải xáo trộn dữ liệu
- D. Phải bỏ trend
*Giải thích: LSTM nhạy với scale; ARIMA thì không cần scale.*

**Câu 8.** Metric nào KHÔNG phù hợp để đánh giá dự báo time-series?
- A. MAE
- B. RMSE
- C. MAPE
- D. ✅ Accuracy
*Giải thích: accuracy cho phân loại; dự báo số dùng MAE/RMSE/MAPE.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-06-time-series/README.md)_
