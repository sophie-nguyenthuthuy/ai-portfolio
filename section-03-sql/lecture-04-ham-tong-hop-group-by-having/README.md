# Section 3 · Lecture 4 — Hàm tổng hợp — GROUP BY & HAVING

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 04
- ~9 phút · 6 slides
- Hàm tổng hợp — GROUP BY & HAVING
- Đây là nơi SQL trả lời các câu hỏi kinh doanh.
- AI IMAGE
- Nhiều dòng dữ liệu gộp thành một con số
- S3 · Lecture 4

### Slide 2

- L4
- Tổng hợp & gom nhóm
- Hàm tổng hợp — gộp nhiều dòng thành một giá trị
- COUNT — đếm số dòng
- SUM · AVG — tổng & trung bình
- MIN · MAX — nhỏ nhất & lớn nhất
- SELECT   count(*)      AS  so_don,
- sum(amount)  AS  doanh_thu,
- avg(amount)  AS trung_binh FROM orders;

### Slide 3

- L4
- Tổng hợp & gom nhóm
- GROUP BY — gom nhóm trước khi tổng hợp
- Dữ liệu thô
- mọi đơn hàng
- →
- Gom theo vùng
- Bắc · Trung · Nam
- →
- Tính tổng mỗi nhóm
- doanh thu từng vùng
- SELECT region, sum(amount) FROM orders GROUP BY region;

### Slide 4

- L4
- Tổng hợp & gom nhóm
- HAVING vs WHERE — lọc trước hay sau khi gom nhóm
- WHERE
- lọc dòng · trước nhóm
- →
- GROUP BY
- gom nhóm
- →
- HAVING
- lọc nhóm · sau nhóm
- ⚠ Câu hỏi phỏng vấn kinh điển: phân biệt WHERE và HAVING.

### Slide 5

- L4
- Tổng hợp & gom nhóm
- Ví dụ thực tế — vùng có doanh thu lớn
- -- Vùng có tổng doanh thu trên 1 tỷ đồng SELECT region, sum(amount) AS doanh_thu FROM orders GROUP BY region HAVING sum(amount) > 1000000000;
- WHERE không dùng được với
- sum()
- — phải dùng HAVING sau khi gom nhóm.

### Slide 6

- L4
- Tóm tắt
- Tóm tắt & chuyển bài
- Hàm tổng hợp
- GROUP BY
- HAVING vs WHERE
- Bài tiếp · JOIN — nối nhiều bảng
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_