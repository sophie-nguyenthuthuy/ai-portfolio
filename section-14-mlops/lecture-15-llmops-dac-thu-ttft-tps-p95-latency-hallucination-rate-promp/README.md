# Section 14 · Lecture 15 — LLMOps đặc thù — TTFT, TPS, P95 latency, hallucination rate, prompt versioning

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- LLMOps — MLOps cho LLM

**🎨 Visual:** `[AI image]` Dashboard giám sát LLM.
**🎤 Speaker note:** "LLM có những metric riêng mà ML thường không có."

### Slide 2 — Vì sao LLM khác

- Sinh văn bản, không phải nhãn
- Chi phí token, độ trễ cao

**🎨 Visual:** `[Mermaid]` ML vs LLM ops.
**🎤 Speaker note:** Cần bộ metric riêng.

### Slide 3 — Metric tốc độ

- TTFT (Time To First Token)
- TPS (Tokens Per Second)
- P95 latency

**🎨 Visual:** `[Mermaid]` Các metric tốc độ.
**🎤 Speaker note:** TTFT ảnh hưởng trải nghiệm người dùng nhất.

### Slide 4 — Metric chất lượng

- Hallucination rate
- Faithfulness, relevance

**🎨 Visual:** `[Mermaid]` Metric chất lượng.
**🎤 Speaker note:** Nối lại RAGAS Section 12.

### Slide 5 — Prompt versioning

- Prompt cũng cần version
- A/B test prompt

**🎨 Visual:** `[Mermaid]` Version prompt.
**🎤 Speaker note:** Đổi prompt = đổi hành vi — phải track.

### Slide 6 — Tóm tắt & chuyển bài

- TTFT/TPS/P95 · hallucination rate · prompt version
- Bài tiếp: Capstone 7 →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp TẤT CẢ vào pipeline production hoàn chỉnh."

---

_← [Về Section README](../README.md)_
