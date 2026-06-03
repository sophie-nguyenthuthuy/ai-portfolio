# Section 3 · Lecture 2 — Cài đặt MySQL / PostgreSQL / DuckDB local

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 02
- ~9 phút · 6 slides
- Cài đặt MySQL / PostgreSQL / DuckDB local
- Dựng database trên máy bạn — học SQL phải có nơi gõ thật.
- AI IMAGE
- 3 logo: MySQL · PostgreSQL · DuckDB
- S3 · Lecture 2

### Slide 2

- L2
- Cài đặt cơ sở dữ liệu
- Chọn database nào để học
- DUCKDB
- POSTGRESQL
- Cài đặt
- pip install — chạy ngay
- Cài server riêng
- Phù hợp
- Học nhanh, phân tích local
- Môi trường giống doanh nghiệp
- Khoá học dùng
- Mặc định khi luyện tập
- Khi mô phỏng thực tế

### Slide 3

- L2
- Cài đặt cơ sở dữ liệu
- Cài DuckDB — không cần server
- # Cài đặt chỉ với một dòng pip install duckdb # Chạy SQL ngay bên trong Python import  duckdb
- duckdb.
- sql("SELECT 42 AS answer").show()
- Tuyệt vời cho người mới: không server, không cấu hình.

### Slide 4

- L2
- Cài đặt cơ sở dữ liệu
- Cài PostgreSQL — môi trường doanh nghiệp
- Tải & cài server PostgreSQL từ trang chính thức
- Quản lý bằng công cụ trực quan
- pgAdmin hoặc DBeaver để xem bảng, chạy query
- Đây là môi trường gần với sản phẩm thật nhất
- SCREEN
- Kết nối pgAdmin tới server

### Slide 5

- L2
- Cài đặt cơ sở dữ liệu
- Nạp dữ liệu mẫu
- -- Tạo bảng từ file CSV bán lẻ CREATE TABLE sales  AS SELECT * FROM read_csv_auto('retail.csv'); SELECT count(*) FROM sales;
- Import file CSV vào bảng
- Dùng một dataset bán lẻ xuyên suốt section
- Mọi ví dụ SQL sau này dựa trên bộ dữ liệu này

### Slide 6

- L2
- Tóm tắt
- Tóm tắt & chuyển bài
- DuckDB
- PostgreSQL + pgAdmin
- Nạp dữ liệu mẫu
- Bài tiếp · SELECT cơ bản
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_