# Section 2 · Lecture 4 — Hàm, scope, lambda & decorator (nhập môn)

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Đóng gói & tái sử dụng code

**🎨 Visual:** `[AI image]` Hộp đen input → output.
**🎤 Speaker note:** "Hàm = công thức bạn viết một lần, dùng mãi."

### Slide 2 — Định nghĩa hàm

- `def ten_ham(thamso):`
- `return` trả kết quả

**🎨 Visual:** `[Screen]` Viết hàm đầu tiên.
**🎤 Speaker note:** Tham số (parameter) vs đối số (argument).

### Slide 3 — Tham số mặc định & *args/**kwargs

- Giá trị mặc định
- Số lượng tham số linh hoạt

**🎨 Visual:** `[Screen]` Ví dụ default + *args.
**🎤 Speaker note:** Hữu ích khi hàm cần linh hoạt.

### Slide 4 — Scope: cục bộ vs toàn cục

- Biến local sống trong hàm
- Biến global sống toàn chương trình

**🎨 Visual:** `[Mermaid]` Vòng tròn scope lồng nhau.
**🎤 Speaker note:** Lỗi scope là bug phổ biến của người mới.

### Slide 5 — Lambda (hàm ẩn danh)

- Hàm 1 dòng: `lambda x: x*2`
- Dùng với map, filter, sort

**🎨 Visual:** `[Screen]` lambda trong sorted().
**🎤 Speaker note:** Gọn cho hàm nhỏ dùng 1 lần.

### Slide 6 — Decorator (nhập môn)

- Hàm bọc hàm — thêm tính năng
- `@decorator`

**🎨 Visual:** `[Mermaid]` Hàm gốc được "bọc" thêm lớp.
**🎤 Speaker note:** Chỉ giới thiệu ý tưởng; gặp lại ở FastAPI sau.

### Slide 7 — Tóm tắt & chuyển bài

- def · scope · lambda · decorator
- Bài tiếp: List vs Tuple →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học cách chứa nhiều dữ liệu."

---

_← [Về Section README](../README.md)_
