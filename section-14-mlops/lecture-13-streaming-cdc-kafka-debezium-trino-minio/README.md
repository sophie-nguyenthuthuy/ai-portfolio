# Section 14 · Lecture 13 — Streaming & CDC — Kafka, Debezium, Trino, MinIO

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Streaming & CDC

**🎨 Visual:** `[AI image]` Dòng dữ liệu chảy real-time.
**🎤 Speaker note:** "Dữ liệu thời gian thực — nền cho ML real-time."

### Slide 2 — Batch vs Streaming

- Batch: xử lý theo lô
- Streaming: xử lý liên tục

**🎨 Visual:** `[Mermaid]` So sánh.
**🎤 Speaker note:** Real-time cần streaming.

### Slide 3 — Kafka

- Hàng đợi message phân tán
- Xương sống streaming

**🎨 Visual:** `[Mermaid]` Producer → Kafka → consumer.
**🎤 Speaker note:** Chuẩn ngành cho streaming.

### Slide 4 — CDC & Debezium

- Bắt thay đổi từ database
- Stream vào Kafka

**🎨 Visual:** `[Mermaid]` DB change → Debezium → Kafka.
**🎤 Speaker note:** Đồng bộ dữ liệu real-time.

### Slide 5 — Trino & MinIO

- Trino: truy vấn dữ liệu phân tán
- MinIO: object storage

**🎨 Visual:** `[Mermaid]` Stack lakehouse.
**🎤 Speaker note:** Stack này chị dạy ở bootcamp DE.

### Slide 6 — Tóm tắt & chuyển bài

- Kafka · CDC/Debezium · Trino · MinIO
- Bài tiếp: monitoring →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta giám sát model trong production."

---

_← [Về Section README](../README.md)_
