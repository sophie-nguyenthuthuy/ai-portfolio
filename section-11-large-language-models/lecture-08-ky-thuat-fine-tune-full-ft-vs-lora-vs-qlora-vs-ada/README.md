# Section 11 · Lecture 8 — Kỹ thuật fine-tune — full FT vs LoRA vs QLoRA vs adapter

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 08
- SECTION 11 · LECTURE 08
- Kỹ thuật fine-tune — full FT vs LoRA vs QLoRA vs adapter
- ~9 phút · 6 slides

### Slide 2

- L08 · FINE-TUNING
- Khi nào fine-tune
- Phong cách / định dạng đặc thù
- ⚠️ Cân nhắc RAG trước
- PROMPT
- Rẻ, nhanh
- thử trước tiên
- RAG
- Kiến thức cập nhật
- grounding tài liệu
- FINE-TUNE
- Phong cách / kỹ năng
- khi prompt không đủ

### Slide 3

- L08 · FINE-TUNING
- Full fine-tuning
- Train lại toàn bộ tham số
- Tốn kém, cần nhiều GPU
- Cập nhật mọi trọng số
- hiếm khi cần với người học

### Slide 4

- L08 · FINE-TUNING
- LoRA
- Chỉ train ma trận nhỏ thêm vào
- Tiết kiệm tài nguyên rất lớn
- W + A·B
- A·B = ma trận hạng thấp — chỉ train phần này

### Slide 5

- L08 · FINE-TUNING
- QLoRA & Adapter
- QLoRA = LoRA + quantization
- Fine-tune model lớn trên 1 GPU
- Model 4-bit
- →
- + LoRA
- →
- Fit Colab

### Slide 6

- L08 · FINE-TUNING — TÓM TẮT
- Tóm tắt
- full FT
- LoRA
- QLoRA
- adapter
- BÀI TIẾP
- Chạy LLM local
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_