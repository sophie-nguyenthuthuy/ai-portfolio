# Section 14 · Lecture 4 — Data versioning với DVC + S3 / MinIO

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 04
- SECTION 14 · LECTURE 04
- Data versioning với DVC + S3 / MinIO
- ~7 phút · 5 slides

### Slide 2

- L04 · DATA VERSIONING
- Vì sao version data
- Tái lập kết quả
- Data đổi → model đổi
- Cùng code + khác data = khác kết quả
- reproducibility cần version cả dữ liệu

### Slide 3

- L04 · DATA VERSIONING
- DVC
- Git cho dữ liệu lớn
- Git lưu con trỏ, data ở storage
- terminal
- $ dvc add data/train.csv $ dvc push # Git lưu .dvc (con trỏ) · data lên storage

### Slide 4

- L04 · DATA VERSIONING
- S3 / MinIO
- Lưu data thật trên object storage
- MinIO: S3 tự host (on-premise)
- DVC
- →
- MinIO / S3

### Slide 5

- L04 · DATA VERSIONING — TÓM TẮT
- Tóm tắt
- DVC
- S3 / MinIO
- reproducibility
- BÀI TIẾP
- Feature store
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_