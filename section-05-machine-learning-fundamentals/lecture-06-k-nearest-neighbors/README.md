# Section 5 · Lecture 6 — K-Nearest Neighbors

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 06 · ~8 PHÚT
- 06
- K-Nearest Neighbors
- khoảng cách · bỏ phiếu · chọn K

### Slide 2

- L06 · NGUYÊN LÝ
- "Bạn là ai = đa số hàng xóm là ai"
- Tìm K điểm gần nhất với điểm cần dự đoán
- Rồi bỏ phiếu theo đa số nhãn
- Không "học" trước — tính ngay lúc dự đoán
- Lazy learning: lưu toàn bộ dữ liệu

### Slide 3

- L06 · ĐO KHOẢNG CÁCH
- Euclid & Manhattan
- EUCLIDEAN · L2
- Đường chim bay
- Khoảng cách thẳng giữa hai điểm — căn bậc hai tổng bình phương sai khác.
- vs
- MANHATTAN · L1
- Đi theo ô bàn cờ
- Tổng trị tuyệt đối các sai khác — di chuyển theo các trục.

### Slide 4

- L06 · CHỌN K
- K quá nhỏ vs quá lớn
- K NHỎ
- Nhạy với nhiễu
- Ranh giới gồ ghề, dễ bị một điểm lạ đánh lừa → overfit.
- ↔
- K LỚN
- Mượt nhưng mờ
- Ranh giới trơn nhưng có thể bỏ qua chi tiết → underfit.
- THỰC HÀNH
- Thử nhiều giá trị K, chọn cái cho điểm tốt nhất trên tập validation.

### Slide 5

- L06 · ƯU / NHƯỢC ĐIỂM
- Đơn giản, nhưng cẩn thận với nhiều chiều
- Ưu điểm
- Đơn giản, trực quan, dễ hiểu
- Không cần giả định về phân phối dữ liệu
- Nhược điểm
- Chậm khi dữ liệu lớn — tính lúc dự đoán
- Kém hiệu quả với nhiều chiều (curse of dimensionality)
- Bắt buộc scale feature trước khi dùng

### Slide 6

- L06 · TÓM TẮT
- K-Nearest Neighbors
- 01
- Hàng xóm
- K điểm gần nhất bỏ phiếu
- 02
- Khoảng cách
- Euclid / Manhattan — cần scale
- 03
- Chọn K
- Cân bằng nhiễu & độ mượt
- BÀI TIẾP
- Decision Tree — model dạng cây quyết định
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_