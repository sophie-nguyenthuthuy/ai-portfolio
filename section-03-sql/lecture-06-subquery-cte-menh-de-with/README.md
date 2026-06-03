# Section 3 · Lecture 6 — Subquery & CTE (mệnh đề WITH)

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Subquery & CTE

**🎨 Visual:** `[AI image]` Truy vấn lồng truy vấn.
**🎤 Speaker note:** "Khi 1 câu SELECT không đủ, ta lồng chúng."

### Slide 2 — Subquery

- Truy vấn bên trong truy vấn
- Trong WHERE, FROM, SELECT

**🎨 Visual:** `[Screen]` Subquery trong WHERE.
**🎤 Speaker note:** Ví dụ: khách chi tiêu trên trung bình.

### Slide 3 — Subquery tương quan

- Phụ thuộc dòng của truy vấn ngoài
- Chạy lặp từng dòng

**🎨 Visual:** `[Screen]` Correlated subquery.
**🎤 Speaker note:** Mạnh nhưng chậm — lưu ý hiệu năng.

### Slide 4 — CTE (WITH)

- Đặt tên cho truy vấn con
- `WITH temp AS (...)`

**🎨 Visual:** `[Screen]` CTE thay subquery.
**🎤 Speaker note:** Dễ đọc hơn subquery lồng nhiều tầng.

### Slide 5 — CTE đệ quy

- Truy vấn tự gọi lại
- Cho dữ liệu phân cấp/cây

**🎨 Visual:** `[Mermaid]` Cây phân cấp.
**🎤 Speaker note:** Dùng cho sơ đồ tổ chức, danh mục lồng nhau.

### Slide 6 — Tóm tắt & chuyển bài

- subquery · CTE · đệ quy
- Bài tiếp: window function →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới phần phân biệt junior với senior — window function."

---

_← [Về Section README](../README.md)_
