# Section 14 · Lecture 5 — Feature store — Feast, Hopsworks (online vs offline)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5 · ~6 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Feature Store

**🎨 Visual:** `[AI image]` Kho feature dùng chung.
**🎤 Speaker note:** "Tránh tính lại feature ở mỗi nơi — quản lý tập trung."

### Slide 2 — Vấn đề không có feature store

- Train/serve tính feature khác nhau
- Training-serving skew

**🎨 Visual:** `[Mermaid]` Skew giữa train & serve.
**🎤 Speaker note:** Lỗi tinh vi gây model dở trong production.

### Slide 3 — Online vs Offline

- Offline: train (lịch sử)
- Online: serve (real-time)

**🎨 Visual:** `[Mermaid]` 2 store.
**🎤 Speaker note:** Cùng định nghĩa feature, 2 nơi dùng.

### Slide 4 — Feast & Hopsworks

- Feast: nhẹ, mã nguồn mở

**🎨 Visual:** `[Screen]` Feast định nghĩa feature.
**🎤 Speaker note:** Đảm bảo nhất quán train-serve.

### Slide 5 — Tóm tắt & chuyển bài

- feature store · online/offline · skew
- Bài tiếp: orchestration →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tự động hoá toàn pipeline."

---

_← [Về Section README](../README.md)_
