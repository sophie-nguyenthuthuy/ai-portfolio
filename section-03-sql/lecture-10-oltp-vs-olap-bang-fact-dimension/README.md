# Section 3 · Lecture 10 — OLTP vs OLAP — bảng Fact & Dimension

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- OLTP vs OLAP

**🎨 Visual:** `[AI image]` Hai hệ thống: giao dịch vs phân tích.
**🎤 Speaker note:** "Hiểu cái này = hiểu cách dữ liệu chảy trong doanh nghiệp."

### Slide 2 — OLTP

- Xử lý giao dịch (ghi nhanh)
- Vd: hệ thống bán hàng, ngân hàng

**🎨 Visual:** `[Mermaid]` Nhiều giao dịch nhỏ.
**🎤 Speaker note:** Tối ưu cho ghi/cập nhật.

### Slide 3 — OLAP

- Phân tích (đọc nhiều, tổng hợp)
- Vd: data warehouse, BI

**🎨 Visual:** `[Mermaid]` Truy vấn phân tích lớn.
**🎤 Speaker note:** Tối ưu cho đọc & báo cáo.

### Slide 4 — Fact & Dimension

- Fact: số đo (doanh thu, số lượng)
- Dimension: ngữ cảnh (thời gian, sản phẩm)

**🎨 Visual:** `[Mermaid]` Star schema: fact ở giữa.
**🎤 Speaker note:** Nền tảng thiết kế data warehouse.

### Slide 5 — Star vs Snowflake schema

- Star: đơn giản, nhanh
- Snowflake: chuẩn hoá hơn

**🎨 Visual:** `[Mermaid]` So sánh 2 schema.
**🎤 Speaker note:** Star phổ biến nhất trong thực tế.

### Slide 6 — Tóm tắt & chuyển bài

- OLTP vs OLAP · fact/dimension · star schema
- Bài tiếp: kết nối Python ↔ SQL →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta đưa dữ liệu SQL vào Python để phân tích."

---

_← [Về Section README](../README.md)_
