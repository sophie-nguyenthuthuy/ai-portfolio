# Section 11 · Lecture 4 — Tokenization cho LLM — BPE, SentencePiece

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5 · ~6 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tokenization cho LLM

**🎨 Visual:** `[AI image]` Văn bản cắt thành token.
**🎤 Speaker note:** "LLM không thấy chữ — chỉ thấy token."

### Slide 2 — Token là gì

- Mảnh subword
- Không phải từ, không phải ký tự

**🎨 Visual:** `[Mermaid]` Câu → token.
**🎤 Speaker note:** Nối lại tokenization Section 9.

### Slide 3 — BPE & SentencePiece

- Gộp cặp ký tự hay đi cùng
- Xử lý từ lạ tốt

**🎨 Visual:** `[Mermaid]` BPE gộp dần.
**🎤 Speaker note:** Cân bằng giữa từ và ký tự.

### Slide 4 — Token & chi phí

- API tính tiền theo token
- Tiếng Việt tốn token hơn tiếng Anh

**🎨 Visual:** `[Screen]` Đếm token.
**🎤 Speaker note:** ⚠️ Lưu ý chi phí khi xử lý tiếng Việt.

### Slide 5 — Tóm tắt & chuyển bài

- token · BPE · chi phí token
- Bài tiếp: prompt engineering →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới kỹ năng quan trọng nhất: viết prompt."

---

_← [Về Section README](../README.md)_
