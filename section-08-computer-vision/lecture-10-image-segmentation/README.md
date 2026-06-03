# Section 8 · Lecture 10 — Image Segmentation

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 10
- LECTURE 10 · ~9 PHÚT · 6 SLIDES
- Image Segmentation
- U-Net · Mask R-CNN · SAM — phân loại từng pixel, chi tiết nhất trong CV

### Slide 2

- L10 · CÁC LOẠI SEGMENTATION
- Khác nhau ở mức độ chi tiết
- SEMANTIC
- Phân vùng theo lớp
- Mọi "người" cùng một màu
- Không tách từng cá thể
- INSTANCE
- Phân vùng theo từng vật
- Người 1, người 2… tách riêng
- Chi tiết hơn

### Slide 3

- L10 · U-NET
- Encoder–decoder hình chữ U — chuẩn vàng ảnh y tế
- Encoder
- thu nhỏ
- ↓
- Bottleneck
- ↑
- Decoder
- phóng lại
- ┄ skip connection nối encoder ↔ decoder, giữ chi tiết không gian.

### Slide 4

- L10 · MASK R-CNN
- Detection + mask cho từng vật
- ảnh
- →
- Phát hiện
- bounding box
- +
- Mask từng vật
- vùng pixel chính xác
- Kết hợp detection và segmentation trong một model.

### Slide 5

- L10 · SEGMENT ANYTHING (SAM)
- Model nền tảng phân vùng "mọi thứ"
- Ít / không cần train thêm
- Chỉ cần click hoặc gợi ý là ra mask
- Bước nhảy lớn: segmentation không cần dữ liệu nhãn
- ảnh + 1 click
- →
- mask tức thì

### Slide 6

- L10 · TÓM TẮT
- Phân vùng tới từng pixel:
- semantic / instance
- U-Net
- Mask R-CNN
- SAM
- BÀI TIẾP
- →
- OCR — đọc chữ trong ảnh

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_