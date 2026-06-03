# Section 3 · Lecture 1 — CSDL quan hệ vs NoSQL — khi nào dùng cái nào

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 01
- ~8 phút · 6 slides
- CSDL quan hệ vs NoSQL — khi nào dùng cái nào
- Cơ sở dữ liệu — nơi dữ liệu thật sống.
- AI IMAGE
- Kho dữ liệu với nhiều ngăn chứa
- S3 · Lecture 1

### Slide 2

- L1
- CSDL quan hệ vs NoSQL
- Cơ sở dữ liệu quan hệ (RDBMS)
- Dữ liệu lưu dạng
- bảng
- , các bảng có quan hệ với nhau
- Hàng = bản ghi, cột = thuộc tính
- Schema cố định, được truy vấn bằng
- SQL
- Cấu trúc định nghĩa trước khi nạp dữ liệu
- MySQL · PostgreSQL · SQL Server
- customers
- id (PK)
- name
- city
- orders
- customer_id (FK)
- amount
- created_at

### Slide 3

- L1
- CSDL quan hệ vs NoSQL
- NoSQL — linh hoạt về schema
- Document
- JSON lồng nhau, mỗi bản ghi tự mô tả — MongoDB
- Key–Value
- Tra cứu siêu nhanh theo khoá — Redis
- Graph
- Quan hệ là trung tâm — Neo4j
- Column
- Tối ưu cho cột & quy mô lớn — Cassandra

### Slide 4

- L1
- CSDL quan hệ vs NoSQL
- Khi nào dùng cái nào
- TIÊU CHÍ
- RDBMS
- NOSQL
- Cấu trúc dữ liệu
- Có cấu trúc, quan hệ chặt
- Linh hoạt, schema thay đổi
- Điểm mạnh
- Giao dịch, báo cáo, toàn vẹn
- Mở rộng ngang, quy mô lớn
- Ví dụ bài toán
- Ngân hàng, bán hàng, kế toán
- Log, IoT, mạng xã hội

### Slide 5

- L1
- CSDL quan hệ vs NoSQL
- SQL vẫn là ngôn ngữ phổ quát của dữ liệu.
- Mọi vai trò Data — Analyst, Engineer, Scientist — đều cần SQL. Đây là kỹ năng nhà tuyển dụng kiểm tra nhiều nhất.

### Slide 6

- L1
- Tóm tắt
- Tóm tắt & chuyển bài
- RDBMS vs NoSQL
- Khi nào dùng cái nào
- SQL — kỹ năng nền tảng
- Bài tiếp · Cài đặt cơ sở dữ liệu
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_