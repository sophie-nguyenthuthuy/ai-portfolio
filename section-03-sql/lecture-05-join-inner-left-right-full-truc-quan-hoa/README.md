# Section 3 · Lecture 5 — JOIN — INNER, LEFT, RIGHT, FULL (trực quan hoá)

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- JOIN — nối các bảng

**🎨 Visual:** `[AI image]` Hai bảng ghép qua khoá chung.
**🎤 Speaker note:** "Dữ liệu thật nằm rải ở nhiều bảng — JOIN gom lại."

### Slide 2 — Vì sao cần JOIN

- Bảng khách hàng + bảng đơn hàng
- Khoá liên kết (key)

**🎨 Visual:** `[Mermaid]` Bảng customers ↔ orders.
**🎤 Speaker note:** Khoá ngoại (foreign key) nối các bảng.

### Slide 3 — INNER JOIN

- Chỉ giữ dòng khớp ở cả 2 bảng

**🎨 Visual:** `[Mermaid]` Venn — phần giao.
**🎤 Speaker note:** JOIN mặc định, dùng nhiều nhất.

### Slide 4 — LEFT / RIGHT JOIN

- Giữ tất cả bảng trái (hoặc phải)
- Không khớp → NULL

**🎨 Visual:** `[Mermaid]` Venn LEFT & RIGHT.
**🎤 Speaker note:** LEFT JOIN tìm khách chưa mua hàng.

### Slide 5 — FULL JOIN & self join

- FULL: giữ tất cả 2 bên
- Self join: nối bảng với chính nó

**🎨 Visual:** `[Mermaid]` Venn FULL + sơ đồ self join.
**🎤 Speaker note:** Self join cho quan hệ phân cấp (nhân viên-quản lý).

### Slide 6 — Tóm tắt & chuyển bài

- INNER · LEFT · RIGHT · FULL
- Bài tiếp: subquery & CTE →

**🎨 Visual:** `[Mermaid]` Tổng hợp 4 Venn.
**🎤 Speaker note:** "Giờ ta lồng truy vấn vào nhau."

---

_← [Về Section README](../README.md)_
