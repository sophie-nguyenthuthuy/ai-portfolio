# Section 8 · Lecture 16 — Capstone 3 — CV thực chiến 🏆 **Capstone**

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 9

---

## Nội dung slide

### Slide 1

- 16
- 🏆 CAPSTONE 3 · ~16 PHÚT · 8 SLIDES
- Capstone 3 — CV thực chiến
- Dự án portfolio thứ 3 — chọn 1 trong 2 hướng (kèm screen recording)

### Slide 2

- L16 · CHỌN ĐỀ & BÀI TOÁN
- Chọn theo hứng thú & định hướng nghề
- HƯỚNG A
- Phân loại ảnh y tế
- Phân loại ảnh X-quang
- Image classification chuyên sâu
- HƯỚNG B
- OCR + trích thông tin hoá đơn
- Đọc & trích trường từ hoá đơn
- Document AI thực tế

### Slide 3

- L16 · CHUẨN BỊ DỮ LIỆU
- Áp dụng tiền xử lý + augmentation
- Tải dataset
- →
- Tiền xử lý
- →
- Augment
- →
- Train / Val / Test

### Slide 4

- L16 · XÂY MODEL
- Tận dụng pretrained — không train từ đầu
- HƯỚNG A
- Transfer learning
- ResNet / EfficientNet pretrained
- Thay lớp cuối, fine-tune
- HƯỚNG B
- PaddleOCR + KIE
- Pipeline OCR sẵn có
- Thêm bước trích trường

### Slide 5

- L16 · HUẤN LUYỆN & ĐÁNH GIÁ
- Theo dõi curve, phân tích lỗi
- Train & theo dõi loss / accuracy curve
- Error analysis: model sai ở đâu, vì sao
- Hướng A · accuracy
- ·
- Detection · mAP
- ·
- Hướng B · độ chính xác trích xuất

### Slide 6

- L16 · TỐI ƯU & NÉN
- Sẵn sàng deploy
- Model đã train
- →
- Export ONNX
- →
- Quantize
- nhỏ & nhanh
- Áp dụng đúng quantization vừa học ở Lecture 15.

### Slide 7

- L16 · DEPLOY WEB / API
- Điểm khiến CV nổi bật: có demo chạy được
- FastAPI cho backend
- Streamlit / Gradio cho giao diện
- Upload ảnh → trả về kết quả ngay
- ⬆️ Upload ảnh
- ↓
- Model inference
- ↓
- Kết quả trên web

### Slide 8

- L16 · TỔNG KẾT SECTION 8
- Computer Vision + Capstone 3 ✅
- 3/7
- Project portfolio thứ 3 hoàn thành
- Pixel → CNN → detection/segmentation → OCR → deploy → một sản phẩm CV chạy được.
- BÀI TIẾP
- →
- Section 9 — Natural Language Processing (NLP)

### Slide 9

- ✅ HOÀN THÀNH SECTION 8
- 16 / 16 lectures
- 16 lectures
- ~94 slides
- ~130 phút video
- Batch 6 · Computer Vision
- TIẾP THEO
- →
- Batch 7 · Section 9 (NLP) + Section 10 (Generative AI)

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_