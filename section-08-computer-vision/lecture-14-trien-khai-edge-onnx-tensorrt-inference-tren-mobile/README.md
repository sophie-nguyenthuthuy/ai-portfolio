# Section 8 · Lecture 14 — Triển khai edge — ONNX, TensorRT, inference trên mobile

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Triển khai Edge

**🎨 Visual:** `[AI image]` Model chạy trên điện thoại/camera.
**🎤 Speaker note:** "Không phải lúc nào cũng có cloud — model phải chạy tại chỗ."

### Slide 2 — Vì sao edge

- Độ trễ thấp, riêng tư, offline

**🎨 Visual:** `[Mermaid]` Cloud vs edge.
**🎤 Speaker note:** Camera an ninh, mobile cần edge.

### Slide 3 — ONNX

- Định dạng model chung
- Chạy trên nhiều nền tảng

**🎨 Visual:** `[Mermaid]` PyTorch → ONNX → nhiều runtime.
**🎤 Speaker note:** "Train một nơi, chạy mọi nơi."

### Slide 4 — TensorRT & mobile

- Tăng tốc inference trên GPU NVIDIA
- TFLite/CoreML cho mobile

**🎨 Visual:** `[Mermaid]` Tối ưu theo phần cứng.
**🎤 Speaker note:** Mỗi phần cứng có runtime tối ưu riêng.

### Slide 5 — Tóm tắt & chuyển bài

- edge · ONNX · TensorRT · mobile
- Bài tiếp: quantization & pruning →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta làm model nhỏ lại để chạy nhanh."

---

_← [Về Section README](../README.md)_
