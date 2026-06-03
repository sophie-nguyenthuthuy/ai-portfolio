# Section 9 · Lecture 6 — Cơ chế Attention — bước đột phá

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Attention — "Attention is all you need"

**🎨 Visual:** `[AI image]` Các từ kết nối với nhau.
**🎤 Speaker note:** "Ý tưởng thay đổi toàn bộ AI hiện đại."

### Slide 2 — Vấn đề cần giải

- RNN xử lý tuần tự, quên xa
- Cần "nhìn" mọi từ cùng lúc

**🎨 Visual:** `[Mermaid]` RNN tuần tự vs nhìn toàn cục.
**🎤 Speaker note:** Attention giải cả 2 vấn đề.

### Slide 3 — Attention là gì

- Mỗi từ "chú ý" tới các từ liên quan
- Trọng số liên quan

**🎨 Visual:** `[Mermaid]` Trọng số attention giữa từ.
**🎤 Speaker note:** Ví dụ: "nó" chú ý tới danh từ nào.

### Slide 4 — Self-attention

- Các từ trong câu chú ý lẫn nhau
- Query, Key, Value

**🎨 Visual:** `[Mermaid]` Q-K-V.
**🎤 Speaker note:** Cơ chế cốt lõi của Transformer.

### Slide 5 — Vì sao mạnh

- Song song hoá được (nhanh)
- Bắt quan hệ xa

**🎨 Visual:** `[Mermaid]` Mọi từ kết nối trực tiếp.
**🎤 Speaker note:** Nối lại ViT (ảnh) Section 8.

### Slide 6 — Tóm tắt & chuyển bài

- attention · self-attention · Q-K-V
- Bài tiếp: Transformer →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp attention thành kiến trúc Transformer."

---

_← [Về Section README](../README.md)_
