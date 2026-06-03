# Section 3 · Lecture 7 — Window function — ROW_NUMBER, RANK, LAG, LEAD

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE 07
- ~11 phút · 7 slides
- Window function — ROW_NUMBER, RANK, LAG, LEAD
- Biết phần này, bạn vượt 80% người học SQL.
- AI IMAGE
- Cửa sổ trượt trên một bảng dữ liệu
- S3 · Lecture 7

### Slide 2

- L7
- Window function
- Window function là gì
- GROUP BY — GỘP MẤT DÒNG
- 3 dòng → 1
- Bắc · 9.8M
- WINDOW — GIỮ NGUYÊN DÒNG
- 3 dòng → 3 (thêm cột)
- Bắc · 3.1M · tổng 9.8M
- Bắc · 2.5M · tổng 9.8M
- Bắc · 4.2M · tổng 9.8M

### Slide 3

- L7
- Window function
- OVER & PARTITION BY — chia cửa sổ theo nhóm
- SELECT  name, region, amount,
- sum(amount) OVER (PARTITION BY region) AS tong_vung FROM orders;
- PARTITION BY giống GROUP BY — nhưng
- giữ nguyên
- mọi dòng gốc.

### Slide 4

- L7
- Window function
- ROW_NUMBER · RANK · DENSE_RANK
- ĐIỂM
- ROW_NUMBER
- RANK
- DENSE_RANK
- 95
- 1
- 1
- 1
- 95
- 2
- 1
- 1
- 88
- 3
- 3
- 2
- Khác nhau khi có giá trị trùng — dùng để lấy
- Top N mỗi nhóm
- .

### Slide 5

- L7
- Window function
- LAG & LEAD — so với kỳ trước / kỳ sau
- -- % tăng trưởng so tháng trước SELECT  month, revenue,
- lag(revenue) OVER  (
- ORDER BY  month
- )
- AS thang_truoc FROM monthly_sales;
- LAG lấy giá trị dòng trước, LEAD dòng sau
- Cốt lõi cho phân tích chuỗi thời gian bằng SQL

### Slide 6

- L7
- Window function
- Running total — tổng luỹ kế
- SELECT  date, amount,
- sum(amount) OVER (ORDER BY date) AS luy_ke FROM orders;
- Cộng dồn theo thứ tự — dùng cho biểu đồ tích luỹ.

### Slide 7

- L7
- Tóm tắt
- Tóm tắt & chuyển bài
- OVER · PARTITION BY
- ROW_NUMBER · RANK
- LAG · LEAD
- Running total
- Bài tiếp · Index & tối ưu truy vấn
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_