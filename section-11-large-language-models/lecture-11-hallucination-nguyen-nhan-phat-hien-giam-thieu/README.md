# Section 11 · Lecture 11 — Hallucination — nguyên nhân, phát hiện, giảm thiểu

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 11
- SECTION 11 · LECTURE 11
- Hallucination — nguyên nhân, phát hiện, giảm thiểu
- ~8 phút · 6 slides

### Slide 2

- L11 · HALLUCINATION
- Hallucination là gì
- Tạo thông tin sai một cách tự tin
- Nguy hiểm vì nghe rất thuyết phục
- Câu trả lời sai trông rất thật
- tự tin nhưng không có thật

### Slide 3

- L11 · HALLUCINATION
- Nguyên nhân
- Model đoán token, không "biết"
- Thiếu kiến thức / ngữ cảnh
- Đoán token
- →
- Thiếu ngữ cảnh
- →
- Bịa thông tin

### Slide 4

- L11 · HALLUCINATION
- Giảm thiểu
- Grounding bằng RAG
- Yêu cầu trích dẫn nguồn · hạ temperature
- Grounding bằng RAG
- ↓
- Yêu cầu trích dẫn nguồn
- ↓
- Hạ temperature

### Slide 5

- L11 · HALLUCINATION
- Phát hiện
- Kiểm tra chéo nguồn
- Self-consistency
- Sinh nhiều câu trả lời
- →
- So khớp
- →
- Lệch = nghi ngờ

### Slide 6

- L11 · HALLUCINATION — TÓM TẮT
- Tóm tắt
- hallucination
- nguyên nhân
- giảm thiểu
- BÀI TIẾP
- Tối ưu chi phí LLM
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_