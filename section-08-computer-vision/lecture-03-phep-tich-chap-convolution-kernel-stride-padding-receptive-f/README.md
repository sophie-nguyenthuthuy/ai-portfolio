# Section 8 · Lecture 3 — Phép tích chập (convolution) — kernel, stride, padding, receptive field

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Convolution — phát hiện đặc trưng

**🎨 Visual:** `[AI image]` Kernel trượt trên ảnh.
**🎤 Speaker note:** "Đây là phép toán làm nên cuộc cách mạng CV."

### Slide 2 — Kernel/filter

- Cửa sổ nhỏ trượt trên ảnh
- Phát hiện cạnh, góc, texture

**🎨 Visual:** `[Mermaid]` Kernel 3×3 trượt.
**🎤 Speaker note:** Mỗi kernel học 1 loại đặc trưng.

### Slide 3 — Stride & padding

- Stride: bước nhảy
- Padding: viền giữ kích thước

**🎨 Visual:** `[Mermaid]` Minh hoạ stride & padding.
**🎤 Speaker note:** Ảnh hưởng kích thước output.

### Slide 4 — Tính kích thước output

- Công thức từ input, kernel, stride, padding

**🎨 Visual:** `[Mermaid]` Công thức + ví dụ.
**🎤 Speaker note:** ⚠️ Hay hỏi: input 224, conv 3×3, stride 1, pad 1 → ?

### Slide 5 — Receptive field

- Vùng ảnh 1 nơ-ron "nhìn thấy"
- Lớp sâu → nhìn rộng hơn

**🎨 Visual:** `[Mermaid]` Receptive field mở rộng theo lớp.
**🎤 Speaker note:** Lớp đầu thấy cạnh, lớp sâu thấy vật thể.

### Slide 6 — Tóm tắt & chuyển bài

- kernel · stride/padding · receptive field
- Bài tiếp: kiến trúc CNN →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp convolution thành 1 mạng CNN."

---

_← [Về Section README](../README.md)_
