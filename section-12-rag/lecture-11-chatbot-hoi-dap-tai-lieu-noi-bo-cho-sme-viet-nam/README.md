# Section 12 · Lecture 11 — 🏆 Capstone 5 — Chatbot hỏi-đáp tài liệu nội bộ cho SME Việt Nam

_Phần của: **Section 12: RAG & Vector Database**_

**Số slide:** 8 · ~16 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 🏆 Capstone 5: RAG Chatbot

**🎨 Visual:** `[AI image]` Chatbot tài liệu doanh nghiệp.
**🎤 Speaker note:** "Dự án portfolio thứ 5 — sản phẩm doanh nghiệp thật cần."

### Slide 2 — Bài toán

- SME có nhiều tài liệu nội bộ
- Nhân viên hỏi-đáp nhanh

**🎨 Visual:** `[Mermaid]` Nhu cầu thật.
**🎤 Speaker note:** Bài toán cực phổ biến ở doanh nghiệp VN.

### Slide 3 — Ingest tài liệu

- PDF/Word → chunk → embed → vector DB

**🎨 Visual:** `[Screen]` Ingest pipeline.
**🎤 Speaker note:** Lưu ý tài liệu tiếng Việt.

### Slide 4 — Xây retrieve pipeline

- Hybrid search + reranker

**🎨 Visual:** `[Screen]` Retrieve pipeline.
**🎤 Speaker note:** Áp dụng hybrid + rerank đã học.

### Slide 5 — Generate có trích dẫn

- LLM trả lời + nguồn
- Chống hallucination

**🎨 Visual:** `[Screen]` Trả lời kèm nguồn.
**🎤 Speaker note:** Grounding + citation.

### Slide 6 — Đánh giá bằng RAGAS

- Faithfulness, relevance

**🎨 Visual:** `[Screen]` RAGAS report.
**🎤 Speaker note:** Đo để chứng minh chất lượng.

### Slide 7 — Deploy web UI

- FastAPI + Streamlit/Gradio
- Upload tài liệu → hỏi

**🎨 Visual:** `[Screen]` Web chatbot demo.
**🎤 Speaker note:** Sản phẩm chạy được = ấn tượng nhà tuyển dụng.

### Slide 8 — Tổng kết Section 12

- RAG + Capstone 5 ✅
- Bài tiếp: Section 13 — Agentic AI →

**🎨 Visual:** `[AI image]` Badge "Project 5/7 Done".
**🎤 Speaker note:** "5 dự án rồi! Giờ ta cho AI tự hành động — Agents!"

---

_← [Về Section README](../README.md)_
