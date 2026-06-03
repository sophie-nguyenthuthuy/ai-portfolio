# Section 8 · Lecture 14 — Triển khai Edge

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 14
- LECTURE 14 · ~7 PHÚT · 5 SLIDES
- Triển khai Edge
- ONNX · TensorRT · mobile — model phải chạy được tại chỗ

### Slide 2

- L14 · VÌ SAO EDGE
- Không phải lúc nào cũng có cloud
- CLOUD
- Chạy trên server
- Mạnh, nhưng cần mạng
- Độ trễ cao, lo về riêng tư
- EDGE
- Chạy ngay trên thiết bị
- Độ trễ thấp · riêng tư · offline
- Camera an ninh, mobile

### Slide 3

- L14 · ONNX
- Train một nơi, chạy mọi nơi
- PyTorch
- →
- ONNX
- định dạng model chung
- →
- CPU / GPU
- Mobile
- Browser / Edge

### Slide 4

- L14 · TENSORRT & MOBILE
- Mỗi phần cứng có runtime tối ưu riêng
- GPU NVIDIA
- TensorRT
- Tăng tốc inference mạnh
- Cho server & Jetson edge
- ĐIỆN THOẠI
- TFLite / CoreML
- TFLite cho Android
- CoreML cho iOS

### Slide 5

- L14 · TÓM TẮT
- Đưa model ra thiết bị:
- edge
- ONNX
- TensorRT
- mobile
- BÀI TIẾP
- →
- Quantization & pruning — làm model nhỏ lại

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_