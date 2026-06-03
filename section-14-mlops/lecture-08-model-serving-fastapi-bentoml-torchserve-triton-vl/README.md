# Section 14 · Lecture 8 — Model serving — FastAPI, BentoML, TorchServe, Triton, vLLM

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 08
- SECTION 14 · LECTURE 08
- Model serving — FastAPI, BentoML, TorchServe, Triton, vLLM
- ~8 phút · 6 slides

### Slide 2

- L08 · MODEL SERVING
- Model serving là gì
- Bọc model thành API
- Nhận input → trả prediction
- Request
- →
- Model
- →
- Response

### Slide 3

- L08 · MODEL SERVING
- FastAPI
- Đơn giản, nhanh, phổ biến
- Lựa chọn số 1 cho người mới
- serve.py
- @app.post("/predict") def predict (x: Input):
- return {"y": model.predict(x.features)}

### Slide 4

- L08 · MODEL SERVING
- BentoML & TorchServe
- Chuyên cho ML serving
- Đóng gói + serve
- FASTAPI
- Tổng quát
- tự lắp
- BENTOML · TORCHSERVE
- Chuyên ML
- đóng gói sẵn

### Slide 5

- L08 · MODEL SERVING
- Triton & vLLM
- Triton: hiệu năng cao đa model
- vLLM: serve LLM tốc độ cao
- TRITON
- Đa model
- hiệu năng cao
- VLLM
- LLM
- throughput cao

### Slide 6

- L08 · MODEL SERVING — TÓM TẮT
- Tóm tắt
- FastAPI
- BentoML
- Triton
- vLLM
- BÀI TIẾP
- Docker & containerization
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_