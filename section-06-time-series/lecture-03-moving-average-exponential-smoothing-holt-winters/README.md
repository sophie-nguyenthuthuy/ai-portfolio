# Section 6 · Lecture 3 — Moving average, exponential smoothing, Holt-Winters

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Làm mượt & dự báo cơ bản

**🎨 Visual:** `[AI image]` Đường gồ ghề → đường mượt.
**🎤 Speaker note:** "Phương pháp cổ điển nhưng cực hữu dụng."

### Slide 2 — Moving Average

- Trung bình cửa sổ trượt
- Làm mượt nhiễu

**🎨 Visual:** `[Screen]` MA 7 ngày.
**🎤 Speaker note:** Nối lại rolling ở Section 2.

### Slide 3 — Exponential Smoothing

- Trọng số giảm dần về quá khứ
- Gần đây quan trọng hơn

**🎨 Visual:** `[Mermaid]` Trọng số mũ.
**🎤 Speaker note:** Phản ứng nhanh hơn với thay đổi mới.

### Slide 4 — Holt (trend)

- Thêm thành phần xu hướng

**🎨 Visual:** `[Mermaid]` Dự báo có trend.
**🎤 Speaker note:** Mở rộng cho chuỗi có xu hướng.

### Slide 5 — Holt-Winters (seasonality)

- Thêm cả mùa vụ
- Bộ ba: level + trend + seasonal

**🎨 Visual:** `[Screen]` Holt-Winters dự báo.
**🎤 Speaker note:** Mạnh cho dữ liệu có mùa rõ rệt.

### Slide 6 — Tóm tắt & chuyển bài

- MA · exponential · Holt-Winters
- Bài tiếp: ACF/PACF →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học công cụ chọn tham số cho ARIMA."

---

_← [Về Section README](../README.md)_
