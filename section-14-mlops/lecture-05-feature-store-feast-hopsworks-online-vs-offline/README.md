# Section 14 · Lecture 5 — Feature store — Feast, Hopsworks (online vs offline)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 05
- SECTION 14 · LECTURE 05
- Feature store — Feast, Hopsworks (online vs offline)
- ~6 phút · 5 slides

### Slide 2

- L05 · FEATURE STORE
- Khi không có feature store
- Train / serve tính feature khác nhau
- Training–serving skew
- Train ≠ Serve → skew
- lệch định nghĩa feature giữa train và serve gây model dở

### Slide 3

- L05 · FEATURE STORE
- Online vs Offline
- Offline: train (lịch sử)
- Online: serve (real-time)
- OFFLINE
- Train
- dữ liệu lịch sử
- ONLINE
- Serve
- real-time

### Slide 4

- L05 · FEATURE STORE
- Feast & Hopsworks
- Feast: nhẹ, mã nguồn mở
- Đảm bảo nhất quán train–serve
- features.py
- from feast import  FeatureStore
- store =  FeatureStore("." )
- store. get_online_features(...)
- # serve store.get_historical_features(...)  # train

### Slide 5

- L05 · FEATURE STORE — TÓM TẮT
- Tóm tắt
- feature store
- online / offline
- skew
- BÀI TIẾP
- Orchestration
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_