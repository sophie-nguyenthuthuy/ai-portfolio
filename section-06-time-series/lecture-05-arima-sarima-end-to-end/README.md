# Section 6 · Lecture 5 — ARIMA & SARIMA end-to-end

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- ARIMA & SARIMA

**🎨 Visual:** `[AI image]` Mô hình dự báo cổ điển.
**🎤 Speaker note:** "Mô hình thống kê kinh điển nhất cho time-series."

### Slide 2 — AR, I, MA

- AR: phụ thuộc quá khứ
- I: sai phân
- MA: phụ thuộc nhiễu quá khứ

**🎨 Visual:** `[Mermaid]` 3 thành phần ARIMA.
**🎤 Speaker note:** Ghép 3 ý đã học ở bài trước.

### Slide 3 — ARIMA(p,d,q)

- Ý nghĩa từng tham số
- Chọn từ ACF/PACF

**🎨 Visual:** `[Mermaid]` p,d,q là gì.
**🎤 Speaker note:** Nối lại bài ACF/PACF.

### Slide 4 — Quy trình chuẩn

- Kiểm tra dừng → sai phân → chọn p,q → fit

**🎨 Visual:** `[Mermaid]` Flowchart quy trình.
**🎤 Speaker note:** Làm theo từng bước, không nhảy cóc.

### Slide 5 — SARIMA (mùa vụ)

- Mở rộng cho seasonality
- Thêm thành phần mùa

**🎨 Visual:** `[Screen]` SARIMA cho doanh số có Tết.
**🎤 Speaker note:** Dùng khi có mùa vụ rõ.

### Slide 6 — Auto-ARIMA

- pmdarima tự tìm tham số
- Cách làm thực tế

**🎨 Visual:** `[Screen]` auto_arima.
**🎤 Speaker note:** Tiết kiệm thời gian dò tay.

### Slide 7 — Tóm tắt & chuyển bài

- ARIMA · SARIMA · auto-ARIMA
- Bài tiếp: Prophet & ML →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta thử cách hiện đại, dễ dùng hơn."

---

_← [Về Section README](../README.md)_
