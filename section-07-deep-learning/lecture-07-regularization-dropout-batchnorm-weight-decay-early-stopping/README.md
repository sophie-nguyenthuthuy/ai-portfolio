# Section 7 · Lecture 7 — Regularization — Dropout, BatchNorm, weight decay, early stopping

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Regularization — chống overfitting

**🎨 Visual:** `[AI image]` Đường khớp vừa vs quá khớp.
**🎤 Speaker note:** "Mạng lớn rất dễ thuộc lòng — phải kiểm soát."

### Slide 2 — Dropout

- Tắt ngẫu nhiên nơ-ron khi train
- Buộc mạng không phụ thuộc 1 đường

**🎨 Visual:** `[Mermaid]` Nơ-ron bị tắt.
**🎤 Speaker note:** Đơn giản mà hiệu quả.

### Slide 3 — Batch Normalization

- Chuẩn hoá đầu ra giữa các lớp
- Train ổn định & nhanh hơn

**🎨 Visual:** `[Mermaid]` BatchNorm giữa lớp.
**🎤 Speaker note:** Gần như mặc định trong CNN.

### Slide 4 — Weight decay (L2)

- Phạt trọng số lớn
- Nối lại norm L2 Section 4

**🎨 Visual:** `[Mermaid]` Trọng số bị "kéo nhỏ".
**🎤 Speaker note:** Giữ mô hình đơn giản hơn.

### Slide 5 — Early stopping

- Dừng khi validation loss tăng

**🎨 Visual:** `[Mermaid]` Điểm dừng tối ưu.
**🎤 Speaker note:** Mẹo đơn giản, hiệu quả, miễn phí.

### Slide 6 — Tóm tắt & chuyển bài

- dropout · batchnorm · weight decay · early stop
- Bài tiếp: PyTorch →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta dùng framework thật — PyTorch."

---

_← [Về Section README](../README.md)_
