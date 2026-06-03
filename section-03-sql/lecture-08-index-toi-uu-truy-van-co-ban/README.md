# Section 3 · Lecture 8 — Index & tối ưu truy vấn cơ bản

_Phần của: **Section 3: SQL — Cơ sở dữ liệu & truy vấn**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Index — tăng tốc truy vấn

**🎨 Visual:** `[AI image]` Mục lục sách / kính lúp nhanh.
**🎤 Speaker note:** "Truy vấn chậm trên triệu dòng = thiếu index."

### Slide 2 — Index là gì

- Cấu trúc giúp tìm dòng nhanh
- Giống mục lục sách

**🎨 Visual:** `[Mermaid]` Quét toàn bảng vs dùng index.
**🎤 Speaker note:** Không index = đọc từng dòng (full scan).

### Slide 3 — Đánh đổi của index

- SELECT nhanh hơn
- INSERT/UPDATE chậm hơn + tốn ổ

**🎨 Visual:** `[Mermaid]` Cân bằng đọc vs ghi.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn: index có nhược điểm gì?

### Slide 4 — Đọc execution plan

- `EXPLAIN` xem cách DB chạy
- Phát hiện full scan

**🎨 Visual:** `[Screen]` EXPLAIN một query.
**🎤 Speaker note:** Công cụ debug hiệu năng số 1.

### Slide 5 — Mẹo tối ưu nhanh

- Index cột hay lọc/JOIN
- Tránh SELECT *, tránh hàm trên cột lọc

**🎨 Visual:** `[Mermaid]` Checklist tối ưu.
**🎤 Speaker note:** Vài mẹo đơn giản giải quyết 80% query chậm.

### Slide 6 — Tóm tắt & chuyển bài

- index · đánh đổi · EXPLAIN
- Bài tiếp: procedure, view, trigger →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tự động hoá logic trong database."

---

_← [Về Section README](../README.md)_
