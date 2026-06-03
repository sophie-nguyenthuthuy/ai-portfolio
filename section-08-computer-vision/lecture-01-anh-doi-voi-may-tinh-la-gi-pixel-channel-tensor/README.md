# Section 8 · Lecture 1 — Ảnh đối với máy tính là gì? Pixel, channel, tensor

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Máy tính "nhìn" ảnh thế nào

**🎨 Visual:** `[AI image]` Ảnh phóng to thành lưới pixel.
**🎤 Speaker note:** "Với máy, ảnh chỉ là một mảng số."

### Slide 2 — Pixel & độ phân giải

- Ảnh = lưới điểm ảnh (pixel)
- Mỗi pixel có giá trị 0-255

**🎨 Visual:** `[Mermaid]` Lưới pixel + giá trị.
**🎤 Speaker note:** Độ phân giải = số pixel.

### Slide 3 — Channel màu

- Ảnh xám: 1 channel
- Ảnh màu: 3 channel (RGB)

**🎨 Visual:** `[Mermaid]` Tách R, G, B.
**🎤 Speaker note:** RGB chồng lên tạo màu.

### Slide 4 — Ảnh = tensor

- Shape: (Height × Width × Channel)
- Nối lại tensor Section 4

**🎨 Visual:** `[Mermaid]` Tensor ảnh 3 chiều.
**🎤 Speaker note:** PyTorch dùng (C×H×W).

### Slide 5 — Tóm tắt & chuyển bài

- pixel · channel · tensor
- Bài tiếp: tiền xử lý ảnh →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta chuẩn bị ảnh trước khi đưa vào model."

---

_← [Về Section README](../README.md)_
