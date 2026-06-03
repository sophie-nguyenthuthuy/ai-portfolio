# Section 14 · Lecture 6 — Orchestration — Airflow, Prefect, Dagster

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Workflow Orchestration

**🎨 Visual:** `[AI image]` Pipeline tự động chạy theo lịch.
**🎤 Speaker note:** "Tự động hoá: data → train → deploy chạy theo lịch."

### Slide 2 — Vì sao orchestration

- Không chạy thủ công từng bước
- Lập lịch, retry, theo dõi

**🎨 Visual:** `[Mermaid]` Thủ công vs tự động.
**🎤 Speaker note:** Pipeline production phải tự chạy.

### Slide 3 — DAG

- Đồ thị các task phụ thuộc
- Task → task → task

**🎨 Visual:** `[Mermaid]` DAG mẫu.
**🎤 Speaker note:** Mỗi bước là 1 task trong DAG.

### Slide 4 — Airflow

- Chuẩn ngành, lập lịch mạnh

**🎨 Visual:** `[Screen]` Airflow DAG UI.
**🎤 Speaker note:** Phổ biến nhất, nhiều doanh nghiệp dùng.

### Slide 5 — Prefect & Dagster

- Hiện đại hơn, dev experience tốt

**🎨 Visual:** `[Mermaid]` So sánh.
**🎤 Speaker note:** Lựa chọn mới, dễ dùng hơn.

### Slide 6 — Tóm tắt & chuyển bài

- orchestration · DAG · Airflow/Prefect
- Bài tiếp: CI/CD →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta tự động test & deploy code ML."

---

_← [Về Section README](../README.md)_
