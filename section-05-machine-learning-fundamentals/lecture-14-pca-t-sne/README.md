# Section 5 · Lecture 14 — PCA & t-SNE

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 14 · ~8 PHÚT
- 14
- PCA & t-SNE
- giảm chiều dữ liệu

### Slide 2

- L14 · VÌ SAO GIẢM CHIỀU
- Nén dữ liệu mà giữ thông tin quan trọng
- TRỰC QUAN HOÁ
- Thấy được
- Ép dữ liệu nhiều chiều xuống 2D/3D để vẽ & quan sát.
- TĂNG TỐC
- Nhẹ hơn
- Ít chiều → model train nhanh hơn, tốn ít bộ nhớ.
- GIẢM NHIỄU
- Sạch hơn
- Bỏ chiều ít thông tin → chống curse of dimensionality .

### Slide 3

- L14 · PCA (ÔN LẠI)
- Giữ hướng có phương sai lớn nhất
- Tìm trục chính theo hướng dữ liệu trải rộng nhất
- Nối lại eigenvector ở Section 4
- Tuyến tính, nhanh — rất hay dùng
- Kết quả dùng được làm feature cho model

### Slide 4

- L14 · T-SNE & UMAP
- Giữ cấu trúc cục bộ — trực quan hoá đẹp
- SCREEN RECORDING
- Bản đồ t-SNE 2D: các chữ số viết tay (MNIST) tự gom thành những cụm màu tách biệt rõ ràng
- Giữ quan hệ "gần nhau" giữa các điểm
- Cho ra bản đồ cụm rất đẹp mắt
- Chỉ dùng để
- xem
- , không dùng làm feature
- Chậm & không tái lập ổn định

### Slide 5

- L14 · PCA VS T-SNE
- Chọn theo mục đích
- PCA
- Nhanh · tuyến tính
- Dùng để giảm chiều làm feature cho model. Tái lập ổn định.
- vs
- T-SNE / UMAP
- Chậm · phi tuyến
- Dùng để trực quan hoá đẹp. Không làm feature.

### Slide 6

- L14 · TÓM TẮT
- PCA & t-SNE
- 01
- Vì sao
- Trực quan · tăng tốc · giảm nhiễu
- 02
- PCA
- Tuyến tính, nhanh, làm feature
- 03
- t-SNE / UMAP
- Phi tuyến, chỉ để trực quan hoá
- BÀI TIẾP
- Association Rules — "mua gì kèm gì"
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_