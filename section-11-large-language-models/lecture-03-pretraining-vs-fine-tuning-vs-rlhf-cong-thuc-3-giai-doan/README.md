# Section 11 · Lecture 3 — Pretraining vs Fine-tuning vs RLHF — công thức 3 giai đoạn

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 3 giai đoạn tạo nên một LLM

**🎨 Visual:** `[AI image]` 3 bước huấn luyện.
**🎤 Speaker note:** "Hiểu cái này = hiểu vì sao ChatGPT 'biết nghe lời'."

### Slide 2 — Pretraining

- Học từ lượng text khổng lồ
- Dự đoán token tiếp theo

**🎨 Visual:** `[Mermaid]` Text internet → base model.
**🎤 Speaker note:** Tốn kém nhất, học kiến thức nền.

### Slide 3 — Supervised fine-tuning

- Dạy làm theo hướng dẫn
- Ví dụ hỏi-đáp chất lượng

**🎨 Visual:** `[Mermaid]` Base → instruct model.
**🎤 Speaker note:** Biến model thô thành trợ lý.

### Slide 4 — RLHF

- Học từ phản hồi con người
- Reward model + RL

**🎨 Visual:** `[Mermaid]` Người xếp hạng → reward → tinh chỉnh.
**🎤 Speaker note:** Làm model hữu ích, an toàn, đúng ý người.

### Slide 5 — Toàn cảnh

- Pretraining → SFT → RLHF

**🎨 Visual:** `[Mermaid]` 3 giai đoạn nối tiếp.
**🎤 Speaker note:** Mỗi giai đoạn 1 mục đích.

### Slide 6 — Tóm tắt & chuyển bài

- pretraining · SFT · RLHF
- Bài tiếp: tokenization →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xem LLM 'đọc' chữ thế nào."

---

_← [Về Section README](../README.md)_
