# Section 13 · Lecture 4 — LlamaIndex cho agent nặng truy xuất

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 13 · LECTURE 04
- LlamaIndex cho agent nặng truy xuất
- ~6 phút · 5 slides

### Slide 2

- L04 · LLAMAINDEX
- LlamaIndex là gì
- Framework data cho LLM/RAG
- Kết nối nhiều nguồn dữ liệu
- Nguồn dữ liệu
- →
- Index
- →
- Query

### Slide 3

- L04 · LLAMAINDEX
- Data connector
- Nạp PDF, DB, API, web
- Tổng hợp dữ liệu đa nguồn
- TÀI LIỆU
- PDF · Word
- file nội bộ
- HỆ THỐNG
- DB · API
- dữ liệu sống
- WEB
- Trang web
- crawl & nạp

### Slide 4

- L04 · LLAMAINDEX
- Query engine & agent
- Truy vấn dữ liệu thông minh
- LangChain vs LlamaIndex — bổ trợ nhau
- query.py
- from llama_index import  VectorStoreIndex
- index = VectorStoreIndex. from_documents (docs)
- engine = index. as_query_engine ()
- engine. query("Doanh thu Q3 là bao nhiêu?") # → trả lời kèm trích dẫn nguồn

### Slide 5

- L04 · LLAMAINDEX — TÓM TẮT
- Tóm tắt
- LlamaIndex
- connector
- query engine
- BÀI TIẾP
- Multi-agent systems
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_