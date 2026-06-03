# Section 2 · Lecture 3 — Vòng lặp — for, while, comprehension, generator

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tự động hoá việc lặp đi lặp lại

**🎨 Visual:** `[AI image]` Vòng tròn lặp / băng chuyền.
**🎤 Speaker note:** "Máy tính giỏi nhất ở việc lặp — đừng làm thủ công."

### Slide 2 — Vòng lặp for

- Lặp qua list, range, chuỗi
- `for item in collection:`

**🎨 Visual:** `[Screen]` for lặp qua list.
**🎤 Speaker note:** Dùng khi biết trước số lần lặp / có tập để duyệt.

### Slide 3 — Vòng lặp while

- Lặp khi điều kiện còn đúng
- Cẩn thận vòng lặp vô hạn

**🎨 Visual:** `[Mermaid]` Flowchart while.
**🎤 Speaker note:** Dùng khi không biết trước số lần lặp.

### Slide 4 — break & continue

- `break`: thoát vòng lặp
- `continue`: bỏ qua lượt hiện tại

**🎨 Visual:** `[Screen]` Ví dụ break/continue.
**🎤 Speaker note:** Điều khiển luồng lặp linh hoạt.

### Slide 5 — List comprehension

- Viết vòng lặp gọn trong 1 dòng
- `[x**2 for x in arr if x > 0]`

**🎨 Visual:** `[Screen]` So sánh for thường vs comprehension.
**🎤 Speaker note:** Pythonic, nhanh — dùng cực nhiều trong data.

### Slide 6 — Generator

- Sinh giá trị lười (lazy), tiết kiệm bộ nhớ
- `yield` thay vì `return`

**🎨 Visual:** `[Mermaid]` So sánh list (giữ hết) vs generator (sinh dần).
**🎤 Speaker note:** Quan trọng khi xử lý dữ liệu lớn.

### Slide 7 — Tóm tắt & chuyển bài

- for · while · comprehension · generator
- Bài tiếp: hàm & module →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta đóng gói code thành hàm dùng lại."

---

_← [Về Section README](../README.md)_
