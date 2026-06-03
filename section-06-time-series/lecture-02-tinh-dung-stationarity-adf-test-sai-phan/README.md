# Section 6 · Lecture 2 — Tính dừng (stationarity), ADF test, sai phân

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tính dừng (Stationarity)

**🎨 Visual:** `[AI image]` Chuỗi dừng vs không dừng.
**🎤 Speaker note:** "Nhiều mô hình yêu cầu chuỗi phải 'dừng'."

### Slide 2 — Chuỗi dừng là gì

- Trung bình, phương sai ổn định theo thời gian

**🎨 Visual:** `[Mermaid]` Chuỗi phẳng vs có xu hướng.
**🎤 Speaker note:** Dễ dự báo hơn khi chuỗi dừng.

### Slide 3 — Kiểm định ADF

- Augmented Dickey-Fuller test
- p-value < 0.05 → dừng

**🎨 Visual:** `[Screen]` Chạy ADF test.
**🎤 Speaker note:** Nối lại p-value ở Section 4.

### Slide 4 — Sai phân (differencing)

- Trừ giá trị kỳ trước
- Biến chuỗi không dừng → dừng

**🎨 Visual:** `[Mermaid]` Trước/sau sai phân.
**🎤 Speaker note:** Đây là chữ "I" trong ARIMA.

### Slide 5 — Bao nhiêu lần sai phân

- Thường 1-2 lần là đủ
- Sai phân quá nhiều = mất thông tin

**🎨 Visual:** `[Screen]` So sánh d=0,1,2.
**🎤 Speaker note:** Kiểm tra lại ADF sau mỗi lần.

### Slide 6 — Tóm tắt & chuyển bài

- dừng · ADF · sai phân
- Bài tiếp: smoothing & Holt-Winters →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta làm mượt chuỗi để thấy xu hướng."

---

_← [Về Section README](../README.md)_
