# Section 14 · Lecture 14 — Monitoring — Prometheus, Grafana, EvidentlyAI (drift)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 14
- SECTION 14 · LECTURE 14
- Monitoring — Prometheus, Grafana, EvidentlyAI (drift)
- ~8 phút · 6 slides

### Slide 2

- L14 · MONITORING
- Vì sao model "xuống cấp"
- Thế giới thay đổi, dữ liệu đổi
- Accuracy giảm dần
- Thế giới đổi → accuracy ↓
- model không tự xấu — phân phối dữ liệu thay đổi

### Slide 3

- L14 · MONITORING
- Các loại drift
- Data drift, concept drift, label drift
- DATA DRIFT
- Input đổi
- CONCEPT DRIFT
- Quan hệ đổi
- LABEL DRIFT
- Nhãn đổi

### Slide 4

- L14 · MONITORING
- Metric production
- Latency, error rate, throughput
- Prometheus + Grafana
- SCREEN
- Grafana dashboard: latency P95, error rate, throughput theo thời gian

### Slide 5

- L14 · MONITORING
- EvidentlyAI
- Phát hiện drift tự động
- Cảnh báo khi cần retrain
- SCREEN
- Evidently drift report: so phân phối train vs production, cảnh báo drift

### Slide 6

- L14 · MONITORING — TÓM TẮT
- Tóm tắt
- drift
- Prometheus / Grafana
- Evidently
- BÀI TIẾP
- LLMOps đặc thù
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_