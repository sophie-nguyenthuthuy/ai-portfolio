# Section 3 · Lecture 3 — SELECT, WHERE, ORDER BY, LIMIT

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 03
- ~9 phút · 6 slides
- SELECT, WHERE, ORDER BY, LIMIT
- Truy vấn dữ liệu — bước đầu tiên, và là 70% công việc SQL hằng ngày.
- AI IMAGE
- Câu lệnh SELECT phát sáng
- S3 · Lecture 3

### Slide 2

- L3
- Truy vấn cơ bản
- SELECT & FROM — lấy cột từ bảng
- -- Chọn cột cụ thể từ một bảng SELECT name, city FROM customers; -- SELECT * lấy tất cả cột SELECT * FROM customers;
- Tránh
- SELECT *
- trong production — chỉ lấy cột bạn cần.

### Slide 3

- L3
- Truy vấn cơ bản
- WHERE — lọc dòng theo điều kiện
- SELECT name, amount FROM orders WHERE city = 'Hà Nội'   AND amount > 500000   AND name LIKE 'Nguyễn%';
- AND · OR kết hợp nhiều điều kiện
- IN · BETWEEN cho danh sách & khoảng giá trị
- LIKE với ký tự % để tìm gần đúng

### Slide 4

- L3
- Truy vấn cơ bản
- ORDER BY — sắp xếp kết quả
- SELECT name, revenue FROM customers ORDER BY revenue DESC;
- Kết quả · revenue DESC
- Mai Anh 9.8M
- Quốc Bảo 7.1M
- Thu Hà 5.6M
- Minh Khôi 4.2M

### Slide 5

- L3
- Truy vấn cơ bản
- LIMIT — giới hạn số dòng trả về
- -- Top 5 khách hàng theo doanh thu SELECT name, revenue FROM customers ORDER BY revenue  DESC LIMIT 5;
- Lấy nhanh Top N kết quả
- Cực quan trọng khi bảng có hàng triệu dòng
- Không tải toàn bộ dữ liệu khi chỉ cần vài dòng

### Slide 6

- L3
- Tóm tắt
- Tóm tắt & chuyển bài
- SELECT
- WHERE
- ORDER BY
- LIMIT
- Bài tiếp · Hàm tổng hợp & GROUP BY
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_