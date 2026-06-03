# Section 8 · Lecture 9 — Object Detection — YOLO (v8/v10), Faster R-CNN, DETR

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Object Detection

**🎨 Visual:** `[AI image]` Ảnh có bounding box quanh vật thể.
**🎤 Speaker note:** "Không chỉ 'ảnh có gì' mà 'vật ở đâu'."

### Slide 2 — Classification vs Detection

- Classification: nhãn cho cả ảnh
- Detection: vị trí + nhãn từng vật

**🎨 Visual:** `[Mermaid]` So sánh 2 bài toán.
**🎤 Speaker note:** Detection khó hơn, hữu dụng hơn.

### Slide 3 — Bounding box & IoU

- Hộp bao vật thể
- IoU đo độ khớp

**🎨 Visual:** `[Mermaid]` IoU = giao/hợp.
**🎤 Speaker note:** Nền của metric detection.

### Slide 4 — One-stage vs Two-stage

- One-stage (YOLO): nhanh
- Two-stage (Faster R-CNN): chính xác

**🎨 Visual:** `[Mermaid]` So sánh 2 hướng.
**🎤 Speaker note:** Trade-off tốc độ vs độ chính xác.

### Slide 5 — YOLO

- Chia lưới, dự đoán trực tiếp
- YOLOv8/v10: nhanh, mạnh, dễ dùng

**🎨 Visual:** `[Mermaid]` Lưới YOLO dự đoán.
**🎤 Speaker note:** Lựa chọn số 1 cho real-time.

### Slide 6 — DETR (Transformer)

- Detection bằng Transformer
- Không cần anchor

**🎨 Visual:** `[Mermaid]` DETR pipeline.
**🎤 Speaker note:** Hướng hiện đại, gọn về thiết kế.

### Slide 7 — Tóm tắt & chuyển bài

- bbox/IoU · YOLO · Faster R-CNN · DETR
- Bài tiếp: segmentation →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta phân vùng ảnh tới từng pixel."

---

_← [Về Section README](../README.md)_
