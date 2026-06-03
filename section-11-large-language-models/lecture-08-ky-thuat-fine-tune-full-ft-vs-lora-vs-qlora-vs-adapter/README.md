# Section 11 · Lecture 8 — Kỹ thuật fine-tune — full FT vs LoRA vs QLoRA vs adapter

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Fine-tuning LLM

**🎨 Visual:** `[AI image]` Model được tinh chỉnh.
**🎤 Speaker note:** "Khi prompt không đủ, ta dạy lại model."

### Slide 2 — Khi nào fine-tune

- Phong cách/định dạng đặc thù
- Kiến thức chuyên ngành sâu

**🎨 Visual:** `[Mermaid]` Prompt vs fine-tune vs RAG.
**🎤 Speaker note:** ⚠️ Không phải lúc nào cũng cần — cân nhắc RAG trước.

### Slide 3 — Full fine-tuning

- Train lại toàn bộ tham số
- Tốn kém, cần nhiều GPU

**🎨 Visual:** `[Mermaid]` Cập nhật mọi trọng số.
**🎤 Speaker note:** Hiếm khi cần với người học.

### Slide 4 — LoRA

- Chỉ train ma trận nhỏ thêm vào
- Tiết kiệm tài nguyên lớn

**🎨 Visual:** `[Mermaid]` LoRA matrix nhỏ.
**🎤 Speaker note:** Nối lại nhân ma trận Section 4.

### Slide 5 — QLoRA & Adapter

- QLoRA: LoRA + quantization
- Fine-tune model lớn trên 1 GPU

**🎨 Visual:** `[Mermaid]` QLoRA tiết kiệm bộ nhớ.
**🎤 Speaker note:** Cho phép fine-tune ngay trên Colab.

### Slide 6 — Tóm tắt & chuyển bài

- full FT · LoRA · QLoRA · adapter
- Bài tiếp: chạy LLM local →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta chạy LLM ngay trên máy mình."

---

_← [Về Section README](../README.md)_
