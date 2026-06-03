# Section 5 · Lecture 12 — K-Means clustering + Elbow method

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- K-Means — phân cụm

**🎨 Visual:** `[AI image]` Các điểm gom thành cụm màu.
**🎤 Speaker note:** "Không có nhãn — máy tự tìm nhóm."

### Slide 2 — Bài toán phân cụm

- Gom điểm giống nhau vào nhóm
- Vd: phân khúc khách hàng

**🎨 Visual:** `[Mermaid]` Dữ liệu → cụm.
**🎤 Speaker note:** Ứng dụng marketing rất nhiều.

### Slide 3 — Thuật toán K-Means

- Chọn K tâm → gán điểm → cập nhật tâm → lặp

**🎨 Visual:** `[Mermaid]` 4 bước lặp.
**🎤 Speaker note:** Lặp tới khi tâm ổn định.

### Slide 4 — Chọn K bằng Elbow

- Vẽ inertia theo K
- Chọn "khuỷu tay"

**🎨 Visual:** `[Mermaid]` Đường elbow.
**🎤 Speaker note:** Cũng có silhouette score để hỗ trợ.

### Slide 5 — Hạn chế

- Phải chọn K trước
- Giả định cụm hình cầu

**🎨 Visual:** `[Mermaid]` K-Means thất bại với cụm cong.
**🎤 Speaker note:** Dẫn sang DBSCAN ở bài sau.

### Slide 6 — Tóm tắt & chuyển bài

- K-Means · elbow · hạn chế
- Bài tiếp: DBSCAN & hierarchical →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ học phân cụm không cần chọn K."

---

_← [Về Section README](../README.md)_
