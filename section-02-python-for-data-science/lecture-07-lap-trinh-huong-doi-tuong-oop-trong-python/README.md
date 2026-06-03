# Section 2 · Lecture 7 — Lập trình hướng đối tượng (OOP) trong Python

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- OOP — tư duy đối tượng

**🎨 Visual:** `[AI image]` Khuôn (class) → nhiều sản phẩm (object).
**🎤 Speaker note:** "Cách code lớn được tổ chức gọn gàng, tái dùng."

### Slide 2 — Class & Object

- Class = bản thiết kế
- Object = thực thể từ class

**🎨 Visual:** `[Mermaid]` Class KhachHang → object an, binh.
**🎤 Speaker note:** Ví von: class = khuôn bánh, object = từng cái bánh.

### Slide 3 — Thuộc tính & __init__

- `__init__` = hàm khởi tạo
- `self` = chính đối tượng đó

**🎨 Visual:** `[Screen]` Viết class với __init__.
**🎤 Speaker note:** `self` luôn là tham số đầu tiên.

### Slide 4 — Method (phương thức)

- Hàm bên trong class
- Hành vi của đối tượng

**🎨 Visual:** `[Screen]` Thêm method vào class.
**🎤 Speaker note:** Method = động từ của đối tượng.

### Slide 5 — Kế thừa (Inheritance)

- Class con kế thừa class cha
- Tái sử dụng + mở rộng

**🎨 Visual:** `[Mermaid]` Cha → con kế thừa.
**🎤 Speaker note:** Gặp lại khi dùng nn.Module trong PyTorch.

### Slide 6 — Vì sao dân Data cần OOP

- PyTorch, scikit-learn đều dùng class
- Hiểu OOP = đọc được code thư viện

**🎨 Visual:** `[Screen]` Ví dụ class model PyTorch (preview).
**🎤 Speaker note:** Không cần master, nhưng phải đọc hiểu.

### Slide 7 — Tóm tắt & chuyển bài

- class · object · method · kế thừa
- Bài tiếp: module & environment →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tổ chức code thành nhiều file."

---

_← [Về Section README](../README.md)_
