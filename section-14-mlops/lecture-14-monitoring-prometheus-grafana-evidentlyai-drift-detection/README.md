# Section 14 · Lecture 14 — Monitoring — Prometheus, Grafana, EvidentlyAI (drift detection)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Monitoring & Drift Detection

**🎨 Visual:** `[AI image]` Dashboard giám sát model.
**🎤 Speaker note:** "Model deploy xong không phải là hết — phải canh nó."

### Slide 2 — Vì sao model "xuống cấp"

- Thế giới thay đổi, dữ liệu đổi
- Accuracy giảm dần

**🎨 Visual:** `[Mermaid]` Accuracy giảm theo thời gian.
**🎤 Speaker note:** Model không tự xấu — thế giới đổi.

### Slide 3 — Các loại drift

- Data drift, concept drift, label drift

**🎨 Visual:** `[Mermaid]` 3 loại drift.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn: data drift vs concept drift?

### Slide 4 — Metric production

- Latency, error rate, throughput
- Prometheus + Grafana

**🎨 Visual:** `[Screen]` Grafana dashboard.
**🎤 Speaker note:** Giám sát hạ tầng + model.

### Slide 5 — EvidentlyAI

- Phát hiện drift tự động
- Báo cáo chất lượng dữ liệu

**🎨 Visual:** `[Screen]` Evidently drift report.
**🎤 Speaker note:** Cảnh báo khi cần retrain.

### Slide 6 — Tóm tắt & chuyển bài

- drift · Prometheus/Grafana · Evidently
- Bài tiếp: LLMOps →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ tới giám sát đặc thù cho LLM."

---

_← [Về Section README](../README.md)_
