# Section 14 · Lecture 7 — CI/CD cho ML — GitHub Actions (test, lint, build, deploy)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- CI/CD cho ML

**🎨 Visual:** `[AI image]` Pipeline tự động test → deploy.
**🎤 Speaker note:** "Tự động kiểm tra & triển khai — như software thật."

### Slide 2 — CI/CD là gì

- CI: tự động test khi push code
- CD: tự động deploy

**🎨 Visual:** `[Mermaid]` Push → test → deploy.
**🎤 Speaker note:** Đảm bảo chất lượng, deploy nhanh.

### Slide 3 — Khác biệt cho ML

- Test cả data & model
- Reproducibility

**🎨 Visual:** `[Mermaid]` CI/CD ML vs software.
**🎤 Speaker note:** ML có thêm data & model để test.

### Slide 4 — GitHub Actions

- Tự động test, build Docker, push

**🎨 Visual:** `[Screen]` GitHub Actions workflow.
**🎤 Speaker note:** Nối lại Git/GitHub Section 1.

### Slide 5 — Tóm tắt & chuyển bài

- CI/CD · test data/model · GitHub Actions
- Bài tiếp: model serving →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta phục vụ model qua API."

---

_← [Về Section README](../README.md)_
