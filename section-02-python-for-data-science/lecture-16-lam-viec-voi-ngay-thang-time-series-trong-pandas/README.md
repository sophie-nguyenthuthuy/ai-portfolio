# Section 2 · Lecture 16 — Làm việc với ngày tháng & time-series trong Pandas

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Dữ liệu theo thời gian

**🎨 Visual:** `[AI image]` Lịch + đường xu hướng.
**🎤 Speaker note:** "Doanh số, log, giá cổ phiếu — đều là time-series."

### Slide 2 — Kiểu datetime

- `pd.to_datetime()`
- Đặt cột thời gian làm index

**🎨 Visual:** `[Screen]` Chuyển string → datetime.
**🎤 Speaker note:** Sai kiểu datetime = mọi phân tích sau sai.

### Slide 3 — Trích thành phần thời gian

- year, month, day, weekday
- `.dt` accessor

**🎨 Visual:** `[Screen]` df['ngay'].dt.month.
**🎤 Speaker note:** Tạo feature thời gian cho model.

### Slide 4 — Resample

- Gom theo giờ/ngày/tháng
- `.resample('M').sum()`

**🎨 Visual:** `[Screen]` Resample doanh số theo tháng.
**🎤 Speaker note:** Đổi tần suất dữ liệu cực tiện.

### Slide 5 — Rolling window

- Trung bình trượt
- `.rolling(7).mean()`

**🎨 Visual:** `[Screen]` Đường trung bình trượt 7 ngày.
**🎤 Speaker note:** Làm mượt nhiễu, thấy xu hướng.

### Slide 6 — Tóm tắt & chuyển bài

- datetime · resample · rolling
- Bài tiếp: Regex →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xử lý dữ liệu văn bản lộn xộn."

---

_← [Về Section README](../README.md)_
