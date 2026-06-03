# Section 2 · Lecture 5 — List vs Tuple — khi nào dùng cái nào

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- List vs Tuple

**🎨 Visual:** `[AI image]` Hai hộp: 1 mở (list) 1 khoá (tuple).
**🎤 Speaker note:** "Giống nhau mà khác nhau ở 1 điểm cốt lõi."

### Slide 2 — List

- Có thể thay đổi (mutable)
- `[1, 2, 3]`
- Thêm/xoá/sửa phần tử

**🎨 Visual:** `[Screen]` Thao tác append/remove.
**🎤 Speaker note:** Dùng khi dữ liệu sẽ thay đổi.

### Slide 3 — Thao tác List quan trọng

- append, insert, remove, pop
- sort, reverse, slicing

**🎨 Visual:** `[Screen]` Slicing `lst[1:4]`.
**🎤 Speaker note:** Slicing dùng cực nhiều trong data.

### Slide 4 — Tuple

- Không thể thay đổi (immutable)
- `(1, 2, 3)`
- Nhanh hơn, an toàn hơn

**🎨 Visual:** `[Screen]` Thử sửa tuple → báo lỗi.
**🎤 Speaker note:** Dùng cho dữ liệu cố định (toạ độ, hằng số).

### Slide 5 — Packing & unpacking

- `a, b = (1, 2)`
- Trả nhiều giá trị từ hàm

**🎨 Visual:** `[Screen]` Unpacking ví dụ.
**🎤 Speaker note:** Mẹo Pythonic hay dùng.

### Slide 6 — Tóm tắt & chuyển bài

- List = đổi được · Tuple = cố định
- Bài tiếp: Dict & Set →

**🎨 Visual:** `[Mermaid]` Bảng so sánh List vs Tuple.
**🎤 Speaker note:** "Hai cấu trúc tiếp theo là xương sống của feature engineering."

---

_← [Về Section README](../README.md)_
