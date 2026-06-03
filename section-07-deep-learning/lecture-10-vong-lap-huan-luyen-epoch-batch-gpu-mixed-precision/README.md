# Section 7 · Lecture 10 — Vòng lặp huấn luyện — epoch, batch, GPU, mixed precision

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Huấn luyện thực tế

**🎨 Visual:** `[AI image]` GPU + biểu đồ loss giảm.
**🎤 Speaker note:** "Những khái niệm bạn gặp mỗi lần train."

### Slide 2 — Epoch vs Batch

- Epoch: 1 lượt toàn dữ liệu
- Batch: chia nhỏ để train

**🎨 Visual:** `[Mermaid]` Epoch chứa nhiều batch.
**🎤 Speaker note:** Batch size ảnh hưởng tốc độ & bộ nhớ.

### Slide 3 — GPU

- Song song hoá phép tính ma trận
- Nhanh gấp nhiều lần CPU

**🎨 Visual:** `[Mermaid]` CPU vs GPU.
**🎤 Speaker note:** Dùng Colab GPU miễn phí.

### Slide 4 — Mixed precision

- Dùng float16 tăng tốc, tiết kiệm bộ nhớ

**🎨 Visual:** `[Screen]` autocast.
**🎤 Speaker note:** Mẹo train nhanh hơn trên GPU hiện đại.

### Slide 5 — Tóm tắt & chuyển bài

- epoch/batch · GPU · mixed precision
- Bài tiếp: debug neural network →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ học cách sửa khi mạng không chịu học."

---

_← [Về Section README](../README.md)_
