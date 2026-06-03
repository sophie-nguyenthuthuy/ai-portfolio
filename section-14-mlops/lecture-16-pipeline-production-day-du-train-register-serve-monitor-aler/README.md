# Section 14 · Lecture 16 — 🏆 Capstone 7 — Pipeline production đầy đủ (train → register → serve → monitor → alert)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 8 · ~18 phút (kèm screen recording)

---

## Nội dung slide

### Slide 1 — Tiêu đề

- 🏆 Capstone 7: Pipeline Production

**🎨 Visual:** `[AI image]` Pipeline ML end-to-end.
**🎤 Speaker note:** "Dự án portfolio cuối — chứng minh bạn làm được production thật."

### Slide 2 — Kiến trúc tổng thể

- Train → Register → Serve → Monitor → Alert

**🎨 Visual:** `[Mermaid]` Kiến trúc đầy đủ.
**🎤 Speaker note:** Ráp mọi thứ Section 14.

### Slide 3 — Train & track

- Train + MLflow tracking
- Đăng ký vào registry

**🎨 Visual:** `[Screen]` MLflow + registry.
**🎤 Speaker note:** Áp dụng tracking + registry.

### Slide 4 — Đóng gói & serve

- FastAPI + Docker
- Expose API

**🎨 Visual:** `[Screen]` Dockerized API.
**🎤 Speaker note:** Container hoá model service.

### Slide 5 — CI/CD & orchestration

- GitHub Actions tự build/deploy
- Airflow lập lịch retrain

**🎨 Visual:** `[Screen]` Pipeline tự động.
**🎤 Speaker note:** Tự động hoá toàn bộ.

### Slide 6 — Monitor & alert

- Grafana dashboard
- Cảnh báo drift → retrain

**🎨 Visual:** `[Screen]` Dashboard + alert.
**🎤 Speaker note:** Khép vòng MLOps: phát hiện drift → retrain.

### Slide 7 — Demo end-to-end

- Chạy toàn pipeline
- Mô phỏng drift → tự cảnh báo

**🎨 Visual:** `[Screen]` Demo hoàn chỉnh.
**🎤 Speaker note:** Đây là dự án "vương miện" của portfolio.

### Slide 8 — Tổng kết Section 14

- MLOps + Capstone 7 ✅
- Bài tiếp: Section 15 — Responsible AI →

**🎨 Visual:** `[AI image]` Badge "Project 7/7 Done".
**🎤 Speaker note:** "7/7 dự án xong! Bạn đã là AI Engineer thực thụ. Còn 2 section nữa!"

---

_← [Về Section README](../README.md)_
