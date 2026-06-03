# Section 8 · Lecture 8 — Pipeline data augmentation (Albumentations, torchvision)

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Pipeline Augmentation

**🎨 Visual:** `[AI image]` 1 ảnh → nhiều biến thể.
**🎤 Speaker note:** "Augmentation tốt = tăng dữ liệu miễn phí."

### Slide 2 — torchvision transforms

- Resize, flip, rotate, normalize
- Compose thành pipeline

**🎨 Visual:** `[Screen]` transforms.Compose.
**🎤 Speaker note:** Đủ cho hầu hết bài toán.

### Slide 3 — Albumentations

- Nhanh, nhiều phép biến đổi mạnh
- Hỗ trợ bbox/mask

**🎨 Visual:** `[Screen]` Albumentations pipeline.
**🎤 Speaker note:** Chuẩn cho detection/segmentation.

### Slide 4 — Augment mạnh vs nhẹ

- So sánh hiệu năng
- Augment phù hợp domain

**🎨 Visual:** `[Mermaid]` No aug vs strong aug.
**🎤 Speaker note:** Augment quá mạnh có thể hại — cân bằng.

### Slide 5 — Tóm tắt & chuyển bài

- torchvision · Albumentations · cân bằng
- Bài tiếp: image classification →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta train bài toán phân loại ảnh hoàn chỉnh."

---

_← [Về Section README](../README.md)_
