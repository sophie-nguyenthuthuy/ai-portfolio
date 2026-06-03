# Section 3 · Lecture 12 — Schema giao dịch ngân hàng + 10 truy vấn

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE 12 · MINI-PROJECT
- Schema giao dịch ngân hàng + 10 truy vấn
- Ráp mọi kỹ năng SQL vào một bài toán thật.
- AI IMAGE
- Sơ đồ hệ thống ngân hàng
- S3 · Lecture 12

### Slide 2

- L12
- Mini-Project ngân hàng
- Bài toán
- Quản lý khách hàng · tài khoản · giao dịch
- Trả lời các câu hỏi nghiệp vụ thực tế
- Top khách hàng, số dư trung bình, tăng trưởng giao dịch
- BỐI CẢNH
- Ngân hàng — quen thuộc tại Việt Nam

### Slide 3

- L12
- Mini-Project ngân hàng
- Thiết kế schema — ER diagram
- customers
- id (PK)
- name
- accounts
- id (PK)
- customer_id (FK)
- balance
- transactions
- id (PK)
- account_id (FK)
- amount
- Quan hệ 1-n · chuẩn hoá để tránh trùng lặp dữ liệu.

### Slide 4

- L12
- Mini-Project ngân hàng
- Truy vấn cơ bản
- -- Số dư trung bình theo loại tài khoản SELECT type, avg(balance) AS sodu_tb FROM accounts GROUP BY type ORDER BY sodu_tb DESC;
- Áp dụng SELECT · GROUP BY · ORDER BY đã học.

### Slide 5

- L12
- Mini-Project ngân hàng
- Truy vấn nâng cao — JOIN + window
- -- Tăng trưởng giao dịch mỗi tháng / khách SELECT  c.name, t.month, t.total,
- t.total
- - lag(t.total) OVER  (
- PARTITION BY c.id ORDER BY  t.month
- )
- AS tang_truong FROM customers c JOIN monthly_tx t ON t.customer_id = c.id;
- Đây là phần khiến CV của bạn nổi bật.

### Slide 6

- L12
- Mini-Project ngân hàng · Bonus
- Phát hiện giao dịch bất thường
- -- Giao dịch lớn gấp 3 lần mức trung bình của tài khoản SELECT * FROM transactions t WHERE amount > 3 *  (
- SELECT avg(amount) FROM  transactions
- WHERE  account_id = t.account_id
- );
- Nền tảng cho bài toán fraud detection ở Capstone sau này.

### Slide 7

- SECTION 03 · HOÀN THÀNH
- Bạn đã có Python + SQL . Giờ ta xây nền toán cho ML.
- SQL cơ bản → nâng cao
- Window · Index · Schema
- Mini-Project ✅
- Section 4 · Toán & Thống kê cho AI
- →
- Mastering AI & Data Science

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_