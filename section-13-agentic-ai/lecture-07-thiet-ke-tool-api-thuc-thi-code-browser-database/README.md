# Section 13 · Lecture 7 — Thiết kế tool — API, thực thi code, browser, database

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 07
- SECTION 13 · LECTURE 07
- Thiết kế tool — API, thực thi code, browser, database
- ~7 phút · 5 slides

### Slide 2

- L07 · THIẾT KẾ TOOL
- Các loại tool
- API call, code execution
- Browser, database query
- API
- Gọi dịch vụ
- CODE
- Thực thi code
- BROWSER
- Duyệt web
- DATABASE
- Truy vấn DB

### Slide 3

- L07 · THIẾT KẾ TOOL
- Mô tả tool tốt
- Tên rõ, mô tả rõ, tham số rõ
- Mô tả tốt = agent dùng đúng tool
- tool.py
- @tool def search_docs (query: str) -> str:
- """Tìm tài liệu nội bộ theo từ khoá."""     return db.search(query)

### Slide 4

- L07 · THIẾT KẾ TOOL
- Xử lý lỗi tool
- Tool fail → agent xử lý thế nào
- Retry, fallback
- Gọi tool
- →
- Lỗi?
- →
- Retry / fallback

### Slide 5

- L07 · THIẾT KẾ TOOL — TÓM TẮT
- Tóm tắt
- loại tool
- mô tả tool
- xử lý lỗi
- BÀI TIẾP
- Hệ thống memory
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_