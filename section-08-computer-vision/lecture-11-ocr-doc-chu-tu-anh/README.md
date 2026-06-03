# Section 8 · Lecture 11 — OCR — đọc chữ từ ảnh

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 11
- LECTURE 11 · ~8 PHÚT · 6 SLIDES
- OCR — đọc chữ từ ảnh
- Tesseract · EasyOCR · PaddleOCR · KIE — hoá đơn, CMND, hợp đồng

### Slide 2

- L11 · OCR LÀ GÌ
- Hai bước: tìm chữ ở đâu , đọc chữ gì
- ảnh
- →
- Detect
- vùng chứa text
- →
- Recognize
- đọc ra ký tự
- Optical Character Recognition — nhận dạng ký tự quang học.

### Slide 3

- L11 · CÔNG CỤ OCR
- Chọn công cụ theo hỗ trợ tiếng Việt
- Tesseract
- Lâu đời, miễn phí, đa ngôn ngữ
- EasyOCR
- Dễ dùng, nhiều ngôn ngữ sẵn
- PaddleOCR
- Mạnh, hỗ trợ tốt dấu tiếng Việt

### Slide 4

- L11 · KIE — KEY INFORMATION EXTRACTION
- Không chỉ đọc, mà hiểu cấu trúc
- hoá đơn
- Tên cửa hàng
- "Cửa hàng ABC"
- ↓
- Số tiền
- "450.000 ₫"
- ↓
- Ngày
- "29/05/2026"
- Đây là phần tạo ra giá trị kinh doanh.

### Slide 5

- L11 · PIPELINE DOCUMENT AI
- Từ ảnh tài liệu đến dữ liệu có cấu trúc
- Detect
- →
- OCR
- →
- KIE
- →
- Output có cấu trúc
- JSON / database
- Liên hệ trực tiếp tới Capstone OCR hoá đơn.

### Slide 6

- L11 · TÓM TẮT
- Đọc & hiểu tài liệu:
- OCR
- PaddleOCR
- KIE
- Document AI
- BÀI TIẾP
- →
- Nhận diện khuôn mặt

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_