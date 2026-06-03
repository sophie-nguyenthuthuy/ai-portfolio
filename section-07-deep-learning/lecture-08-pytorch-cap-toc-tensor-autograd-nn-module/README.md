# Section 7 · Lecture 8 — PyTorch cấp tốc — tensor, autograd, nn.Module

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 7 · ~10 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- PyTorch cấp tốc

**🎨 Visual:** `[AI image]` Logo PyTorch.
**🎤 Speaker note:** "Framework deep learning phổ biến nhất hiện nay."

### Slide 2 — Tensor

- Giống NumPy array + chạy GPU

**🎨 Visual:** `[Screen]` Tạo tensor, chuyển GPU.
**🎤 Speaker note:** Nối lại tensor Section 4.

### Slide 3 — Autograd

- Tự tính gradient
- `.backward()`

**🎨 Visual:** `[Screen]` requires_grad + backward.
**🎤 Speaker note:** Khỏi tự code backprop — autograd lo.

### Slide 4 — nn.Module

- Định nghĩa model bằng class
- Nối lại OOP Section 2

**🎨 Visual:** `[Screen]` Class model kế thừa nn.Module.
**🎤 Speaker note:** Đây là lý do ta học OOP từ đầu.

### Slide 5 — Vòng lặp huấn luyện

- forward → loss → backward → step

**🎨 Visual:** `[Screen]` Training loop.
**🎤 Speaker note:** Mẫu này lặp lại cho mọi model PyTorch.

### Slide 6 — Optimizer & loss có sẵn

- torch.optim, torch.nn loss

**🎨 Visual:** `[Screen]` Adam + CrossEntropyLoss.
**🎤 Speaker note:** Mọi thứ đã học có sẵn trong thư viện.

### Slide 7 — Tóm tắt & chuyển bài

- tensor · autograd · nn.Module · train loop
- Bài tiếp: TensorFlow/Keras →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ xem framework còn lại — Keras."

---

_← [Về Section README](../README.md)_
