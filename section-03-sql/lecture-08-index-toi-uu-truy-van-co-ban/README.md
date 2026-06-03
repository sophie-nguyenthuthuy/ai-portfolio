# Section 3 · Lecture 8 — Index & tối ưu truy vấn cơ bản

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 08
- ~8 phút · 6 slides
- Index & tối ưu truy vấn cơ bản
- Truy vấn chậm trên hàng triệu dòng — thường là do thiếu index.
- AI IMAGE
- Mục lục sách giúp tra cứu tức thì
- S3 · Lecture 8

### Slide 2

- L8
- Tối ưu truy vấn
- Index là gì — như mục lục của một cuốn sách
- Không index
- đọc từng dòng · full table scan
- vs
- Có index
- nhảy thẳng tới dòng cần tìm
- Index là cấu trúc giúp database tìm dòng mà không cần quét cả bảng.

### Slide 3

- L8
- Tối ưu truy vấn
- Đánh đổi của index
- LỢI
- CHI PHÍ
- Đọc (SELECT)
- Nhanh hơn rất nhiều
- —
- Ghi (INSERT/UPDATE)
- —
- Chậm hơn · phải cập nhật index
- Lưu trữ
- —
- Tốn thêm dung lượng ổ đĩa
- ⚠ Câu hỏi phỏng vấn: index có nhược điểm gì?

### Slide 4

- L8
- Tối ưu truy vấn
- Đọc execution plan với EXPLAIN
- EXPLAIN SELECT * FROM orders WHERE customer_id = 42; -- Seq Scan  → đang quét toàn bảng (chậm) -- Index Scan → đang dùng index (nhanh)
- Công cụ debug hiệu năng số 1 — phát hiện full scan.

### Slide 5

- L8
- Tối ưu truy vấn
- Mẹo tối ưu nhanh
- Tạo index cho cột hay dùng để lọc hoặc JOIN
- Tránh SELECT * — chỉ lấy cột cần thiết
- Tránh đặt hàm lên cột lọc (vd WHERE year(date)=2025) — làm index vô hiệu
- Vài mẹo đơn giản giải quyết 80% truy vấn chậm.

### Slide 6

- L8
- Tóm tắt
- Tóm tắt & chuyển bài
- Index
- Đánh đổi đọc/ghi
- EXPLAIN
- Bài tiếp · Procedure, view, trigger
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_