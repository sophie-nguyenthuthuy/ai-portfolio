# Section 3 · Lecture 11 — Kết nối Python với SQL

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 11
- ~8 phút · 6 slides
- Kết nối Python với SQL
- Cầu nối thực tế: lấy dữ liệu từ database vào Pandas.
- AI IMAGE
- Python ↔ database
- S3 · Lecture 11

### Slide 2

- L11
- Python ↔ SQL
- Vì sao kết nối
- Database
- truy vấn dữ liệu thô
- →
- Python · Pandas
- phân tích, biến đổi
- →
- Báo cáo
- tự động hoá, biểu đồ
- Quy trình hằng ngày của Data Analyst & Data Scientist.

### Slide 3

- L11
- Python ↔ SQL
- Thư viện kết nối
- from sqlalchemy import  create_engine
- engine =
- create_engine (
- "postgresql://localhost/shop" )
- psycopg2 — driver cho PostgreSQL
- SQLAlchemy — đa CSDL, linh hoạt, dùng nhiều nhất

### Slide 4

- L11
- Python ↔ SQL
- pd.read_sql — query trả về DataFrame
- import pandas as  pd
- df = pd.
- read_sql (
- "SELECT region, sum(amount) FROM orders GROUP BY region" ,
- engine
- )
- Kết hợp sức mạnh của SQL với sự linh hoạt của Pandas.

### Slide 5

- L11
- Python ↔ SQL
- Bảo mật & best practice
- import  os
- pwd = os.
- getenv("DB_PASSWORD") # Parameterized — chống SQL injection pd.read_sql (
- "SELECT * FROM users WHERE id = %s" ,
- conn, params=[user_id]
- )
- Không hardcode mật khẩu — dùng biến môi trường
- Parameterized query chống SQL injection

### Slide 6

- L11
- Tóm tắt
- Tóm tắt & chuyển bài
- SQLAlchemy
- pd.read_sql
- Bảo mật
- Bài tiếp · Mini-Project
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_