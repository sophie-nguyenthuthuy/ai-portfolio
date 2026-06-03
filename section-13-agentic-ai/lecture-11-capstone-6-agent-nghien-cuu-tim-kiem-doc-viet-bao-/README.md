# Section 13 · Lecture 11 — Capstone 6 — Agent nghiên cứu (tìm kiếm, đọc, viết báo cáo)

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 9

---

## Nội dung slide

### Slide 1

- 11
- SECTION 13 · LECTURE 11
- Capstone 6 — Agent nghiên cứu (tìm kiếm, đọc, viết báo cáo)
- CAPSTONE 6
- ~15 phút · 8 slides

### Slide 2

- L11 · CAPSTONE 6
- Bài toán
- Nhập chủ đề → agent tự tìm, đọc, tổng hợp
- Xuất báo cáo có nguồn
- Chủ đề
- →
- Agent
- →
- Báo cáo + nguồn

### Slide 3

- L11 · CAPSTONE 6
- Thiết kế kiến trúc
- LangGraph state machine
- Tools: search, fetch, write
- State: chủ đề + phát hiện
- ↓
- Node: search → fetch → write
- ↓
- Điều kiện: đủ thông tin? → lặp / kết thúc

### Slide 4

- L11 · CAPSTONE 6
- Tool & memory
- Web search, đọc trang
- Memory lưu phát hiện
- tools.py
- tools = [
- web_search,
- # tìm nguồn   fetch_page,    # đọc nội dung   write_report,  # tổng hợp ]
- memory.save(findings)
- # nhớ phát hiện

### Slide 5

- L11 · CAPSTONE 6
- Vòng lặp ReAct
- Nghĩ → tìm → đọc → tổng hợp → lặp
- Nghĩ
- →
- Tìm
- →
- Đọc
- →
- Tổng hợp
- →
- ↻

### Slide 6

- L11 · CAPSTONE 6
- Observability & guardrail
- Trace bằng LangSmith
- Giới hạn số bước (chống loop)
- SCREEN
- Trace LangSmith + giới hạn max_steps để chống vòng lặp vô hạn

### Slide 7

- L11 · CAPSTONE 6
- Output & demo
- Báo cáo có trích dẫn
- Web UI nhập chủ đề
- UI
- Web app: ô nhập chủ đề → agent chạy → báo cáo có trích dẫn nguồn

### Slide 8

- ✓
- Hoàn thành Section 13
- 11 / 11 lectures · Capstone 6 ✓ · 166 / 198 lectures
- BÀI TIẾP
- Section 14 — MLOps
- →

### Slide 9

- MASTERING AI · BATCH 9
- 14
- MLOps & Triển khai Production
- Dựng pipeline MLOps đầy đủ (tracking, registry, versioning, orchestration ), đóng gói API, deploy cloud / K8s, CI/CD, giám sát drift và LLMOps — hoàn thành Capstone cuối.

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_