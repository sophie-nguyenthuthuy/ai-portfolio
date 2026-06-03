# Section 7 · Lecture 5 — Backpropagation — quy tắc chuỗi

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Backpropagation

**🎨 Visual:** `[AI image]` Gradient chảy ngược phải → trái.
**🎤 Speaker note:** "Thuật toán làm cho deep learning khả thi."

### Slide 2 — Ý tưởng

- Tính loss → truyền lỗi ngược
- Cập nhật trọng số

**🎨 Visual:** `[Mermaid]` Forward rồi backward.
**🎤 Speaker note:** Mạng học bằng cách "đổ lỗi" ngược về.

### Slide 3 — Quy tắc chuỗi

- Đạo hàm hàm hợp
- Nhân gradient qua các lớp

**🎨 Visual:** `[Mermaid]` Chain rule qua lớp.
**🎤 Speaker note:** Nối lại đạo hàm Section 4.

### Slide 4 — Computational graph

- Biểu diễn phép tính thành đồ thị
- Tự động tính gradient

**🎨 Visual:** `[Mermaid]` Đồ thị tính toán.
**🎤 Speaker note:** Nền của autograd trong PyTorch.

### Slide 5 — Code backprop đơn giản

- Tự cài cho mạng 2 lớp

**🎨 Visual:** `[Screen]` Backprop NumPy.
**🎤 Speaker note:** Làm 1 lần bằng tay để hiểu sâu.

### Slide 6 — Tóm tắt & chuyển bài

- truyền lỗi ngược · chain rule · graph
- Bài tiếp: optimizer →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta chọn cách cập nhật trọng số."

---

_← [Về Section README](../README.md)_
