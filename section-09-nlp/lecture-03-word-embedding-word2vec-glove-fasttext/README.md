# Section 9 · Lecture 3 — Word embedding — Word2Vec, GloVe, FastText

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Word Embedding

**🎨 Visual:** `[AI image]` Các từ trong không gian vector.
**🎤 Speaker note:** "Từ có nghĩa gần nhau → vector gần nhau."

### Slide 2 — Ý tưởng

- Biểu diễn từ bằng vector dày
- Nắm bắt ngữ nghĩa

**🎨 Visual:** `[Mermaid]` Từ → vector ngữ nghĩa.
**🎤 Speaker note:** Khác BoW: vector mang ý nghĩa.

### Slide 3 — Phép toán nổi tiếng

- king − man + woman ≈ queen

**🎨 Visual:** `[Mermaid]` Vector arithmetic.
**🎤 Speaker note:** Bằng chứng embedding hiểu quan hệ.

### Slide 4 — Word2Vec & GloVe

- Word2Vec: dự đoán ngữ cảnh
- GloVe: thống kê đồng xuất hiện

**🎨 Visual:** `[Mermaid]` 2 cách train.
**🎤 Speaker note:** Nối lại cosine similarity Section 4.

### Slide 5 — FastText & hạn chế

- FastText: subword, xử lý từ lạ
- Hạn chế: 1 từ 1 vector (không theo ngữ cảnh)

**🎨 Visual:** `[Mermaid]` "bank" 2 nghĩa cùng 1 vector.
**🎤 Speaker note:** Dẫn nhập contextual embedding (BERT).

### Slide 6 — Tóm tắt & chuyển bài

- Word2Vec · GloVe · FastText
- Bài tiếp: NLP tiếng Việt →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xử lý đặc thù tiếng Việt."

---

_← [Về Section README](../README.md)_
