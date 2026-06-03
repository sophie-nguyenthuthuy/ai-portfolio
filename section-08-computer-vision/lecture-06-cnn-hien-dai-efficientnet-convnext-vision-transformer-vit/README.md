# Section 8 · Lecture 6 — CNN hiện đại — EfficientNet, ConvNeXt, Vision Transformer (ViT)

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- CV hiện đại

**🎨 Visual:** `[AI image]` Ảnh chia thành các patch.
**🎤 Speaker note:** "Transformer không chỉ cho text — còn cho ảnh."

### Slide 2 — EfficientNet

- Cân bằng độ sâu/rộng/phân giải
- Nhẹ, nhanh, chính xác

**🎨 Visual:** `[Mermaid]` Scaling cân bằng.
**🎤 Speaker note:** Phổ biến trong production.

### Slide 3 — ConvNeXt

- CNN "hiện đại hoá" theo ý tưởng Transformer

**🎨 Visual:** `[Mermaid]` ConvNeXt block.
**🎤 Speaker note:** Chứng minh CNN vẫn cạnh tranh.

### Slide 4 — Vision Transformer (ViT)

- Ảnh → chuỗi patch
- Áp dụng attention như NLP

**🎨 Visual:** `[Mermaid]` Ảnh → patches → transformer.
**🎤 Speaker note:** Gặp lại attention chi tiết ở Section NLP.

### Slide 5 — Khi nào dùng cái nào

- ViT: dữ liệu lớn
- CNN/EfficientNet: dữ liệu vừa, edge

**🎨 Visual:** `[Mermaid]` Bảng lựa chọn.
**🎤 Speaker note:** Thực tế thường vẫn chọn CNN cho dữ liệu nhỏ.

### Slide 6 — Tóm tắt & chuyển bài

- EfficientNet · ConvNeXt · ViT
- Bài tiếp: transfer learning →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tận dụng model đã train sẵn."

---

_← [Về Section README](../README.md)_
