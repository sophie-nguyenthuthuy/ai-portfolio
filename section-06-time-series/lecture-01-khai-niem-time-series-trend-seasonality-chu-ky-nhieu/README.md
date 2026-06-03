# Section 6 · Lecture 1 — Khái niệm time-series — trend, seasonality, chu kỳ, nhiễu

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Dữ liệu chuỗi thời gian

**🎨 Visual:** `[AI image]` Đường biểu đồ theo thời gian.
**🎤 Speaker note:** "Doanh số, giá cổ phiếu, log hệ thống — đều là time-series."

### Slide 2 — Time-series khác gì dữ liệu thường

- Thứ tự thời gian có ý nghĩa
- Không được xáo trộn

**🎨 Visual:** `[Mermaid]` So sánh cross-sectional vs time-series.
**🎤 Speaker note:** Đây là điểm khiến nó cần xử lý riêng.

### Slide 3 — 4 thành phần

- Trend (xu hướng)
- Seasonality (mùa vụ)
- Cyclical (chu kỳ)
- Noise (nhiễu)

**🎨 Visual:** `[Mermaid]` Tách 4 thành phần.
**🎤 Speaker note:** Hiểu 4 cái này = hiểu chuỗi thời gian.

### Slide 4 — Decomposition

- Tách chuỗi thành các thành phần
- Additive vs Multiplicative

**🎨 Visual:** `[Screen]` seasonal_decompose.
**🎤 Speaker note:** Bước đầu khi nhìn bất kỳ chuỗi nào.

### Slide 5 — Ví dụ thực tế VN

- Doanh số tăng dịp Tết (seasonality)
- Tăng trưởng dài hạn (trend)

**🎨 Visual:** `[Screen]` Biểu đồ doanh số có Tết.
**🎤 Speaker note:** Liên hệ mùa vụ kinh doanh tại VN.

### Slide 6 — Tóm tắt & chuyển bài

- 4 thành phần · decomposition
- Bài tiếp: tính dừng & ADF →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học khái niệm cốt lõi: tính dừng."

---

_← [Về Section README](../README.md)_
