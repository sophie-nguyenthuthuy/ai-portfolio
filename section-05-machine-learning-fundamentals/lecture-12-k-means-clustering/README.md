# Section 5 · Lecture 12 — K-Means Clustering

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 12 · ~8 PHÚT · UNSUPERVISED
- 12
- K-Means Clustering
- thuật toán lặp · Elbow method

### Slide 2

- L12 · BÀI TOÁN PHÂN CỤM
- Gom các điểm giống nhau — không cần nhãn
- Tự tìm nhóm tự nhiên trong dữ liệu thô
- Máy phát hiện cấu trúc, không ai gán nhãn
- Ứng dụng phổ biến: phân khúc khách hàng
- Rất nhiều trong marketing

### Slide 3

- L12 · THUẬT TOÁN K-MEANS
- Bốn bước lặp tới khi tâm ổn định
- 1 · Chọn K tâm
- khởi tạo ngẫu nhiên
- →
- 2 · Gán điểm
- về tâm gần nhất
- →
- 3 · Cập nhật tâm
- = trung bình cụm
- ↺
- 4 · Lặp lại

### Slide 4

- L12 · CHỌN K BẰNG ELBOW
- Tìm "khuỷu tay" của đường inertia
- Vẽ inertia (tổng khoảng cách trong cụm) theo K
- Inertia luôn giảm khi K tăng
- Chọn K tại điểm "gãy khuỷu"
- Cũng có silhouette score để hỗ trợ

### Slide 5

- L12 · HẠN CHẾ
- Phải chọn K & giả định cụm hình cầu
- Bắt buộc chọn số cụm K trước
- Không phải lúc nào cũng biết K
- Giả định cụm tròn, kích thước đều
- Thất bại với cụm cong / mật độ khác nhau
- DẪN SANG BÀI SAU
- DBSCAN giải quyết được cụm hình dạng bất kỳ & không cần chọn K.

### Slide 6

- L12 · TÓM TẮT
- K-Means Clustering
- 01
- Thuật toán
- Gán điểm → cập nhật tâm → lặp
- 02
- Elbow
- Chọn K tại điểm gãy khuỷu
- 03
- Hạn chế
- Cần chọn K, giả định cụm cầu
- BÀI TIẾP
- DBSCAN & Hierarchical — phân cụm không cần chọn K
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_