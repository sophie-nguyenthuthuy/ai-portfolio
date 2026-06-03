# Section 11 · Lecture 4 — Tokenization cho LLM — BPE, SentencePiece

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 11 · LECTURE 04
- Tokenization cho LLM — BPE, SentencePiece
- ~6 phút · 5 slides

### Slide 2

- L04 · TOKENIZATION
- Token là gì
- Mảnh subword
- Không phải từ, cũng không phải ký tự
- “tokenization”
- →
- token
- →
- ##ization

### Slide 3

- L04 · TOKENIZATION
- BPE & SentencePiece
- Gộp dần các cặp ký tự hay đi cùng
- Xử lý từ lạ tốt
- t,o,k,e,n → to, ken → token
- BPE gộp cặp phổ biến — cân bằng từ ↔ ký tự

### Slide 4

- L04 · TOKENIZATION
- Token & chi phí
- API tính tiền theo token
- ⚠️ Tiếng Việt tốn token hơn tiếng Anh
- count_tokens.py
- import  tiktoken
- enc = tiktoken.get_encoding("cl100k_base") len(enc.encode("Xin chào thế giới")) # → 9 tokens · "Hello world" → 2

### Slide 5

- L04 · TOKENIZATION — TÓM TẮT
- Tóm tắt
- token
- BPE / SentencePiece
- chi phí token
- BÀI TIẾP
- Prompt engineering
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_