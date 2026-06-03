# Section 14 · Lecture 9 — Containerization — Docker, Docker Compose, multi-stage build

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Docker & Containerization

**🎨 Visual:** `[AI image]` Container đóng gói app.
**🎤 Speaker note:** "Build một lần — chạy mọi nơi. Hết cảnh 'máy tôi chạy được'."

### Slide 2 — Vấn đề Docker giải

- "Trên máy tôi chạy được"
- Khác môi trường = khác kết quả

**🎨 Visual:** `[Mermaid]` Môi trường khác nhau.
**🎤 Speaker note:** Container đóng gói cả môi trường.

### Slide 3 — Image & container

- Image: bản thiết kế
- Container: thực thể chạy

**🎨 Visual:** `[Mermaid]` Image → container.
**🎤 Speaker note:** Nối lại class/object Section 2.

### Slide 4 — Dockerfile

- Công thức build image
- FROM, COPY, RUN, CMD

**🎨 Visual:** `[Screen]` Dockerfile cho FastAPI ML.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn hay yêu cầu viết Dockerfile.

### Slide 5 — Multi-stage & Compose

- Multi-stage: image nhỏ gọn
- Compose: nhiều service cùng lúc

**🎨 Visual:** `[Screen]` docker-compose.
**🎤 Speaker note:** Compose dựng cả stack (API + DB + vector DB).

### Slide 6 — Tóm tắt & chuyển bài

- image/container · Dockerfile · multi-stage · Compose
- Bài tiếp: Kubernetes →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta điều phối container ở quy mô lớn."

---

_← [Về Section README](../README.md)_
