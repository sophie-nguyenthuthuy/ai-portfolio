# Section 14 · Lecture 2 — Experiment tracking — MLflow, Weights & Biases, Comet

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 02
- SECTION 14 · LECTURE 02
- Experiment tracking — MLflow, Weights & Biases, Comet
- ~8 phút · 6 slides

### Slide 2

- L02 · EXPERIMENT TRACKING
- Vấn đề khi không track
- Quên tham số, không tái lập được
- "Model tốt mà không nhớ chạy sao"
- không track = không tái lập được kết quả

### Slide 3

- L02 · EXPERIMENT TRACKING
- Track gì
- Params, metrics
- Artifacts, code version
- PARAMS
- Tham số
- METRICS
- Kết quả
- ARTIFACTS
- Model · file
- CODE
- Version

### Slide 4

- L02 · EXPERIMENT TRACKING
- MLflow
- Mã nguồn mở, phổ biến
- Log + UI so sánh
- train.py
- import mlflow with mlflow.start_run ():
- mlflow. log_param("lr" , 3e-4)
- mlflow. log_metric("acc" , 0.92)
- mlflow. log_artifact("model.pkl")

### Slide 5

- L02 · EXPERIMENT TRACKING
- W&B & Comet
- Dashboard đẹp, cộng tác
- MLFLOW
- Mã nguồn mở
- self-host
- W&B · COMET
- Dashboard đẹp
- cộng tác team

### Slide 6

- L02 · EXPERIMENT TRACKING — TÓM TẮT
- Tóm tắt
- tracking
- MLflow
- W&B
- BÀI TIẾP
- Model registry
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_