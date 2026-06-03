# Section 12 · Lecture 2 — Embeddings — vector dày đặc, similarity, chọn model

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 02
- SECTION 12 · LECTURE 02
- Embeddings — vector dày đặc, similarity, chọn model
- ~8 phút · 6 slides

### Slide 2

- L02 · EMBEDDINGS
- Embedding là gì
- Vector mang ngữ nghĩa
- Nối lại Section 4 & 9
- “tài liệu”
- →
- [ 0.12, −0.55, 0.83, … ]

### Slide 3

- L02 · EMBEDDINGS
- Đo độ tương đồng
- Cosine similarity
- Vector gần = nội dung liên quan
- cos(q, d) → [−1, 1]
- càng gần 1 = càng liên quan

### Slide 4

- L02 · EMBEDDINGS
- Chọn embedding model
- Lưu ý chất lượng với tiếng Việt
- OPENAI
- text-embedding-3
- chất lượng cao
- trả phí
- BGE
- open · mạnh
- self-host
- E5
- đa ngôn ngữ
- hỗ trợ VN

### Slide 5

- L02 · EMBEDDINGS
- Tạo embedding
- Văn bản → vector qua model
- Vài dòng với sentence-transformers
- embed.py
- from sentence_transformers import  SentenceTransformer
- m =  SentenceTransformer("BAAI/bge-m3" )
- vecs = m. encode(docs)
- # → (n, 1024)

### Slide 6

- L02 · EMBEDDINGS — TÓM TẮT
- Tóm tắt
- embedding
- cosine
- chọn model
- BÀI TIẾP
- Vector database
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_