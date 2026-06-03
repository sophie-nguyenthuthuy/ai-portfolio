# Section 8 · Lecture 8 — Pipeline data augmentation

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 08
- LECTURE 08 · ~7 PHÚT · 5 SLIDES
- Pipeline data augmentation
- Albumentations · torchvision — tăng dữ liệu miễn phí

### Slide 2

- L08 · TORCHVISION TRANSFORMS
- Compose thành một pipeline — đủ cho hầu hết bài toán
- from torchvision import transforms
- train_tf = transforms.Compose([
- transforms.Resize((224, 224)),
- transforms.RandomHorizontalFlip(),
- transforms.RandomRotation(15),
- transforms.ToTensor(),
- transforms.Normalize(mean, std),
- ])

### Slide 3

- L08 · ALBUMENTATIONS
- Nhanh, mạnh — chuẩn cho detection & segmentation
- Rất nhiều phép biến đổi mạnh, tốc độ cao
- Hỗ trợ đồng bộ cả bounding box & mask
- import albumentations as A
- tf = A.Compose([
- A.RandomBrightnessContrast(),
- A.ShiftScaleRotate(),
- A.CoarseDropout(),
- ], bbox_params=...)

### Slide 4

- L08 · AUGMENT MẠNH VS NHẸ
- Augment phải phù hợp domain
- CÂN BẰNG
- Augment hợp lý
- Tăng đa dạng, chống overfit
- Giữ ảnh vẫn "thật"
- CẨN THẬN
- Augment quá mạnh
- Bóp méo đặc trưng quan trọng
- Có thể làm model tệ đi

### Slide 5

- L08 · TÓM TẮT
- Tăng dữ liệu đúng cách:
- torchvision
- Albumentations
- cân bằng
- BÀI TIẾP
- →
- Object Detection — không chỉ "ảnh có gì" mà "vật ở đâu"

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_