# Section 12 · Lecture 11 — Capstone 5 — Chatbot hỏi-đáp tài liệu nội bộ cho SME Việt Nam

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 9

---

## Nội dung slide

### Slide 1

- 11
- SECTION 12 · LECTURE 11
- Capstone 5 — Chatbot hỏi-đáp tài liệu nội bộ cho SME Việt Nam
- CAPSTONE 5
- ~16 phút · 8 slides

### Slide 2

- L11 · CAPSTONE 5
- Bài toán
- SME có nhiều tài liệu nội bộ
- Nhân viên cần hỏi-đáp nhanh
- HIỆN TẠI
- Tìm thủ công
- chậm, dễ sai
- RAG CHATBOT
- Hỏi là có
- trả lời kèm nguồn

### Slide 3

- L11 · CAPSTONE 5
- Ingest tài liệu
- PDF/Word → chunk → embed → vector DB
- Lưu ý tài liệu tiếng Việt
- ingest.py
- docs = load("*.pdf" )
- chunks =  split(docs, size=512, overlap=64 )
- db. add(embed(chunks))

### Slide 4

- L11 · CAPSTONE 5
- Xây retrieve pipeline
- Hybrid search + reranker
- Áp dụng kỹ thuật đã học
- Câu hỏi
- →
- Hybrid
- →
- Rerank
- →
- Top chunks

### Slide 5

- L11 · CAPSTONE 5
- Generate có trích dẫn
- LLM trả lời + nguồn
- Grounding chống hallucination
- chat.py
- ctx = retrieve (question)
- answer = llm( f"Dựa trên: {ctx}\nTrả lời: {question}") # → câu trả lời + [nguồn]

### Slide 6

- L11 · CAPSTONE 5
- Đánh giá bằng RAGAS
- Faithfulness, answer relevance
- Đo để chứng minh chất lượng
- SCREEN
- RAGAS report: faithfulness · relevance · context precision theo từng câu hỏi

### Slide 7

- L11 · CAPSTONE 5
- Deploy web UI
- FastAPI + Streamlit / Gradio
- Upload tài liệu → hỏi
- UI
- Web chatbot: ô upload tài liệu, khung chat, câu trả lời kèm trích dẫn nguồn

### Slide 8

- ✓
- Hoàn thành Section 12
- 11 / 11 lectures · Capstone 5 ✓ · 155 / 198 lectures
- BÀI TIẾP
- Section 13 — Agentic AI
- →

### Slide 9

- MASTERING AI · LỘ TRÌNH
- Tiến độ tổng — 155 / 198 lectures
- BATCH
- SECTION
- LECTURES
- TRẠNG THÁI
- Batch 1
- S1
- 6
- ✓ Hoàn thành
- Batch 2
- S2 · Python
- 18
- ✓ Hoàn thành
- Batch 3
- S3 + S4
- 26
- ✓ Hoàn thành
- Batch 4
- S5 · ML
- 20
- ✓ Hoàn thành
- Batch 5
- S6 + S7
- 21
- ✓ Hoàn thành
- Batch 6
- S8 · CV
- 16
- ✓ Hoàn thành
- Batch 7
- S9 + S10
- 23
- ✓ Hoàn thành
- Batch 8
- S11 LLMs + S12 RAG
- 25
- ✓ Batch này
- Batch 9
- S13 + S14
- 27
- ⏳ Tiếp theo
- Batch 10
- S15 + S16
- 16
- —

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_