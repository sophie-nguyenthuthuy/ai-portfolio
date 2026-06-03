# Section 3 · Lecture 7 — Window function — ROW_NUMBER, RANK, LAG, LEAD

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 7 · ~11 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Window function — vũ khí của analyst giỏi

**🎨 Visual:** `[AI image]` Cửa sổ trượt trên bảng.
**🎤 Speaker note:** "Biết cái này, bạn vượt 80% người học SQL."

### Slide 2 — Window function là gì

- Tính trên 1 "cửa sổ" dòng
- Không gom nhóm mất dòng (khác GROUP BY)

**🎨 Visual:** `[Mermaid]` So sánh GROUP BY (gộp) vs window (giữ dòng).
**🎤 Speaker note:** Điểm khác biệt cốt lõi với GROUP BY.

### Slide 3 — OVER & PARTITION BY

- `OVER (PARTITION BY ...)`
- Chia cửa sổ theo nhóm

**🎨 Visual:** `[Screen]` Cú pháp OVER.
**🎤 Speaker note:** PARTITION giống GROUP BY nhưng giữ nguyên dòng.

### Slide 4 — ROW_NUMBER, RANK, DENSE_RANK

- Đánh số / xếp hạng trong nhóm
- Khác nhau khi có giá trị trùng

**🎨 Visual:** `[Screen]` So sánh 3 hàm.
**🎤 Speaker note:** Lấy top N mỗi nhóm — bài toán cực phổ biến.

### Slide 5 — LAG & LEAD

- Lấy giá trị dòng trước/sau
- Tính tăng trưởng kỳ này vs kỳ trước

**🎨 Visual:** `[Screen]` LAG tính % tăng trưởng.
**🎤 Speaker note:** Cốt lõi cho phân tích chuỗi thời gian bằng SQL.

### Slide 6 — Running total

- Tổng luỹ kế (cộng dồn)
- `SUM() OVER (ORDER BY ...)`

**🎨 Visual:** `[Screen]` Doanh thu luỹ kế.
**🎤 Speaker note:** Dùng cho biểu đồ tích luỹ.

### Slide 7 — Tóm tắt & chuyển bài

- OVER · ROW_NUMBER · LAG/LEAD · running total
- Bài tiếp: index & tối ưu →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta làm truy vấn chạy nhanh hơn."

---

_← [Về Section README](../README.md)_
