# Section 9 · Lecture 8 — Dòng BERT — fine-tune cho classification, NER, QA

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- BERT & fine-tuning

**🎨 Visual:** `[AI image]` Logo BERT + các task.
**🎤 Speaker note:** "Model encoder mạnh nhất cho hiểu văn bản."

### Slide 2 — BERT là gì

- Encoder Transformer pretrained
- Contextual embedding (theo ngữ cảnh)

**🎨 Visual:** `[Mermaid]` "bank" 2 nghĩa → 2 vector.
**🎤 Speaker note:** Khắc phục hạn chế Word2Vec.

### Slide 3 — Pretraining của BERT

- Masked LM: đoán từ bị che
- Học từ lượng văn bản khổng lồ

**🎨 Visual:** `[Mermaid]` Che từ → đoán.
**🎤 Speaker note:** Học hiểu ngôn ngữ trước, dùng sau.

### Slide 4 — Fine-tuning

- Thêm lớp đầu cho task cụ thể
- Train với ít dữ liệu

**🎨 Visual:** `[Mermaid]` BERT + task head.
**🎤 Speaker note:** Tận dụng kiến thức pretrained.

### Slide 5 — Các task

- Classification, NER, QA
- PhoBERT cho tiếng Việt

**🎨 Visual:** `[Screen]` Hugging Face fine-tune.
**🎤 Speaker note:** PhoBERT là BERT cho tiếng Việt.

### Slide 6 — Tóm tắt & chuyển bài

- BERT · masked LM · fine-tune · PhoBERT
- Bài tiếp: GPT →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ sang dòng sinh văn bản — GPT."

---

_← [Về Section README](../README.md)_
