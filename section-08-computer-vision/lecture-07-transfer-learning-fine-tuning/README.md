# Section 8 · Lecture 7 — Transfer learning & fine-tuning

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 07
- LECTURE 07 · ~9 PHÚT · 6 SLIDES
- Transfer learning & fine-tuning
- Không ai train từ đầu — ta đứng trên vai người khổng lồ

### Slide 2

- L07 · VÌ SAO TRANSFER LEARNING
- Kỹ thuật quan trọng nhất trong CV thực tế
- Tiết kiệm dữ liệu, thời gian, GPU
- Tận dụng đặc trưng model đã học sẵn
- Model
- pretrained
- đã học trên triệu ảnh
- →
- Task
- mới
- dữ liệu của bạn

### Slide 3

- L07 · FEATURE EXTRACTION
- Đóng băng backbone, chỉ train lớp cuối
- Dùng khi dữ liệu ít
- Phần đã học giữ nguyên — train nhanh
- 🔒 Conv blocks (frozen)
- ↓
- 🔒 Conv blocks (frozen)
- ↓
- ⚡ FC mới (train)

### Slide 4

- L07 · FINE-TUNING
- Mở băng & train lại với learning rate nhỏ
- Dùng khi có nhiều dữ liệu hơn
- lr nhỏ để không phá hỏng đặc trưng cũ
- 🔓 Conv blocks (train, lr nhỏ)
- ↓
- 🔓 Conv blocks (train, lr nhỏ)
- ↓
- ⚡ FC mới (train)

### Slide 5

- L07 · QUY TRÌNH THỰC TẾ
- Vài dòng code, kết quả mạnh ngay
- import torchvision.models as models
- # 1 · Chọn model pretrained
- model = models.resnet50(weights="IMAGENET1K_V2")
- # 2 · Thay lớp cuối cho số lớp của bạn
- model.fc = nn.Linear(model.fc.in_features, 5)
- # 3 · Train như bình thường

### Slide 6

- L07 · TÓM TẮT
- Tái sử dụng tri thức:
- transfer
- feature extraction
- fine-tune
- BÀI TIẾP
- →
- Xây pipeline data augmentation chuyên nghiệp

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_