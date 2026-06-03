# Section 12 · Lecture 3 — Vector database — FAISS, ChromaDB, Pinecone, Qdrant, Weaviate, Milvus

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 03
- SECTION 12 · LECTURE 03
- Vector database — FAISS, ChromaDB, Pinecone, Qdrant, Weaviate, Milvus
- ~8 phút · 6 slides

### Slide 2

- L03 · VECTOR DB
- Vì sao cần vector DB
- Tìm nearest neighbor nhanh
- Quy mô lớn, lọc metadata
- BRUTE FORCE
- So mọi vector
- chính xác
- rất chậm
- ANN
- Gần đúng
- cực nhanh
- quy mô triệu

### Slide 3

- L03 · VECTOR DB
- FAISS & ChromaDB
- FAISS: thư viện nhanh, local
- Chroma: dễ dùng cho học
- index.py
- import  chromadb
- col = chromadb.Client().create_collection("docs" )
- col. add(ids=ids, embeddings=vecs, documents=docs)

### Slide 4

- L03 · VECTOR DB
- Vector DB chuyên dụng
- Production: quản lý, mở rộng, lọc
- Pinecone
- →
- Qdrant
- →
- Weaviate
- →
- Milvus

### Slide 5

- L03 · VECTOR DB
- Chọn vector DB nào
- ⚠️ Phỏng vấn: 100M vector chọn gì?
- HỌC
- Đơn giản
- Chroma · FAISS
- PRODUCTION
- Mở rộng lớn
- Qdrant · Pinecone

### Slide 6

- L03 · VECTOR DB — TÓM TẮT
- Tóm tắt
- vector DB
- ANN
- cách chọn
- BÀI TIẾP
- Document chunking
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_