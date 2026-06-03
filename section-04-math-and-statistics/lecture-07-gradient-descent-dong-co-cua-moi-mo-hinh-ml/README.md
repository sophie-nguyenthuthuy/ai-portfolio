# Section 4 · Lecture 7 — Gradient Descent — động cơ của mọi mô hình ML

_Phần của: **Section 4: Toán & Thống kê cho AI**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Gradient Descent

**🎨 Visual:** `[AI image]` Người xuống dốc thung lũng.
**🎤 Speaker note:** "Thuật toán quan trọng nhất bạn sẽ học trong khoá."

### Slide 2 — Trực giác

- Đi xuống dốc tới đáy
- Đáy = sai số nhỏ nhất

**🎨 Visual:** `[Mermaid]` Bóng lăn xuống đáy.
**🎤 Speaker note:** Ví von xuống núi trong sương mù.

### Slide 3 — Công thức cập nhật

- tham số ← tham số − lr × gradient

**🎨 Visual:** `[Mermaid]` Công thức + giải nghĩa ký hiệu.
**🎤 Speaker note:** Lặp lại bước này hàng nghìn lần.

### Slide 4 — Learning rate

- Bước đi lớn hay nhỏ
- Quá lớn: nhảy qua đáy; quá nhỏ: chậm

**🎨 Visual:** `[Mermaid]` 3 trường hợp lr.
**🎤 Speaker note:** Siêu tham số quan trọng nhất.

### Slide 5 — Local vs global minimum

- Đáy nhỏ vs đáy thật
- Vì sao đôi khi kẹt

**🎨 Visual:** `[Mermaid]` Mặt loss nhiều đáy.
**🎤 Speaker note:** Thực tế "đủ tốt" thường chấp nhận được.

### Slide 6 — Các biến thể

- Batch · Stochastic · Mini-batch GD

**🎨 Visual:** `[Mermaid]` So sánh 3 cách.
**🎤 Speaker note:** Mini-batch là chuẩn trong deep learning.

### Slide 7 — Tóm tắt & chuyển bài

- xuống dốc · learning rate · minima
- Bài tiếp: nhiễu & minima →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta nói về nhiễu và bẫy local minimum."

---

_← [Về Section README](../README.md)_
