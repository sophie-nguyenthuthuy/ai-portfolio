# Section 11 · Lecture 10 — Đánh giá LLM — perplexity, MMLU, HumanEval, benchmark riêng

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 10
- SECTION 11 · LECTURE 10
- Đánh giá LLM — perplexity, MMLU, HumanEval, benchmark riêng
- ~7 phút · 5 slides

### Slide 2

- L10 · ĐÁNH GIÁ LLM
- Perplexity
- Đo độ "bất ngờ" của model
- Thấp = dự đoán tốt
- Perplexity ↓ = dự đoán tốt ↑
- chỉ số nội tại — không nói hết chất lượng

### Slide 3

- L10 · ĐÁNH GIÁ LLM
- Benchmark chuẩn
- Tham khảo nhưng có thể bị "luyện đề"
- MMLU
- Kiến thức tổng quát
- 57 lĩnh vực
- HUMANEVAL
- Sinh code
- pass@k

### Slide 4

- L10 · ĐÁNH GIÁ LLM
- Benchmark riêng
- Tự xây tập test cho bài toán của bạn
- Quan trọng nhất
- eval.py
- # model thắng MMLU chưa chắc hợp việc bạn for q, gold in  my_eval_set:
- pred = model(q)
- score +=  grade(pred, gold)

### Slide 5

- L10 · ĐÁNH GIÁ LLM — TÓM TẮT
- Tóm tắt
- perplexity
- MMLU / HumanEval
- eval riêng
- BÀI TIẾP
- Hallucination
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_