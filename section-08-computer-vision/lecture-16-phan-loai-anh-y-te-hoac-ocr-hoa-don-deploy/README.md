# Section 8 · Lecture 16 — 🏆 Capstone 3 — Phân loại ảnh y tế HOẶC OCR hoá đơn + deploy

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 8 · ~16 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 🏆 Capstone 3: CV thực chiến

**🎨 Visual:** `[AI image]` Ảnh y tế / hoá đơn + giao diện web.
**🎤 Speaker note:** "Dự án portfolio thứ 3 — chọn 1 trong 2 hướng."

### Slide 2 — Chọn đề & bài toán

- A: Phân loại ảnh y tế (X-quang)
- B: OCR + trích thông tin hoá đơn

**🎨 Visual:** `[Mermaid]` 2 lựa chọn đề.
**🎤 Speaker note:** Chọn theo hứng thú / định hướng nghề.

### Slide 3 — Chuẩn bị dữ liệu

- Tải dataset, tiền xử lý, augment

**🎨 Visual:** `[Screen]` Data pipeline.
**🎤 Speaker note:** Áp dụng tiền xử lý + augmentation.

### Slide 4 — Xây model

- A: Transfer learning ResNet/EfficientNet
- B: PaddleOCR + KIE pipeline

**🎨 Visual:** `[Screen]` Build model theo đề.
**🎤 Speaker note:** Tận dụng pretrained, không train từ đầu.

### Slide 5 — Huấn luyện & đánh giá

- Train, theo dõi curve
- Metric: accuracy / mAP / độ chính xác trích xuất

**🎨 Visual:** `[Screen]` Training + metric.
**🎤 Speaker note:** Phân tích lỗi (error analysis).

### Slide 6 — Tối ưu & nén

- Chuyển ONNX, quantize
- Sẵn sàng deploy

**🎨 Visual:** `[Screen]` Export ONNX.
**🎤 Speaker note:** Áp dụng quantization đã học.

### Slide 7 — Deploy web/API

- FastAPI + giao diện Streamlit/Gradio
- Upload ảnh → kết quả

**🎨 Visual:** `[Screen]` Demo web app.
**🎤 Speaker note:** Đây là điểm khiến CV nổi bật — có demo chạy được.

### Slide 8 — Tổng kết Section 8

- Computer Vision + Capstone 3 ✅
- Bài tiếp: Section 9 — NLP →

**🎨 Visual:** `[AI image]` Badge "Project 3/7 Done".
**🎤 Speaker note:** "3 dự án rồi! Giờ ta chuyển sang xử lý ngôn ngữ."

---

_← [Về Section README](../README.md)_
