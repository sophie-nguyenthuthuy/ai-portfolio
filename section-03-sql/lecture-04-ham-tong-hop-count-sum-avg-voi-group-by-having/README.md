# Section 3 · Lecture 4 — Hàm tổng hợp — COUNT, SUM, AVG với GROUP BY / HAVING

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tổng hợp & gom nhóm dữ liệu

**🎨 Visual:** `[AI image]` Nhiều dòng → 1 con số.
**🎤 Speaker note:** "Đây là nơi SQL trả lời câu hỏi kinh doanh."

### Slide 2 — Hàm tổng hợp

- COUNT, SUM, AVG, MIN, MAX

**🎨 Visual:** `[Screen]` Tính tổng doanh thu.
**🎤 Speaker note:** Gộp nhiều dòng thành 1 giá trị.

### Slide 3 — GROUP BY

- Gom nhóm trước khi tổng hợp
- Doanh thu theo từng vùng

**🎨 Visual:** `[Mermaid]` Gom nhóm → tính tổng từng nhóm.
**🎤 Speaker note:** Giống groupby trong Pandas.

### Slide 4 — HAVING vs WHERE

- WHERE lọc dòng (trước nhóm)
- HAVING lọc nhóm (sau nhóm)

**🎨 Visual:** `[Mermaid]` Thứ tự: WHERE → GROUP BY → HAVING.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn kinh điển.

### Slide 5 — Ví dụ thực tế

- Vùng có doanh thu > 1 tỷ
- Khách mua > 10 đơn

**🎨 Visual:** `[Screen]` GROUP BY + HAVING.
**🎤 Speaker note:** Liên hệ phân tích bán lẻ.

### Slide 6 — Tóm tắt & chuyển bài

- aggregate · GROUP BY · HAVING
- Bài tiếp: JOIN →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta nối nhiều bảng lại với nhau."

---

_← [Về Section README](../README.md)_
