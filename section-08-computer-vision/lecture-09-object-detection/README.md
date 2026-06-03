# Section 8 · Lecture 9 — Object Detection

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- 09
- LECTURE 09 · ~10 PHÚT · 7 SLIDES
- Object Detection
- YOLO · Faster R-CNN · DETR — không chỉ "ảnh có gì" mà "vật ở đâu"

### Slide 2

- L09 · CLASSIFICATION VS DETECTION
- Từ "ảnh có gì" đến "vật nằm ở đâu"
- CLASSIFICATION
- Một nhãn cho cả ảnh
- "Đây là ảnh con mèo"
- Không biết vị trí
- DETECTION
- Vị trí + nhãn từng vật
- Hộp bao quanh từng vật thể
- Khó hơn, hữu dụng hơn

### Slide 3

- L09 · BOUNDING BOX & IOU
- IoU đo độ khớp giữa dự đoán & thực tế
- ━ thực tế ━ dự đoán
- IoU = giao / hợp
- 1.0 = trùng khít hoàn hảo
- Nền tảng của mọi metric detection

### Slide 4

- L09 · ONE-STAGE VS TWO-STAGE
- Trade-off tốc độ vs độ chính xác
- ONE-STAGE
- YOLO
- Dự đoán trực tiếp — rất nhanh
- Lý tưởng cho real-time
- TWO-STAGE
- Faster R-CNN
- Đề xuất vùng → phân loại
- Chính xác hơn, chậm hơn

### Slide 5

- L09 · YOLO
- Chia lưới, dự đoán trong một lần nhìn
- "You Only Look Once" — chia ảnh thành lưới ô
- YOLOv8 / v10: nhanh, mạnh, dễ dùng
- Lựa chọn số 1 cho ứng dụng real-time
- dog 0.94

### Slide 6

- L09 · DETR (TRANSFORMER)
- Detection bằng Transformer — không cần anchor
- ảnh
- →
- CNN backbone
- →
- Transformer
- →
- Tập hộp + nhãn
- thiết kế gọn, hiện đại

### Slide 7

- L09 · TÓM TẮT
- Phát hiện vật thể:
- bbox / IoU
- YOLO
- Faster R-CNN
- DETR
- BÀI TIẾP
- →
- Segmentation — phân vùng ảnh tới từng pixel

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_