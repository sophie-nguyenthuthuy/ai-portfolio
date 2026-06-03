# Section 11 · Lecture 11 — Hallucination — nguyên nhân, phát hiện, giảm thiểu

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Hallucination — khi LLM "bịa"

**🎨 Visual:** `[AI image]` Model nói tự tin nhưng sai.
**🎤 Speaker note:** "Vấn đề nguy hiểm nhất khi đưa LLM vào sản phẩm."

### Slide 2 — Hallucination là gì

- Tạo thông tin sai một cách tự tin

**🎨 Visual:** `[Mermaid]` Câu trả lời sai trông thật.
**🎤 Speaker note:** Nguy hiểm vì nghe rất thuyết phục.

### Slide 3 — Nguyên nhân

- Model đoán token, không "biết"
- Thiếu kiến thức/ngữ cảnh

**🎨 Visual:** `[Mermaid]` Nguyên nhân.
**🎤 Speaker note:** Bản chất "đoán từ tiếp theo" gây ra.

### Slide 4 — Giảm thiểu

- Grounding bằng RAG
- Yêu cầu trích dẫn nguồn
- Hạ temperature

**🎨 Visual:** `[Mermaid]` Các biện pháp.
**🎤 Speaker note:** RAG là vũ khí chính — section sau.

### Slide 5 — Phát hiện

- Kiểm tra chéo nguồn
- Self-consistency

**🎨 Visual:** `[Mermaid]` Cross-check.
**🎤 Speaker note:** Tự động phát hiện vẫn là bài toán mở.

### Slide 6 — Tóm tắt & chuyển bài

- hallucination · nguyên nhân · giảm thiểu
- Bài tiếp: tối ưu chi phí →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta làm LLM rẻ & nhanh hơn."

---

_← [Về Section README](../README.md)_
