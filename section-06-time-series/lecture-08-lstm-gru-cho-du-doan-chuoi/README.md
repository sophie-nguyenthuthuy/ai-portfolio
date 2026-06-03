# Section 6 · Lecture 8 — LSTM & GRU cho dự đoán chuỗi

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- LSTM & GRU

**🎨 Visual:** `[AI image]` Mạng có "bộ nhớ".
**🎤 Speaker note:** "Deep learning cho dữ liệu có thứ tự."

### Slide 2 — Vì sao cần "bộ nhớ"

- Regression thường quên quá khứ
- Chuỗi cần nhớ ngữ cảnh

**🎨 Visual:** `[Mermaid]` Thông tin truyền qua thời gian.
**🎤 Speaker note:** Dẫn nhập RNN.

### Slide 3 — RNN & vấn đề

- Trí nhớ ngắn hạn
- Vanishing gradient

**🎨 Visual:** `[Mermaid]` Gradient mờ dần qua thời gian.
**🎤 Speaker note:** RNN khó nhớ quan hệ xa.

### Slide 4 — LSTM

- Cơ chế "cổng" (gate)
- Nhớ dài hạn, quên nhiễu

**🎨 Visual:** `[Mermaid]` LSTM cell với các cổng.
**🎤 Speaker note:** Giải thích nôm na: cổng quyết định nhớ/quên.

### Slide 5 — GRU & chuẩn bị dữ liệu

- GRU: gọn hơn LSTM
- Phải scale về [0,1]

**🎨 Visual:** `[Screen]` Scale + reshape cho LSTM.
**🎤 Speaker note:** ⚠️ LSTM bắt buộc scale, ARIMA thì không.

### Slide 6 — Tóm tắt & chuyển bài

- RNN · LSTM · GRU · scale
- Bài tiếp: Capstone 2 →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả vào dự án dự báo thật."

---

_← [Về Section README](../README.md)_
