# Section 3 · Lecture 11 — Kết nối Python với SQL (SQLAlchemy, psycopg2)

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~8 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Python gặp SQL

**🎨 Visual:** `[AI image]` Python ↔ database.
**🎤 Speaker note:** "Đây là cầu nối thực tế: lấy dữ liệu từ DB vào Pandas."

### Slide 2 — Vì sao kết nối

- Truy vấn DB → phân tích bằng Pandas
- Tự động hoá báo cáo

**🎨 Visual:** `[Mermaid]` DB → Python → phân tích.
**🎤 Speaker note:** Quy trình hằng ngày của Data Analyst/Scientist.

### Slide 3 — Thư viện kết nối

- psycopg2 (PostgreSQL)
- SQLAlchemy (đa CSDL)

**🎨 Visual:** `[Screen]` Tạo connection.
**🎤 Speaker note:** SQLAlchemy linh hoạt, dùng nhiều nhất.

### Slide 4 — pd.read_sql

- Chạy SQL → trả về DataFrame
- `pd.read_sql(query, conn)`

**🎨 Visual:** `[Screen]` Query → DataFrame.
**🎤 Speaker note:** Kết hợp sức mạnh SQL + Pandas.

### Slide 5 — Bảo mật & best practice

- Tránh hardcode mật khẩu
- Parameterized query (chống SQL injection)

**🎨 Visual:** `[Screen]` Dùng biến môi trường.
**🎤 Speaker note:** Nhấn an toàn — quan trọng trong production.

### Slide 6 — Tóm tắt & chuyển bài

- SQLAlchemy · read_sql · bảo mật
- Bài tiếp: Mini-Project →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả vào 1 dự án SQL thật."

---

_← [Về Section README](../README.md)_
