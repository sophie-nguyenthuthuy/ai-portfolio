# Section 13 · Lecture 11 — 🏆 Capstone 6 — Agent nghiên cứu (tìm kiếm, đọc, viết báo cáo)

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 8 · ~15 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 🏆 Capstone 6: Research Agent

**🎨 Visual:** `[AI image]` Agent tự nghiên cứu & viết.
**🎤 Speaker note:** "Dự án portfolio thứ 6 — agent đa bước thật."

### Slide 2 — Bài toán

- Nhập chủ đề → agent tự tìm, đọc, tổng hợp
- Xuất báo cáo có nguồn

**🎨 Visual:** `[Mermaid]` Input → agent → báo cáo.
**🎤 Speaker note:** Tự động hoá nghiên cứu.

### Slide 3 — Thiết kế kiến trúc

- LangGraph state machine
- Tools: search, fetch, write

**🎨 Visual:** `[Mermaid]` Kiến trúc agent.
**🎤 Speaker note:** Áp dụng pattern + tool đã học.

### Slide 4 — Tool & memory

- Web search, đọc trang
- Memory lưu phát hiện

**🎨 Visual:** `[Screen]` Định nghĩa tools.
**🎤 Speaker note:** Memory tránh quên giữa các bước.

### Slide 5 — Vòng lặp ReAct

- Nghĩ → tìm → đọc → tổng hợp → lặp

**🎨 Visual:** `[Screen]` Agent chạy từng bước.
**🎤 Speaker note:** Thấy rõ agent suy luận.

### Slide 6 — Observability & guardrail

- Trace bằng LangSmith
- Giới hạn số bước (chống loop)

**🎨 Visual:** `[Screen]` Trace + limit.
**🎤 Speaker note:** Production phải có guardrail.

### Slide 7 — Output & demo

- Báo cáo có trích dẫn
- Web UI nhập chủ đề

**🎨 Visual:** `[Screen]` Demo agent.
**🎤 Speaker note:** Dự án ấn tượng nhất portfolio.

### Slide 8 — Tổng kết Section 13

- Agentic AI + Capstone 6 ✅
- Bài tiếp: Section 14 — MLOps →

**🎨 Visual:** `[AI image]` Badge "Project 6/7 Done".
**🎤 Speaker note:** "6 dự án rồi! Giờ ta đưa mọi thứ vào production."

---

_← [Về Section README](../README.md)_
