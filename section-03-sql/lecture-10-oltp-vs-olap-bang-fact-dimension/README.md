# Section 3 · Lecture 10 — OLTP vs OLAP — bảng Fact & Dimension

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 10
- ~8 phút · 6 slides
- OLTP vs OLAP — bảng Fact & Dimension
- Hiểu cách dữ liệu chảy trong doanh nghiệp.
- AI IMAGE
- Hai hệ thống: giao dịch vs phân tích
- S3 · Lecture 10

### Slide 2

- L10
- OLTP vs OLAP
- OLTP — xử lý giao dịch
- Nhiều giao dịch nhỏ, ghi nhanh
- Tối ưu cho ghi & cập nhật liên tục
- Ví dụ: hệ thống bán hàng, ngân hàng
- Mỗi đơn hàng, mỗi lần chuyển tiền là một giao dịch
- SƠ ĐỒ
- Nhiều giao dịch nhỏ liên tục

### Slide 3

- L10
- OLTP vs OLAP
- OLAP — phân tích
- Đọc nhiều, tổng hợp lượng lớn dữ liệu
- Tối ưu cho truy vấn báo cáo, ít cập nhật
- Ví dụ: data warehouse, hệ thống BI
- SƠ ĐỒ
- Truy vấn phân tích lớn theo lô

### Slide 4

- L10
- OLTP vs OLAP
- Fact & Dimension — star schema
- dim_time
- dim_product
- fact_sales
- doanh thu · số lượng
- dim_customer
- dim_store
- Fact = số đo · Dimension = ngữ cảnh. Nền tảng thiết kế data warehouse.

### Slide 5

- L10
- OLTP vs OLAP
- Star vs Snowflake schema
- STAR
- SNOWFLAKE
- Cấu trúc
- Dimension phẳng, đơn giản
- Dimension chuẩn hoá nhiều tầng
- Truy vấn
- Nhanh, ít JOIN
- Nhiều JOIN hơn
- Thực tế
- Phổ biến nhất
- Khi cần tiết kiệm lưu trữ

### Slide 6

- L10
- Tóm tắt
- Tóm tắt & chuyển bài
- OLTP vs OLAP
- Fact & Dimension
- Star schema
- Bài tiếp · Kết nối Python với SQL
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_