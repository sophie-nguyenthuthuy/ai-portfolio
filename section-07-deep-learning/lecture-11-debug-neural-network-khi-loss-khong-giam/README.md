# Section 7 · Lecture 11 — Debug neural network — khi loss không giảm

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Debug Neural Network

**🎨 Visual:** `[AI image]` Loss curve phẳng lì.
**🎤 Speaker note:** "Kỹ năng phân biệt người mới với người có kinh nghiệm."

### Slide 2 — Loss không giảm

- Learning rate sai
- Quên scale dữ liệu

**🎨 Visual:** `[Mermaid]` Loss phẳng → nguyên nhân.
**🎤 Speaker note:** Kiểm tra lr & dữ liệu đầu tiên.

### Slide 3 — Loss = NaN

- lr quá lớn, exploding gradient
- Gradient clipping

**🎨 Visual:** `[Screen]` clip_grad_norm.
**🎤 Speaker note:** NaN gần như luôn do lr/gradient.

### Slide 4 — Overfit train, dở test

- Thêm regularization
- Thêm dữ liệu / augmentation

**🎨 Visual:** `[Mermaid]` Khoảng cách train-val.
**🎤 Speaker note:** Nối lại bài regularization.

### Slide 5 — Quy trình debug

- Overfit 1 batch nhỏ trước
- Kiểm tra shape, dữ liệu

**🎨 Visual:** `[Mermaid]` Checklist debug.
**🎤 Speaker note:** Mẹo: nếu không overfit nổi 1 batch → code có bug.

### Slide 6 — Tóm tắt & chuyển bài

- loss phẳng/NaN · overfit · checklist
- Bài tiếp: Mini-Project →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả: xây mạng từ đầu rồi bằng PyTorch."

---

_← [Về Section README](../README.md)_
