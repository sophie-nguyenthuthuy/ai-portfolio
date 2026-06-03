# Section 14 · Lecture 10 — Kubernetes cho ML — K8s cơ bản, Kubeflow, KServe

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Kubernetes cho ML

**🎨 Visual:** `[AI image]` Cụm container được điều phối.
**🎤 Speaker note:** "Khi cần chạy nhiều container, tự co giãn — đó là K8s."

### Slide 2 — Vì sao Kubernetes

- Tự co giãn, tự phục hồi
- Quản lý nhiều container

**🎨 Visual:** `[Mermaid]` K8s điều phối pods.
**🎤 Speaker note:** Chuẩn ngành cho hệ thống lớn.

### Slide 3 — Khái niệm cơ bản

- Pod, Deployment, Service

**🎨 Visual:** `[Mermaid]` Kiến trúc K8s.
**🎤 Speaker note:** Pod = đơn vị nhỏ nhất chạy container.

### Slide 4 — Autoscaling

- Tự tăng/giảm theo tải

**🎨 Visual:** `[Mermaid]` Tải cao → thêm pod.
**🎤 Speaker note:** Tiết kiệm chi phí + chịu tải.

### Slide 5 — Kubeflow & KServe

- Kubeflow: ML platform trên K8s
- KServe: serve model trên K8s

**🎨 Visual:** `[Mermaid]` ML trên K8s.
**🎤 Speaker note:** Đây là nội dung talk "AI Inference trên K8s" của chị.

### Slide 6 — Tóm tắt & chuyển bài

- K8s · pod/deployment · autoscale · Kubeflow/KServe
- Bài tiếp: cloud platforms →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xem các nền tảng cloud."

---

_← [Về Section README](../README.md)_
