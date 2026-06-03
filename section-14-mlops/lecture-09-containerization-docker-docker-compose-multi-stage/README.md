# Section 14 · Lecture 9 — Containerization — Docker, Docker Compose, multi-stage build

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 09
- SECTION 14 · LECTURE 09
- Containerization — Docker, Docker Compose, multi-stage build
- ~9 phút · 6 slides

### Slide 2

- L09 · DOCKER
- Vấn đề Docker giải
- "Trên máy tôi chạy được"
- Khác môi trường = khác kết quả
- "Máy tôi chạy được" → chạy mọi nơi
- container đóng gói cả môi trường

### Slide 3

- L09 · DOCKER
- Image & container
- Image: bản thiết kế
- Container: thực thể chạy
- BẢN THIẾT KẾ
- Image
- →
- THỰC THỂ CHẠY
- Container

### Slide 4

- L09 · DOCKER
- Dockerfile
- Công thức build image
- FROM, COPY, RUN, CMD
- Dockerfile
- FROM python:3.11-slim COPY . /app RUN pip install -r requirements.txt CMD ["uvicorn", "serve:app"]

### Slide 5

- L09 · DOCKER
- Multi-stage & Compose
- Multi-stage: image nhỏ gọn
- Compose: nhiều service cùng lúc
- API
- →
- + DB
- →
- + Vector DB

### Slide 6

- L09 · DOCKER — TÓM TẮT
- Tóm tắt
- image / container
- Dockerfile
- multi-stage
- Compose
- BÀI TIẾP
- Kubernetes cho ML
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_