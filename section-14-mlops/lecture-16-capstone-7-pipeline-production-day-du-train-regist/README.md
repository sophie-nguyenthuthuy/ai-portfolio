# Section 14 · Lecture 16 — Capstone 7 — Pipeline production đầy đủ (train → register → serve → monitor → alert)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 9

---

## Nội dung slide

### Slide 1

- 16
- SECTION 14 · LECTURE 16
- Capstone 7 — Pipeline production đầy đủ (train → register → serve → monitor → alert)
- CAPSTONE 7
- ~18 phút · 8 slides

### Slide 2

- L16 · CAPSTONE 7
- Kiến trúc tổng thể
- Train → Register → Serve → Monitor → Alert
- Train
- →
- Register
- →
- Serve
- →
- Monitor
- →
- Alert

### Slide 3

- L16 · CAPSTONE 7
- Train & track
- Train + MLflow tracking
- Đăng ký vào registry
- Train
- →
- MLflow
- →
- Registry

### Slide 4

- L16 · CAPSTONE 7
- Đóng gói & serve
- FastAPI + Docker
- Expose API
- Model
- →
- FastAPI + Docker
- →
- API

### Slide 5

- L16 · CAPSTONE 7
- CI/CD & orchestration
- GitHub Actions tự build / deploy
- Airflow lập lịch retrain
- GitHub Actions
- →
- Build / Deploy
- →
- Airflow retrain

### Slide 6

- L16 · CAPSTONE 7
- Monitor & alert
- Grafana dashboard
- Cảnh báo drift → retrain
- Grafana
- →
- Drift?
- →
- Alert → retrain

### Slide 7

- L16 · CAPSTONE 7
- Demo end-to-end
- Chạy toàn pipeline
- Mô phỏng drift → tự cảnh báo
- SCREEN
- Demo: chạy toàn pipeline · mô phỏng drift → dashboard cảnh báo → trigger retrain

### Slide 8

- ✓
- Hoàn thành Section 14
- 16 / 16 lectures · Capstone 7 ✓ · 182 / 198 lectures
- BÀI TIẾP
- Section 15 — Responsible AI
- →

### Slide 9

- MASTERING AI · LỘ TRÌNH
- Tiến độ tổng — 182 / 198 lectures
- BATCH
- SECTION
- LECTURES
- TRẠNG THÁI
- Batch 1
- S1
- 6
- ✓ Hoàn thành
- Batch 2
- S2 · Python
- 18
- ✓ Hoàn thành
- Batch 3
- S3 + S4
- 26
- ✓ Hoàn thành
- Batch 4
- S5 · ML
- 20
- ✓ Hoàn thành
- Batch 5
- S6 + S7
- 21
- ✓ Hoàn thành
- Batch 6
- S8 · CV
- 16
- ✓ Hoàn thành
- Batch 7
- S9 + S10
- 23
- ✓ Hoàn thành
- Batch 8
- S11 + S12
- 25
- ✓ Hoàn thành
- Batch 9
- S13 Agentic + S14 MLOps
- 27
- ✓ Batch này
- Batch 10
- S15 + S16
- 16
- ⏳ Tiếp theo

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_