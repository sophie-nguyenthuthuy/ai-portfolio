# Section 9 · Lecture 1 — Tiền xử lý văn bản — tokenization, stemming, lemmatization

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Xử lý ngôn ngữ tự nhiên (NLP)

**🎨 Visual:** `[AI image]` Văn bản biến thành số.
**🎤 Speaker note:** "Máy không hiểu chữ — ta phải biến chữ thành số."

### Slide 2 — Vì sao NLP khó

- Ngôn ngữ mơ hồ, đa nghĩa
- Ngữ cảnh quyết định

**🎨 Visual:** `[Mermaid]` Một câu, nhiều nghĩa.
**🎤 Speaker note:** "Con ngựa đá con ngựa đá" — máy phải hiểu ngữ cảnh.

### Slide 3 — Tokenization

- Tách văn bản thành token
- Word, subword, character

**🎨 Visual:** `[Mermaid]` Câu → các token.
**🎤 Speaker note:** Bước đầu tiên của mọi pipeline NLP.

### Slide 4 — Stemming & Lemmatization

- Đưa từ về dạng gốc
- Stemming (cắt thô) vs Lemma (đúng ngữ pháp)

**🎨 Visual:** `[Mermaid]` running → run.
**🎤 Speaker note:** Giảm số lượng từ phải xử lý.

### Slide 5 — Làm sạch văn bản

- Bỏ stopword, ký tự đặc biệt
- Nối lại regex Section 2

**🎨 Visual:** `[Screen]` Pipeline làm sạch.
**🎤 Speaker note:** Văn bản sạch = model tốt hơn.

### Slide 6 — Tóm tắt & chuyển bài

- tokenize · stem/lemma · làm sạch
- Bài tiếp: BoW & TF-IDF →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta biến văn bản thành vector số."

---

_← [Về Section README](../README.md)_
