# Section 2 · Lecture 11 — Pandas Phần 2 — groupby, merge, pivot, xử lý dữ liệu thiếu

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~12 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Pandas thực chiến

**🎨 Visual:** `[AI image]` Nhiều bảng ghép lại.
**🎤 Speaker note:** "Đây là phần biến bạn từ biết Pandas thành dùng được Pandas."

### Slide 2 — groupby

- Gom nhóm + tính tổng hợp
- `df.groupby('nhom').sum()`

**🎨 Visual:** `[Mermaid]` Split → Apply → Combine.
**🎤 Speaker note:** Tư duy "split-apply-combine" — cốt lõi.

### Slide 3 — Hàm tổng hợp

- sum, mean, count, min, max
- `.agg()` nhiều hàm cùng lúc

**🎨 Visual:** `[Screen]` groupby + agg.
**🎤 Speaker note:** Ví dụ: doanh thu trung bình theo vùng.

### Slide 4 — merge & join

- Nối 2 DataFrame theo key
- how: inner, left, right, outer

**🎨 Visual:** `[Mermaid]` Venn 4 kiểu join.
**🎤 Speaker note:** Giống JOIN trong SQL.

### Slide 5 — pivot & pivot_table

- Xoay dữ liệu dài ↔ rộng
- Tạo bảng tổng hợp đa chiều

**🎨 Visual:** `[Screen]` pivot_table doanh số.
**🎤 Speaker note:** Giống PivotTable trong Excel.

### Slide 6 — Xử lý dữ liệu thiếu

- `isna()`, `dropna()`, `fillna()`
- Điền median/mean/mode

**🎨 Visual:** `[Screen]` fillna bằng median.
**🎤 Speaker note:** Vì sao median > mean cho dữ liệu lệch (income).

### Slide 7 — Tóm tắt & chuyển bài

- groupby · merge · pivot · missing
- Bài tiếp: NumPy →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xuống tầng nền tảng tốc độ — NumPy."

---

_← [Về Section README](../README.md)_
