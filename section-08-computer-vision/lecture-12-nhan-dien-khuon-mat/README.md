# Section 8 · Lecture 12 — Nhận diện khuôn mặt

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 12
- LECTURE 12 · ~7 PHÚT · 5 SLIDES
- Nhận diện khuôn mặt
- FaceNet & ArcFace — từ mở khoá điện thoại tới chấm công

### Slide 2

- L12 · BÀI TOÁN
- Hai câu hỏi khác nhau
- VERIFICATION
- Có phải cùng một người?
- So 1–1: mặt này = mặt kia?
- VD: mở khoá điện thoại
- IDENTIFICATION
- Đây là ai?
- So 1–N: tìm trong cơ sở dữ liệu
- VD: chấm công, an ninh

### Slide 3

- L12 · FACE EMBEDDING
- Biến khuôn mặt thành một vector
- khuôn mặt
- →
- Model embedding
- →
- [ 0.12, −0.84, … ]
- vector đặc trưng
- So sánh hai mặt = đo khoảng cách hai vector — nối lại cosine similarity ở Section 4.

### Slide 4

- L12 · FACENET & ARCFACE
- Học embedding phân biệt tốt
- Cùng người → vector gần nhau
- Khác người → vector xa nhau
- ArcFace dùng biên độ góc để tách lớp rõ hơn
- Các cụm tách biệt trong không gian embedding

### Slide 5

- L12 · TÓM TẮT
- Nhận diện khuôn mặt:
- verification / identification
- embedding
- ArcFace
- BÀI TIẾP
- →
- Vision đa phương thức — nối ảnh với ngôn ngữ

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_