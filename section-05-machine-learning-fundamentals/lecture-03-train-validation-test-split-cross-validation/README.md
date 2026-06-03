# Section 5 · Lecture 3 — Train/validation/test split + cross-validation

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Chia dữ liệu đúng cách

**🎨 Visual:** `[Mermaid]` Dataset chia 3 phần.
**🎤 Speaker note:** "Lỗi này khiến nhiều người tưởng model giỏi mà thực ra dở."

### Slide 2 — Vì sao phải chia

- Học bài rồi thi đúng đề = gian lận
- Cần dữ liệu chưa thấy để đánh giá

**🎨 Visual:** `[AI image]` Học sinh thi đề lạ.
**🎤 Speaker note:** Ví von học thuộc lòng vs hiểu thật.

### Slide 3 — Train / Validation / Test

- Train: học
- Validation: tinh chỉnh
- Test: chấm cuối cùng

**🎨 Visual:** `[Mermaid]` 3 vai trò.
**🎤 Speaker note:** Test chỉ dùng 1 lần, cuối cùng.

### Slide 4 — Cross-validation

- Chia k phần, luân phiên train/test
- Đánh giá ổn định hơn

**🎨 Visual:** `[Mermaid]` K-fold minh hoạ.
**🎤 Speaker note:** Dùng khi dữ liệu ít.

### Slide 5 — Data leakage

- Rò rỉ thông tin test vào train
- Lỗi nguy hiểm & khó phát hiện

**🎨 Visual:** `[Mermaid]` Mũi tên rò rỉ.
**🎤 Speaker note:** Scale/encode phải fit trên train trước.

### Slide 6 — Tóm tắt & chuyển bài

- split · cross-validation · leakage
- Bài tiếp: Linear Regression →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xây model đầu tiên."

---

_← [Về Section README](../README.md)_
