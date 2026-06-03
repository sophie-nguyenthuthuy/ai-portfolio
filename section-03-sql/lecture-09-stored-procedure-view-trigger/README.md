# Section 3 · Lecture 9 — Stored procedure, view, trigger

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 09
- ~7 phút · 6 slides
- Stored procedure, view, trigger
- Database không chỉ chứa dữ liệu — nó còn chạy được logic.
- AI IMAGE
- Bánh răng vận hành bên trong database
- S3 · Lecture 9

### Slide 2

- L9
- Logic trong database
- View — truy vấn lưu sẵn như bảng ảo
- CREATE VIEW top_khach  AS SELECT name, sum(amount) AS total FROM orders GROUP BY name; SELECT * FROM top_khach;
- Tái sử dụng, ẩn bớt độ phức tạp
- Lý tưởng cho các báo cáo lặp lại

### Slide 3

- L9
- Logic trong database
- Stored procedure — khối lệnh lưu sẵn
- CREATE PROCEDURE tang_hang(id INT) BEGIN   UPDATE  customers
- SET tier = 'VIP'   WHERE customer_id = id; END;
- Đóng gói nghiệp vụ phức tạp, gọi lại nhiều lần

### Slide 4

- L9
- Logic trong database
- Trigger — tự chạy khi có sự kiện
- INSERT / UPDATE
- sự kiện xảy ra
- →
- Trigger kích hoạt
- tự động, không cần gọi tay
- →
- Ghi log
- vd: lưu lịch sử thay đổi
- Mạnh nhưng dùng cẩn thận — chạy ngầm nên khó debug.

### Slide 5

- L9
- Logic trong database
- Khi nào dùng cái nào
- CÔNG CỤ
- DÙNG CHO
- View
- Báo cáo lặp lại, đơn giản hoá truy vấn
- Procedure
- Đóng gói nghiệp vụ nhiều bước
- Trigger
- Tự động hoá theo sự kiện

### Slide 6

- L9
- Tóm tắt
- Tóm tắt & chuyển bài
- View
- Stored procedure
- Trigger
- Bài tiếp · OLTP vs OLAP
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_