# Section 11 · Lecture 14 — Mini-Project — Fine-tune model 7B với QLoRA trên dataset chuyên ngành

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 8

---

## Nội dung slide

### Slide 1

- 14
- SECTION 11 · LECTURE 14
- Mini-Project — Fine-tune model 7B với QLoRA trên dataset chuyên ngành
- MINI-PROJECT
- ~14 phút · 7 slides

### Slide 2

- L14 · MINI-PROJECT
- Bài toán & dữ liệu
- Chọn domain (luật, y tế, CSKH…)
- Chuẩn bị dataset instruction
- dataset.jsonl
- {"instruction": "Tóm tắt điều khoản sau…" ,
- "input": "…" ,
- "output": "…"}
- # định dạng đúng là then chốt

### Slide 3

- L14 · MINI-PROJECT
- Setup QLoRA
- Load model 4-bit
- Cấu hình LoRA
- setup.py
- from peft import LoraConfig from transformers import  BitsAndBytesConfig
- bnb =  BitsAndBytesConfig(load_in_4bit=True )
- lora =  LoraConfig(r=16, lora_alpha=32)

### Slide 4

- L14 · MINI-PROJECT
- Huấn luyện
- Train, theo dõi loss
- train.log
- step  100 | loss 1.84
- step  500 | loss 1.12
- step 1000 | loss  0.79  ✓ hội tụ

### Slide 5

- L14 · MINI-PROJECT
- Đánh giá
- So trước / sau fine-tune
- Trên eval set riêng
- TRƯỚC
- Trả lời chung chung
- không sát domain
- SAU
- Đúng văn phong
- thuật ngữ chuyên ngành

### Slide 6

- L14 · MINI-PROJECT
- Merge & dùng
- Gộp LoRA vào model
- Chạy inference — sẵn sàng deploy
- Base + LoRA
- →
- Merge
- →
- Model fine-tuned

### Slide 7

- ✓
- Hoàn thành Section 11
- 14 / 14 lectures · Mini-Project ✓ · 144 / 198 lectures
- BÀI TIẾP
- Section 12 — RAG & Vector Database
- →

### Slide 8

- MASTERING AI · BATCH 8
- 12
- RAG & Vector Database
- Xây pipeline RAG hoàn chỉnh với embedding và vector DB, áp dụng hybrid search , reranker, RAG nâng cao; đánh giá bằng RAGAS và hoàn thành Capstone 5 chatbot tài liệu nội bộ.

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_