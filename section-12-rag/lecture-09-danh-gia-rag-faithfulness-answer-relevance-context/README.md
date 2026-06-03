# Section 12 · Lecture 9 — Đánh giá RAG — faithfulness, answer relevance, context precision (RAGAS)

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 09
- SECTION 12 · LECTURE 09
- Đánh giá RAG — faithfulness, answer relevance, context precision (RAGAS)
- ~7 phút · 5 slides

### Slide 2

- L09 · ĐÁNH GIÁ RAG
- Vì sao khó đánh giá
- Nhiều khâu: retrieve + generate
- Lỗi nằm ở đâu?
- RETRIEVE
- Tìm sai tài liệu?
- context precision
- GENERATE
- Trả lời sai?
- faithfulness

### Slide 3

- L09 · ĐÁNH GIÁ RAG
- Các chỉ số chính
- Faithfulness chống hallucination
- FAITHFULNESS
- Bám tài liệu
- không bịa
- ANSWER RELEVANCE
- Đúng câu hỏi
- sát ý
- CONTEXT PRECISION
- Tài liệu liên quan
- ít nhiễu

### Slide 4

- L09 · ĐÁNH GIÁ RAG
- RAGAS
- Framework đánh giá RAG tự động
- Dùng LLM chấm RAG
- ragas.py
- from ragas import  evaluate
- evaluate(dataset, metrics=[faithfulness, answer_relevancy]) # faithfulness 0.92 · relevance 0.88

### Slide 5

- L09 · ĐÁNH GIÁ RAG — TÓM TẮT
- Tóm tắt
- faithfulness
- relevance
- context precision
- RAGAS
- BÀI TIẾP
- RAG trong production
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_