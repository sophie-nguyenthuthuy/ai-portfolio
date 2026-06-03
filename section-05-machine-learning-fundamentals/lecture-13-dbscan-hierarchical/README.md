# Section 5 · Lecture 13 — DBSCAN & Hierarchical

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- LECTURE 13 · ~7 PHÚT
- 13
- DBSCAN & Hierarchical
- phân cụm theo mật độ · dendrogram

### Slide 2

- L13 · DBSCAN
- Phân cụm theo mật độ — tự bắt nhiễu
- Tự phát hiện số cụm — không cần chọn K
- Bắt được cụm hình cong bất kỳ
- Tự đánh dấu điểm nhiễu (outlier)
- Điểm ở vùng mật độ thấp

### Slide 3

- L13 · THAM SỐ DBSCAN
- Hai núm vặn: eps & min_samples
- EPS
- Bán kính lân cận
- Khoảng cách tối đa để hai điểm được coi là "gần nhau".
- +
- MIN_SAMPLES
- Mật độ tối thiểu
- Số điểm tối thiểu trong bán kính để tạo thành một cụm.
- LƯU Ý
- Chọn hai tham số này là phần khó nhất khi dùng DBSCAN.

### Slide 4

- L13 · HIERARCHICAL CLUSTERING
- Gom dần thành cây — dendrogram
- Gom các điểm/cụm gần nhau dần thành cây
- Trực quan, thấy cấu trúc lồng nhau
- Cắt cây ở độ cao mong muốn để lấy số cụm
- Không cần định trước K

### Slide 5

- L13 · TÓM TẮT
- DBSCAN & Hierarchical
- 01
- DBSCAN
- Phân cụm theo mật độ, bắt nhiễu
- 02
- eps · min_samples
- Hai tham số then chốt
- 03
- Dendrogram
- Cắt cây để chọn số cụm
- BÀI TIẾP
- PCA & t-SNE — giảm chiều để thấy & tăng tốc
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_