# Section 9 · Lecture 5 — RNN & LSTM — vì sao chúng đi trước Transformer

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 5 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- RNN & LSTM cho ngôn ngữ

**🎨 Visual:** `[AI image]` Chuỗi từ truyền qua mạng.
**🎤 Speaker note:** "Ôn lại nhanh — đã gặp ở time-series."

### Slide 2 — Vì sao cần xử lý chuỗi

- Thứ tự từ quan trọng
- Ngữ cảnh phụ thuộc từ trước

**🎨 Visual:** `[Mermaid]` Câu = chuỗi từ.
**🎤 Speaker note:** Nối lại LSTM Section 6.

### Slide 3 — RNN cho NLP

- Đọc từ trái sang phải, giữ ngữ cảnh

**🎨 Visual:** `[Mermaid]` RNN xử lý câu.
**🎤 Speaker note:** Trí nhớ ngắn hạn là điểm yếu.

### Slide 4 — Hạn chế

- Xử lý tuần tự (chậm, khó song song)
- Quên ngữ cảnh xa

**🎨 Visual:** `[Mermaid]` Câu dài → quên đầu câu.
**🎤 Speaker note:** Đây là lý do Transformer ra đời.

### Slide 5 — Tóm tắt & chuyển bài

- RNN/LSTM · hạn chế tuần tự
- Bài tiếp: attention →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới bước đột phá: cơ chế attention."

---

_← [Về Section README](../README.md)_
