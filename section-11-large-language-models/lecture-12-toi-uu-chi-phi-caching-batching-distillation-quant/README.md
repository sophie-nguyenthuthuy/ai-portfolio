# Section 11 · Lecture 12 — Tối ưu chi phí — caching, batching, distillation, quantization

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 12
- SECTION 11 · LECTURE 12
- Tối ưu chi phí — caching, batching, distillation, quantization
- ~7 phút · 5 slides

### Slide 2

- L12 · TỐI ƯU CHI PHÍ
- Caching
- Lưu kết quả truy vấn lặp lại
- Tiết kiệm token & độ trễ
- Câu hỏi
- →
- Cache hit?
- →
- Trả ngay

### Slide 3

- L12 · TỐI ƯU CHI PHÍ
- Batching
- Gộp nhiều request
- Tăng throughput
- req · req · req
- →
- Batch
- →
- 1 lần xử lý

### Slide 4

- L12 · TỐI ƯU CHI PHÍ
- Distillation & quantization
- Distillation: model nhỏ học model lớn
- Quantization: giảm độ chính xác số
- DISTILLATION
- Model nhỏ học lớn
- nhẹ, nhanh hơn
- QUANTIZATION
- Giảm bit số
- FP16 → INT4

### Slide 5

- L12 · TỐI ƯU CHI PHÍ — TÓM TẮT
- Tóm tắt
- caching
- batching
- distillation
- quantization
- BÀI TIẾP
- An toàn LLM
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_