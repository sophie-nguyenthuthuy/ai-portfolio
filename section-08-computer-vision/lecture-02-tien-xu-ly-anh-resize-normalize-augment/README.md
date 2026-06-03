# Section 8 · Lecture 2 — Tiền xử lý ảnh — resize, normalize, augment

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Tiền xử lý ảnh

**🎨 Visual:** `[AI image]` Ảnh được resize & biến đổi.
**🎤 Speaker note:** "Ảnh thô không dùng được ngay — phải chuẩn hoá."

### Slide 2 — Resize & crop

- Đưa về cùng kích thước
- Model cần input cố định

**🎨 Visual:** `[Screen]` Resize ảnh.
**🎤 Speaker note:** Hầu hết CNN cần kích thước cố định.

### Slide 3 — Normalize

- Đưa pixel về [0,1] hoặc chuẩn hoá
- Giúp train ổn định

**🎨 Visual:** `[Mermaid]` Trước/sau normalize.
**🎤 Speaker note:** Nối lại scaling Section 5.

### Slide 4 — Data augmentation

- Lật, xoay, đổi sáng, crop
- Tăng đa dạng dữ liệu

**🎨 Visual:** `[Screen]` 1 ảnh → nhiều biến thể.
**🎤 Speaker note:** Chống overfitting cực hiệu quả.

### Slide 5 — Khi nào augment

- Chỉ augment trên train
- Không augment test

**🎨 Visual:** `[Mermaid]` Train có / test không.
**🎤 Speaker note:** Augment test = đánh giá sai.

### Slide 6 — Tóm tắt & chuyển bài

- resize · normalize · augment
- Bài tiếp: convolution →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới trái tim của CV: phép tích chập."

---

_← [Về Section README](../README.md)_
