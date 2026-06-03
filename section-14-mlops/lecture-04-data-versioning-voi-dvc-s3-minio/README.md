# Section 14 · Lecture 4 — Data versioning với DVC + S3/MinIO

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Data Versioning

**🎨 Visual:** `[AI image]` Dữ liệu có version như code.
**🎤 Speaker note:** "Code đổi, data cũng đổi — phải version cả hai."

### Slide 2 — Vì sao version data

- Tái lập kết quả
- Data đổi → model đổi

**🎨 Visual:** `[Mermaid]` Cùng code, khác data, khác kết quả.
**🎤 Speaker note:** Reproducibility cần version data.

### Slide 3 — DVC

- Git cho dữ liệu lớn
- Track data, không lưu trong Git

**🎨 Visual:** `[Screen]` dvc add/push.
**🎤 Speaker note:** Git lưu con trỏ, data ở storage.

### Slide 4 — S3 / MinIO

- Lưu data thật trên object storage
- MinIO: S3 tự host

**🎨 Visual:** `[Mermaid]` DVC → MinIO/S3.
**🎤 Speaker note:** MinIO hợp môi trường on-premise.

### Slide 5 — Tóm tắt & chuyển bài

- DVC · S3/MinIO · reproducibility
- Bài tiếp: feature store →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta quản lý feature tập trung."

---

_← [Về Section README](../README.md)_
