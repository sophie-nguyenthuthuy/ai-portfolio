# Section 3 · Lecture 6 — Subquery & CTE (mệnh đề WITH)

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 06
- ~9 phút · 6 slides
- Subquery & CTE (mệnh đề WITH)
- Khi một câu SELECT không đủ, ta lồng chúng vào nhau.
- AI IMAGE
- Truy vấn lồng trong truy vấn
- S3 · Lecture 6

### Slide 2

- L6
- Truy vấn lồng nhau
- Subquery — truy vấn bên trong truy vấn
- -- Khách hàng chi tiêu trên mức trung bình SELECT name, total FROM customers WHERE total >  (
- SELECT avg(total) FROM  customers
- );
- Subquery có thể đặt trong WHERE, FROM hoặc SELECT.

### Slide 3

- L6
- Truy vấn lồng nhau
- Subquery tương quan
- -- Phụ thuộc từng dòng bảng ngoài SELECT name FROM customers c WHERE total >  (
- SELECT avg (total)
- FROM  customers
- WHERE  city = c.city
- );
- Chạy lặp lại cho từng dòng của truy vấn ngoài
- Rất mạnh nhưng chậm — lưu ý hiệu năng

### Slide 4

- L6
- Truy vấn lồng nhau
- CTE (WITH) — đặt tên cho truy vấn con
- WITH vip AS  (
- SELECT customer_id, sum(amount) AS  total
- FROM orders GROUP BY  customer_id
- )
- SELECT * FROM vip WHERE total > 10000000;
- Dễ đọc hơn nhiều so với subquery lồng nhiều tầng.

### Slide 5

- L6
- Truy vấn lồng nhau
- CTE đệ quy — cho dữ liệu phân cấp
- Truy vấn tự gọi lại chính nó
- Cho dữ liệu dạng cây / phân cấp
- Sơ đồ tổ chức, danh mục sản phẩm lồng nhau
- Điện tử
- └ Điện thoại
- └ iPhone 15

### Slide 6

- L6
- Tóm tắt
- Tóm tắt & chuyển bài
- Subquery
- CTE (WITH)
- CTE đệ quy
- Bài tiếp · Window function
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_