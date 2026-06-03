# Section 4 · Lecture 13 — p-value, sai lầm loại I/II, t-test, chi-square

_Phần của: **Section 4: Toán & Thống kê cho AI**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- p-value & các phép kiểm định

**🎨 Visual:** `[AI image]` Cán cân bằng chứng.
**🎤 Speaker note:** "p-value bị hiểu sai nhiều nhất trong thống kê."

### Slide 2 — p-value là gì

- Xác suất thấy kết quả nếu H0 đúng
- Nhỏ → bằng chứng chống H0

**🎨 Visual:** `[Mermaid]` Vùng đuôi phân phối.
**🎤 Speaker note:** p nhỏ ≠ "quan trọng" — chỉ là "khó do ngẫu nhiên".

### Slide 3 — Ngưỡng α & quyết định

- α thường = 0.05
- p < α → bác H0

**🎨 Visual:** `[Mermaid]` p so với α.
**🎤 Speaker note:** Ngưỡng do bạn chọn trước, không phải sau.

### Slide 4 — Sai lầm loại I & II

- Loại I: báo động giả
- Loại II: bỏ sót thật

**🎨 Visual:** `[Mermaid]` Bảng 2×2 confusion của quyết định.
**🎤 Speaker note:** Liên hệ Precision/Recall sau này.

### Slide 5 — t-test & chi-square

- t-test: so sánh trung bình
- chi-square: kiểm định phân loại

**🎨 Visual:** `[Screen]` scipy.stats ttest/chi2.
**🎤 Speaker note:** Hai test phổ biến nhất trong thực tế.

### Slide 6 — Tóm tắt & chuyển bài

- p-value · α · loại I/II · t-test/chi2
- Bài tiếp: EDA Project →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả vào 1 bài EDA thật."

---

_← [Về Section README](../README.md)_
