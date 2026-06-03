# Section 8 · Lecture 5 — CNN kinh điển

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 05
- LECTURE 05 · ~9 PHÚT · 6 SLIDES
- CNN kinh điển
- LeNet · AlexNet · VGG · ResNet — hiểu lịch sử để hiểu thiết kế hiện đại

### Slide 2

- L05 · LENET & ALEXNET
- Hai cột mốc khởi đầu
- 1998
- LeNet
- Nhận dạng chữ số viết tay
- CNN đầu tiên thực dụng
- 2012
- AlexNet
- Thắng ImageNet vang dội
- Khởi đầu kỷ nguyên Deep Learning

### Slide 3

- L05 · VGG
- Sâu hơn, dùng kernel 3×3 đều đặn
- Xếp chồng nhiều lớp conv 3×3
- Đơn giản & đều — nhưng rất nặng
- Số tham số lớn, tốn bộ nhớ và tính toán
- Nhiều lớp 3×3 xếp chồng đều đặn

### Slide 4

- L05 · VẤN ĐỀ MẠNG SÂU
- Càng sâu lại càng khó train
- Mạng vừa
- train tốt ✓
- →
- Mạng rất sâu
- loss lại tệ hơn ✗
- →
- Vanishing gradient
- gradient tan biến khi lan ngược
- Thêm lớp không còn giúp ích — chính vấn đề này dẫn tới ResNet.

### Slide 5

- L05 · RESNET & SKIP CONNECTION
- "Đường tắt" giúp train mạng rất sâu
- skip connection: + x
- x
- →
- F(x) : conv → conv
- khối học phần dư (residual)
- →
- ⊕
- →
- out = F(x)+x
- Gradient chảy thẳng qua "đường tắt" — giải quyết vanishing gradient.

### Slide 6

- L05 · TÓM TẮT
- Dòng chảy lịch sử CNN:
- LeNet
- AlexNet
- VGG
- ResNet
- BÀI TIẾP
- →
- CNN hiện đại & Vision Transformer — cái gì đang thống trị 2026

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_