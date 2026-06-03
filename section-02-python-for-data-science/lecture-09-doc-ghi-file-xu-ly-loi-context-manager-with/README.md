# Section 2 · Lecture 9 — Đọc/ghi file, xử lý lỗi & context manager (with)

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Làm việc với file & lỗi

**🎨 Visual:** `[AI image]` File + biểu tượng cảnh báo.
**🎤 Speaker note:** "Dữ liệu thật luôn nằm trong file — và luôn có lỗi."

### Slide 2 — Đọc/ghi file

- `open()`, `read()`, `write()`
- Chế độ: r, w, a

**🎨 Visual:** `[Screen]` Đọc file text.
**🎤 Speaker note:** Phân biệt w (ghi đè) vs a (ghi thêm).

### Slide 3 — Context manager (with)

- `with open(...) as f:`
- Tự đóng file an toàn

**🎨 Visual:** `[Screen]` So sánh có/không dùng with.
**🎤 Speaker note:** Luôn dùng `with` — tránh quên đóng file.

### Slide 4 — Xử lý lỗi: try/except

- `try / except / finally`
- Bắt lỗi, không cho chương trình crash

**🎨 Visual:** `[Mermaid]` Flowchart try-except.
**🎤 Speaker note:** Code production không được sập vì 1 lỗi nhỏ.

### Slide 5 — Các lỗi thường gặp

- FileNotFoundError, ValueError
- KeyError, TypeError

**🎨 Visual:** `[Screen]` Ví dụ bắt từng loại lỗi.
**🎤 Speaker note:** Đọc thông báo lỗi = kỹ năng debug số 1.

### Slide 6 — Tóm tắt & chuyển bài

- file · with · try/except
- Bài tiếp: Pandas Phần 1 →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta vào ngôi sao của Data Science — Pandas."

---

_← [Về Section README](../README.md)_
