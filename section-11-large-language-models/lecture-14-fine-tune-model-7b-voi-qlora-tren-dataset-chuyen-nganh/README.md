# Section 11 · Lecture 14 — Mini-Project — Fine-tune model 7B với QLoRA trên dataset chuyên ngành

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 7 · ~14 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Mini-Project: Fine-tune LLM với QLoRA

**🎨 Visual:** `[AI image]` Model 7B được tinh chỉnh.
**🎤 Speaker note:** "Fine-tune model lớn ngay trên Colab — kỹ năng đáng giá."

### Slide 2 — Bài toán & dữ liệu

- Chọn domain (luật, y tế, CSKH...)
- Chuẩn bị dataset instruction

**🎨 Visual:** `[Screen]` Dataset format.
**🎤 Speaker note:** Định dạng dữ liệu đúng là then chốt.

### Slide 3 — Setup QLoRA

- Load model 4-bit
- Cấu hình LoRA

**🎨 Visual:** `[Screen]` peft + bitsandbytes.
**🎤 Speaker note:** Quantization giúp vừa bộ nhớ Colab.

### Slide 4 — Huấn luyện

- Train, theo dõi loss

**🎨 Visual:** `[Screen]` Training run.
**🎤 Speaker note:** Nối lại training loop đã học.

### Slide 5 — Đánh giá

- So trước/sau fine-tune
- Eval set riêng

**🎨 Visual:** `[Screen]` So sánh output.
**🎤 Speaker note:** Đo trên benchmark riêng của bài toán.

### Slide 6 — Merge & dùng

- Gộp LoRA vào model
- Chạy inference

**🎨 Visual:** `[Screen]` Inference model fine-tuned.
**🎤 Speaker note:** Sẵn sàng deploy.

### Slide 7 — Tổng kết Section 11

- LLMs ✅
- Bài tiếp: Section 12 — RAG →

**🎨 Visual:** `[AI image]` Cánh cửa mở.
**🎤 Speaker note:** "Làm chủ LLM rồi. Giờ ta giải bài toán hallucination bằng RAG!"

---

_← [Về Section README](../README.md)_
