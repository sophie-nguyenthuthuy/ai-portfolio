# Section 4 · Lecture 8 — Learning rate, local vs global minimum, nhiễu

_Phần của: **Section 4: Toán & Thống kê cho AI**_

**Số slide:** 6 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tinh chỉnh quá trình học

**🎨 Visual:** `[AI image]` Địa hình gồ ghề nhiều đáy.
**🎤 Speaker note:** "Hiểu phần này giúp bạn debug khi model không hội tụ."

### Slide 2 — Learning rate ảnh hưởng thế nào

- Quá cao: dao động/phân kỳ
- Quá thấp: học chậm

**🎨 Visual:** `[Mermaid]` Đường loss theo lr.
**🎤 Speaker note:** Quan sát loss curve để chỉnh lr.

### Slide 3 — Learning rate schedule

- Giảm dần lr theo thời gian
- Học nhanh đầu, mịn cuối

**🎨 Visual:** `[Mermaid]` lr giảm dần.
**🎤 Speaker note:** Mẹo thực tế tăng chất lượng model.

### Slide 4 — Local minimum & saddle point

- Đáy giả vs đáy thật
- Điểm yên ngựa

**🎨 Visual:** `[Mermaid]` Local, global, saddle.
**🎤 Speaker note:** Momentum giúp thoát các bẫy này.

### Slide 5 — Vai trò của nhiễu

- Stochastic giúp thoát đáy giả
- Nhiễu không hẳn xấu

**🎨 Visual:** `[Mermaid]` Đường đi gập ghềnh vượt đáy giả.
**🎤 Speaker note:** Một chút ngẫu nhiên lại có lợi.

### Slide 6 — Tóm tắt & chuyển bài

- lr schedule · minima · nhiễu
- Bài tiếp: xác suất & Bayes →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ sang xác suất — cách AI xử lý điều không chắc chắn."

---

_← [Về Section README](../README.md)_
