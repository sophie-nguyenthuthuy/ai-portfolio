# Section 14 · Lecture 8 — Model serving — FastAPI, BentoML, TorchServe, Triton, vLLM

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Model Serving

**🎨 Visual:** `[AI image]` Model phục vụ qua API.
**🎤 Speaker note:** "Đưa model ra cho người/hệ thống khác dùng."

### Slide 2 — Model serving là gì

- Bọc model thành API
- Nhận input → trả prediction

**🎨 Visual:** `[Mermaid]` Request → model → response.
**🎤 Speaker note:** Cách model "ra đời thật".

### Slide 3 — FastAPI

- Đơn giản, nhanh, phổ biến
- Nối lại decorator Section 2

**🎨 Visual:** `[Screen]` FastAPI endpoint.
**🎤 Speaker note:** Lựa chọn số 1 cho người mới.

### Slide 4 — BentoML & TorchServe

- Chuyên cho ML serving
- Đóng gói + serve

**🎨 Visual:** `[Mermaid]` So sánh.
**🎤 Speaker note:** Tiện hơn FastAPI cho ML thuần.

### Slide 5 — Triton & vLLM

- Triton: hiệu năng cao đa model
- vLLM: serve LLM tốc độ cao

**🎨 Visual:** `[Mermaid]` Khi nào dùng.
**🎤 Speaker note:** vLLM cho LLM — nối lại Section 11.

### Slide 6 — Tóm tắt & chuyển bài

- FastAPI · BentoML · Triton · vLLM
- Bài tiếp: Docker →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta đóng gói để chạy ở mọi nơi."

---

_← [Về Section README](../README.md)_
