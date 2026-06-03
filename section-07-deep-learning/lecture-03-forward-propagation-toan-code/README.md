# Section 7 · Lecture 3 — Forward propagation — toán + code

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Lan truyền xuôi (Forward)

**🎨 Visual:** `[AI image]` Dữ liệu chảy trái → phải.
**🎤 Speaker note:** "Cách mạng tạo ra dự đoán."

### Slide 2 — Một lớp tính gì

- z = W·x + b
- a = activation(z)

**🎨 Visual:** `[Mermaid]` 1 lớp tính toán.
**🎤 Speaker note:** Nối lại nhân ma trận Section 4.

### Slide 3 — Xếp chồng nhiều lớp

- Output lớp này = input lớp sau

**🎨 Visual:** `[Mermaid]` Chuỗi lớp.
**🎤 Speaker note:** Cứ thế tới lớp output.

### Slide 4 — Code forward bằng NumPy

- Nhân ma trận + activation

**🎨 Visual:** `[Screen]` Forward pass NumPy.
**🎤 Speaker note:** Thấy rõ neural network chỉ là toán ma trận.

### Slide 5 — Tóm tắt & chuyển bài

- z=Wx+b · activation · xếp lớp
- Bài tiếp: hàm mất mát →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta đo mạng dự đoán sai bao nhiêu."

---

_← [Về Section README](../README.md)_
