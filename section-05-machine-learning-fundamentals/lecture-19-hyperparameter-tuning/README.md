# Section 5 · Lecture 19 — Hyperparameter Tuning

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- LECTURE 19 · ~9 PHÚT
- 19
- Hyperparameter Tuning
- Grid · Random · Bayesian (Optuna)

### Slide 2

- L19 · PARAMETER VS HYPERPARAMETER
- Cái nào model tự học, cái nào ta chọn?
- PARAMETER
- Model tự học
- Học được từ dữ liệu trong quá trình train. Vd: trọng số w, b.
- vs
- HYPERPARAMETER
- Ta chọn trước
- Đặt trước khi train. Vd: learning_rate, max_depth, n_estimators.

### Slide 3

- L19 · GRID SEARCH VS RANDOM SEARCH
- Thử mọi tổ hợp hay thử ngẫu nhiên?
- GRID SEARCH
- Thử mọi tổ hợp
- Đầy đủ nhưng chậm. Tốt khi không gian tham số nhỏ.
- vs
- RANDOM SEARCH
- Thử ngẫu nhiên
- Hiệu quả hơn Grid khi có nhiều tham số, cùng ngân sách thời gian.

### Slide 4

- L19 · BAYESIAN OPTIMIZATION
- Optuna — thử thông minh, học từ lần trước
- optuna_tune.py
- import optuna def objective (trial):
- lr = trial.
- suggest_float("lr", 1e-3, 0.3, log=True )
- return cross_val_score(model(lr), X, y).mean ()
- study = optuna.
- create_study(direction="maximize" )
- study.
- optimize(objective, n_trials=100)
- Học từ các lần thử trước để chọn điểm thử tiếp theo
- Hội tụ tới vùng tốt nhanh hơn
- Optuna là thư viện phổ biến nhất
- Tiết kiệm thời gian đáng kể

### Slide 5

- L19 · TÓM TẮT
- Hyperparameter Tuning
- 01
- Param vs hyperparam
- Model học vs ta chọn
- 02
- Grid & Random
- Thử đủ vs thử ngẫu nhiên
- 03
- Bayesian / Optuna
- Thử thông minh, học từ lần trước
- BÀI TIẾP
- 🏆 Capstone 1 — ráp tất cả vào dự án churn
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_