# Section 8 · Lecture 4 — Kiến trúc CNN — Conv, Pool, FC

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Kiến trúc CNN

**🎨 Visual:** `[AI image]` Sơ đồ CNN từ ảnh tới nhãn.
**🎤 Speaker note:** "Cách các thành phần ghép thành mạng hoàn chỉnh."

### Slide 2 — Lớp Convolution

- Trích đặc trưng từ ảnh
- Nhiều filter → nhiều feature map

**🎨 Visual:** `[Mermaid]` Conv tạo feature maps.
**🎤 Speaker note:** Mỗi filter 1 feature map.

### Slide 3 — Pooling

- Giảm kích thước (max/avg pool)
- Giữ đặc trưng quan trọng

**🎨 Visual:** `[Mermaid]` Max pooling 2×2.
**🎤 Speaker note:** Giảm tính toán + chống overfit nhẹ.

### Slide 4 — Fully Connected

- Làm phẳng → lớp dày → output

**🎨 Visual:** `[Mermaid]` Flatten → FC → softmax.
**🎤 Speaker note:** Phần "ra quyết định" cuối cùng.

### Slide 5 — Toàn cảnh CNN

- Conv-Pool lặp lại → FC → nhãn

**🎨 Visual:** `[Mermaid]` Kiến trúc CNN đầy đủ.
**🎤 Speaker note:** Trích đặc trưng → phân loại.

### Slide 6 — Tóm tắt & chuyển bài

- Conv · Pool · FC
- Bài tiếp: CNN kinh điển →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ xem các kiến trúc nổi tiếng."

---

_← [Về Section README](../README.md)_
