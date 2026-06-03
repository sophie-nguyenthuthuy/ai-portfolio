# Section 8 · Lecture 6 — CNN hiện đại & ViT

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 06
- LECTURE 06 · ~9 PHÚT · 6 SLIDES
- CNN hiện đại & ViT
- EfficientNet · ConvNeXt · Vision Transformer — Transformer không chỉ cho text

### Slide 2

- L06 · EFFICIENTNET
- Cân bằng cả ba chiều — nhẹ, nhanh, chính xác
- Compound scaling: độ sâu · độ rộng · độ phân giải
- Rất phổ biến trong production
- độ sâu (depth)
- độ rộng (width)
- độ phân giải (resolution)

### Slide 3

- L06 · CONVNEXT
- CNN được "hiện đại hoá" theo ý tưởng Transformer
- Mượn thiết kế từ Transformer, vẫn là CNN
- Chứng minh CNN vẫn rất cạnh tranh
- large-kernel conv
- ↓
- LayerNorm
- ↓
- MLP (1×1 conv)

### Slide 4

- L06 · VISION TRANSFORMER (VIT)
- Cắt ảnh thành patch , xử lý như chuỗi từ
- →
- Chuỗi patch + vị trí
- →
- Transformer encoder
- attention
- →
- Nhãn
- Gặp lại attention chi tiết ở Section NLP.

### Slide 5

- L06 · KHI NÀO DÙNG CÁI NÀO
- Chọn theo lượng dữ liệu
- DỮ LIỆU LỚN
- ViT
- Phát huy khi có rất nhiều ảnh
- Mạnh ở quy mô lớn
- DỮ LIỆU VỪA · EDGE
- CNN / EfficientNet
- Hiệu quả với dữ liệu nhỏ–vừa
- Thực tế vẫn là lựa chọn an toàn

### Slide 6

- L06 · TÓM TẮT
- Bộ ba hiện đại:
- EfficientNet
- ConvNeXt
- ViT
- BÀI TIẾP
- →
- Transfer learning — tận dụng model đã train sẵn

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_