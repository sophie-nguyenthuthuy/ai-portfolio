# Section 11 · Lecture 7 — Function calling / tool use — thiết kế JSON schema

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 07
- SECTION 11 · LECTURE 07
- Function calling / tool use — thiết kế JSON schema
- ~8 phút · 6 slides

### Slide 2

- L07 · FUNCTION CALLING
- Vì sao cần tool
- LLM không biết thời gian thực
- Không tính toán chính xác
- LLM
- →
- + Tool
- →
- bù khuyết điểm

### Slide 3

- L07 · FUNCTION CALLING
- Cách hoạt động
- LLM tự quyết định khi nào cần tool
- Mô tả tool
- →
- LLM chọn
- →
- Gọi
- →
- Nhận kết quả

### Slide 4

- L07 · FUNCTION CALLING
- Thiết kế JSON schema
- Mô tả tool rõ ràng: tên, mô tả, tham số
- Mô tả tốt = LLM gọi đúng
- tool_schema.json
- {
- "name": "get_weather" ,
- "description": "Lấy thời tiết theo thành phố" ,
- "parameters": {"city": {"type": "string" }}
- }

### Slide 5

- L07 · FUNCTION CALLING
- Ví dụ thực tế
- Tra cứu DB, gọi API thời tiết
- Thực thi code
- tool_call.py
- # LLM tự sinh lời gọi tool {"tool": "get_weather", "args": {"city": "Hà Nội"}} # → 28°C, có mưa rào

### Slide 6

- L07 · FUNCTION CALLING — TÓM TẮT
- Tóm tắt
- tool use
- JSON schema
- ví dụ thực tế
- BÀI TIẾP
- Fine-tune — LoRA / QLoRA
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_