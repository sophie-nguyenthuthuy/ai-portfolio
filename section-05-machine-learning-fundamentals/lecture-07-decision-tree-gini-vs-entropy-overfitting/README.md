# Section 5 · Lecture 7 — Decision Tree — Gini vs Entropy, overfitting

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Decision Tree — cây quyết định

**🎨 Visual:** `[AI image]` Cây phân nhánh câu hỏi.
**🎤 Speaker note:** "Dễ hiểu nhất — giống cách con người ra quyết định."

### Slide 2 — Cấu trúc cây

- Node hỏi, nhánh trả lời, lá kết luận

**🎨 Visual:** `[Mermaid]` Cây if-then.
**🎤 Speaker note:** Diễn giải được — điểm cộng lớn.

### Slide 3 — Chia nhánh thế nào

- Chọn câu hỏi tách dữ liệu tốt nhất

**🎨 Visual:** `[Mermaid]` Tách dữ liệu theo feature.
**🎤 Speaker note:** Mục tiêu: mỗi nhánh càng "thuần" càng tốt.

### Slide 4 — Gini vs Entropy

- 2 cách đo độ "lộn xộn"
- Chọn split giảm tạp chất nhiều nhất

**🎨 Visual:** `[Mermaid]` So sánh Gini & Entropy.
**🎤 Speaker note:** Thực tế cho kết quả gần giống nhau.

### Slide 5 — Overfitting & cắt tỉa

- Cây sâu = thuộc lòng dữ liệu
- max_depth, min_samples để kiểm soát

**🎨 Visual:** `[Mermaid]` Cây quá sâu vs cắt tỉa.
**🎤 Speaker note:** Cây dễ overfit nhất — phải kiểm soát.

### Slide 6 — Tóm tắt & chuyển bài

- cấu trúc · Gini/Entropy · overfit
- Bài tiếp: Random Forest →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Một cây yếu — nhiều cây thì mạnh."

---

_← [Về Section README](../README.md)_
