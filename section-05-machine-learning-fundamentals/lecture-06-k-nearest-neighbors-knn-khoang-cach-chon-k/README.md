# Section 5 · Lecture 6 — K-Nearest Neighbors (KNN) — khoảng cách, chọn K

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- KNN — học theo hàng xóm

**🎨 Visual:** `[AI image]` Điểm mới + các điểm gần nhất.
**🎤 Speaker note:** "Bạn là ai = đa số hàng xóm là ai."

### Slide 2 — Nguyên lý

- Tìm K điểm gần nhất
- Bỏ phiếu theo đa số

**🎨 Visual:** `[Mermaid]` K=3 láng giềng bỏ phiếu.
**🎤 Speaker note:** Không "học" trước — tính lúc dự đoán.

### Slide 3 — Khoảng cách

- Euclid, Manhattan
- Nối lại norm L1/L2

**🎨 Visual:** `[Mermaid]` 2 loại khoảng cách.
**🎤 Speaker note:** Nhắc lại Section 4.

### Slide 4 — Chọn K

- K nhỏ: nhiễu
- K lớn: mượt nhưng mờ ranh giới

**🎨 Visual:** `[Mermaid]` Decision boundary theo K.
**🎤 Speaker note:** Thường thử nhiều K, chọn bằng validation.

### Slide 5 — Ưu/nhược & curse of dimensionality

- Đơn giản, dễ hiểu
- Chậm khi dữ liệu lớn, kém với nhiều chiều

**🎨 Visual:** `[Mermaid]` Khoảng cách mất ý nghĩa khi nhiều chiều.
**🎤 Speaker note:** Vì sao cần scale feature trước.

### Slide 6 — Tóm tắt & chuyển bài

- láng giềng · khoảng cách · chọn K
- Bài tiếp: Decision Tree →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta học model dạng cây quyết định."

---

_← [Về Section README](../README.md)_
