# Section 11 · Lecture 7 — Function calling / tool use — thiết kế JSON schema

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Function Calling / Tool Use

**🎨 Visual:** `[AI image]` LLM gọi API/công cụ.
**🎤 Speaker note:** "Cho LLM 'tay chân' để làm việc thật, không chỉ nói."

### Slide 2 — Vì sao cần tool

- LLM không biết thời gian thực
- Không tính toán chính xác

**🎨 Visual:** `[Mermaid]` LLM + tool bù khuyết điểm.
**🎤 Speaker note:** Tool bù những gì LLM yếu.

### Slide 3 — Cách hoạt động

- Mô tả tool → LLM chọn → gọi → nhận kết quả

**🎨 Visual:** `[Mermaid]` Vòng function calling.
**🎤 Speaker note:** LLM quyết định khi nào cần tool.

### Slide 4 — Thiết kế JSON schema

- Mô tả tool rõ ràng
- Tên, mô tả, tham số

**🎨 Visual:** `[Screen]` JSON schema một tool.
**🎤 Speaker note:** Mô tả tốt = LLM gọi đúng.

### Slide 5 — Ví dụ thực tế

- Tra cứu DB, gọi API thời tiết
- Thực thi code

**🎨 Visual:** `[Screen]` Tool call demo.
**🎤 Speaker note:** Nền tảng của agent.

### Slide 6 — Tóm tắt & chuyển bài

- tool use · JSON schema · ví dụ
- Bài tiếp: fine-tuning LoRA/QLoRA →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta dạy LLM kiến thức chuyên ngành."

---

_← [Về Section README](../README.md)_
