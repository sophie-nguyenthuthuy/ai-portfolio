# Section 9 · Lecture 7 — Kiến trúc Transformer — encoder/decoder, multi-head, positional encoding

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Kiến trúc Transformer

**🎨 Visual:** `[AI image]` Sơ đồ Transformer.
**🎤 Speaker note:** "Nền tảng của GPT, BERT, Claude — mọi LLM."

### Slide 2 — Tổng quan

- Encoder + Decoder
- Xếp chồng nhiều khối

**🎨 Visual:** `[Mermaid]` Encoder-Decoder.
**🎤 Speaker note:** BERT dùng encoder, GPT dùng decoder.

### Slide 3 — Multi-head attention

- Nhiều "đầu" chú ý song song
- Nắm nhiều loại quan hệ

**🎨 Visual:** `[Mermaid]` Nhiều head attention.
**🎤 Speaker note:** Mỗi head học 1 kiểu quan hệ.

### Slide 4 — Positional encoding

- Transformer không có thứ tự sẵn
- Mã hoá vị trí từ

**🎨 Visual:** `[Mermaid]` Thêm vị trí vào embedding.
**🎤 Speaker note:** Vì xử lý song song nên cần báo thứ tự.

### Slide 5 — Feed-forward & residual

- FFN sau attention
- Residual + LayerNorm

**🎨 Visual:** `[Mermaid]` Khối Transformer đầy đủ.
**🎤 Speaker note:** Nối lại skip connection (ResNet) Section 8.

### Slide 6 — Encoder vs Decoder

- Encoder: hiểu (BERT)
- Decoder: sinh (GPT)

**🎨 Visual:** `[Mermaid]` So sánh 2 nhánh.
**🎤 Speaker note:** Quyết định kiến trúc dùng cho task gì.

### Slide 7 — Tóm tắt & chuyển bài

- encoder/decoder · multi-head · positional
- Bài tiếp: BERT →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta dùng BERT cho bài toán thật."

---

_← [Về Section README](../README.md)_
