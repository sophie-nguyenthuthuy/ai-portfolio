# Section 8 · Lecture 2 — Tiền xử lý ảnh

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 02
- LECTURE 02 · ~8 PHÚT · 6 SLIDES
- Tiền xử lý ảnh
- resize · normalize · augment — ảnh thô không dùng được ngay

### Slide 2

- L02 · RESIZE & CROP
- Model cần input cố định kích thước
- Đưa mọi ảnh về cùng một kích thước
- Hầu hết CNN yêu cầu input cố định, ví dụ 224×224
- Resize co giãn, hoặc crop cắt vùng cần thiết
- ảnh gốc
- 1024 × 768
- →
- 224 × 224
- Kích thước khác nhau → một kích thước chuẩn

### Slide 3

- L02 · NORMALIZE
- Đưa pixel về thang nhỏ giúp train ổn định
- pixel
- 0 – 255
- giá trị thô, thang rộng
- →
- [ 0.0 – 1.0 ]
- chia 255, hoặc chuẩn hoá mean/std
- Nối lại feature scaling ở Section 5 — gradient mượt hơn, hội tụ nhanh hơn.

### Slide 4

- L02 · DATA AUGMENTATION
- Một ảnh → nhiều biến thể , tăng đa dạng dữ liệu
- Lật · xoay · đổi sáng · crop ngẫu nhiên
- Chống overfitting cực kỳ hiệu quả
- Model thấy nhiều "phiên bản" của cùng một vật
- gốc
- lật
- xoay
- sáng

### Slide 5

- L02 · KHI NÀO AUGMENT
- Chỉ augment trên train — không bao giờ trên test
- TẬP TRAIN
- Có augment ✓
- Lật, xoay, đổi màu thoải mái
- Tạo đa dạng, chống overfit
- TẬP TEST
- Không augment ✗
- Giữ nguyên ảnh thật
- Augment test = đánh giá sai lệch

### Slide 6

- L02 · TÓM TẮT
- Ba bước chuẩn bị ảnh:
- resize
- normalize
- augment
- BÀI TIẾP
- →
- Convolution — trái tim của Computer Vision

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_