# Section 7 · Lecture 6 — Optimizer — SGD, Momentum, Adam, AdamW

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Optimizer — cách mạng học nhanh

**🎨 Visual:** `[AI image]` Đường đi xuống dốc khác nhau.
**🎤 Speaker note:** "Cùng gradient, optimizer khác = tốc độ học khác."

### Slide 2 — SGD

- Gradient descent trên từng batch

**🎨 Visual:** `[Mermaid]` Đường SGD gập ghềnh.
**🎤 Speaker note:** Nối lại gradient descent Section 4.

### Slide 3 — Momentum

- Tích luỹ "quán tính"
- Vượt local minima dễ hơn

**🎨 Visual:** `[Mermaid]` Bóng lăn có đà.
**🎤 Speaker note:** Nhanh hơn, mượt hơn SGD thuần.

### Slide 4 — Adam

- Tự điều chỉnh learning rate
- Mặc định phổ biến nhất

**🎨 Visual:** `[Mermaid]` Adam hội tụ nhanh.
**🎤 Speaker note:** Lựa chọn an toàn cho hầu hết bài toán.

### Slide 5 — AdamW

- Adam + weight decay đúng cách
- Chuẩn cho Transformer/LLM

**🎨 Visual:** `[Mermaid]` AdamW.
**🎤 Speaker note:** Gặp lại khi train LLM.

### Slide 6 — Tóm tắt & chuyển bài

- SGD · Momentum · Adam · AdamW
- Bài tiếp: regularization →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta chống overfitting cho mạng."

---

_← [Về Section README](../README.md)_
