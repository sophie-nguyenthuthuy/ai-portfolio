# Section 12 · Lecture 3 — Vector database — FAISS, ChromaDB, Pinecone, Qdrant, Weaviate, Milvus

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Vector Database

**🎨 Visual:** `[AI image]` Kho vector khổng lồ.
**🎤 Speaker note:** "Tìm vector gần nhất trong hàng triệu — cực nhanh."

### Slide 2 — Vì sao cần vector DB

- Tìm nearest neighbor nhanh
- Quy mô lớn, lọc metadata

**🎨 Visual:** `[Mermaid]` Brute force vs ANN.
**🎤 Speaker note:** ANN: gần đúng nhưng cực nhanh.

### Slide 3 — FAISS & ChromaDB

- FAISS: thư viện, nhanh, local
- Chroma: dễ dùng cho học

**🎨 Visual:** `[Screen]` Index FAISS.
**🎤 Speaker note:** Bắt đầu với Chroma cho đơn giản.

### Slide 4 — Pinecone, Qdrant, Weaviate, Milvus

- Vector DB chuyên dụng, production
- Quản lý, mở rộng, lọc

**🎨 Visual:** `[Mermaid]` So sánh.
**🎤 Speaker note:** Cho hệ thống lớn, nhiều người dùng.

### Slide 5 — Chọn vector DB nào

- Học: Chroma/FAISS
- Production: Qdrant/Pinecone

**🎨 Visual:** `[Mermaid]` Bảng quyết định.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn: 100M vector chọn gì?

### Slide 6 — Tóm tắt & chuyển bài

- vector DB · ANN · cách chọn
- Bài tiếp: chunking →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học cách cắt tài liệu cho đúng."

---

_← [Về Section README](../README.md)_
