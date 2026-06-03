# Section 8 · Lecture 7 — Transfer learning & fine-tuning — quy trình thực tế

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Transfer Learning

**🎨 Visual:** `[AI image]` Model pretrained chuyển sang task mới.
**🎤 Speaker note:** "Không ai train từ đầu — ta đứng trên vai người khổng lồ."

### Slide 2 — Vì sao transfer learning

- Tiết kiệm dữ liệu, thời gian, GPU
- Tận dụng đặc trưng đã học

**🎨 Visual:** `[Mermaid]` Pretrained → fine-tune.
**🎤 Speaker note:** Kỹ thuật quan trọng nhất trong CV thực tế.

### Slide 3 — Feature extraction

- Đóng băng phần đã học
- Chỉ train lớp cuối

**🎨 Visual:** `[Mermaid]` Freeze backbone.
**🎤 Speaker note:** Dùng khi dữ liệu ít.

### Slide 4 — Fine-tuning

- Mở băng & train lại với lr nhỏ

**🎨 Visual:** `[Mermaid]` Unfreeze + lr thấp.
**🎤 Speaker note:** Dùng khi có nhiều dữ liệu hơn.

### Slide 5 — Quy trình thực tế

- Chọn model → thay lớp cuối → train
- torchvision pretrained

**🎨 Visual:** `[Screen]` Load ResNet pretrained.
**🎤 Speaker note:** Vài dòng code, kết quả mạnh ngay.

### Slide 6 — Tóm tắt & chuyển bài

- transfer · feature extraction · fine-tune
- Bài tiếp: augmentation nâng cao →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xây pipeline augmentation chuyên nghiệp."

---

_← [Về Section README](../README.md)_
