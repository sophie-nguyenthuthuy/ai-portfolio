# Section 3 · Lecture 5 — JOIN — INNER, LEFT, RIGHT, FULL

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 05
- ~10 phút · 6 slides
- JOIN — INNER, LEFT, RIGHT, FULL
- Dữ liệu thật nằm rải ở nhiều bảng — JOIN gom chúng lại.
- AI IMAGE
- Hai bảng ghép lại qua khoá chung
- S3 · Lecture 5

### Slide 2

- L5
- Nối các bảng
- Vì sao cần JOIN
- Thông tin khách hàng ở một bảng, đơn hàng ở bảng khác
- Nối qua
- khoá liên kết
- (key) chung
- Khoá ngoại — foreign key — trỏ về khoá chính của bảng kia
- customers
- id (PK)
- name
- orders
- customer_id (FK)
- amount

### Slide 3

- L5
- Nối các bảng
- INNER JOIN — chỉ giữ dòng khớp cả hai bảng
- Là JOIN mặc định và dùng nhiều nhất
- Loại bỏ mọi dòng không có cặp khớp ở cả hai bên

### Slide 4

- L5
- Nối các bảng
- LEFT / RIGHT JOIN — giữ trọn một bên
- Giữ tất cả dòng của bảng trái (hoặc phải)
- Không có cặp khớp → cột bên kia là NULL
- LEFT JOIN giúp tìm khách hàng chưa từng mua

### Slide 5

- L5
- Nối các bảng
- FULL JOIN & self join
- FULL JOIN — giữ tất cả dòng của cả hai bảng
- Self join
- — nối một bảng với chính nó
- Cho quan hệ phân cấp: nhân viên ↔ quản lý

### Slide 6

- L5
- Tóm tắt
- Tóm tắt & chuyển bài
- INNER
- LEFT
- RIGHT
- FULL
- Self join
- Bài tiếp · Subquery & CTE
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_