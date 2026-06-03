# Section 12 · Lecture 4 — Chunking — cố định, ngữ nghĩa, phân cấp

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 12 · LECTURE 04
- Chunking — cố định, ngữ nghĩa, phân cấp
- ~7 phút · 5 slides

### Slide 2

- L04 · CHUNKING
- Vì sao chunk
- Tài liệu dài quá context
- Chunk = đơn vị tìm kiếm
- Tài liệu dài
- →
- Cắt chunk
- →
- Đoạn nhỏ

### Slide 3

- L04 · CHUNKING
- Cố định vs ngữ nghĩa
- Semantic giữ ngữ cảnh tốt hơn
- FIXED
- Cắt theo số token
- đơn giản
- dễ cắt đứt ý
- SEMANTIC
- Cắt theo nghĩa
- giữ trọn ý

### Slide 4

- L04 · CHUNKING
- Overlap & phân cấp
- Chồng lấn giữ ngữ cảnh
- Parent-child chunk
- …cuối chunk A
- →
- overlap
- →
- đầu chunk B…

### Slide 5

- L04 · CHUNKING — TÓM TẮT
- Tóm tắt
- fixed / semantic
- overlap
- phân cấp
- BÀI TIẾP
- Pipeline RAG cơ bản
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_