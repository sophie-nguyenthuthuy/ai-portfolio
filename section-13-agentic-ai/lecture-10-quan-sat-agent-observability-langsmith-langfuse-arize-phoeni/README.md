# Section 13 · Lecture 10 — Quan sát agent (observability) — LangSmith, LangFuse, Arize Phoenix

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 6 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Agent Observability

**🎨 Visual:** `[AI image]` Dashboard theo dõi agent.
**🎤 Speaker note:** "Agent là hộp đen — phải nhìn được nó nghĩ gì."

### Slide 2 — Vì sao cần observability

- Debug khi agent làm sai
- Theo dõi chi phí, độ trễ

**🎨 Visual:** `[Mermaid]` Trace agent steps.
**🎤 Speaker note:** Không nhìn được = không sửa được.

### Slide 3 — Tracing

- Ghi lại từng bước: nghĩ, tool, kết quả

**🎨 Visual:** `[Screen]` Trace một lần chạy.
**🎤 Speaker note:** Thấy rõ agent đi qua những bước nào.

### Slide 4 — Công cụ

- LangSmith, LangFuse, Arize Phoenix

**🎨 Visual:** `[Mermaid]` So sánh công cụ.
**🎤 Speaker note:** Nối lại LangSmith ở RAG observability.

### Slide 5 — Failure mode thường gặp

- Vòng lặp vô hạn, dùng sai tool
- Context overflow

**🎨 Visual:** `[Mermaid]` Các lỗi agent.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn: agent loop vô hạn debug sao?

### Slide 6 — Tóm tắt & chuyển bài

---

_← [Về Section README](../README.md)_
