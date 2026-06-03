# Section 5 · Lecture 3 — Train / Validation / Test split

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 03 · ~8 PHÚT
- 03
- Train / Validation / Test split
- + cross-validation & chống data leakage

### Slide 2

- L03 · VÌ SAO PHẢI CHIA
- Học bài rồi thi đúng đề = gian lận
- Đánh giá model trên chính dữ liệu đã học → điểm ảo
- Giống học thuộc lòng thay vì hiểu thật
- Cần dữ liệu
- chưa từng thấy
- để chấm công bằng
- Mới biết model có "tổng quát hoá" được không
- AI IMAGE
- Học sinh ngồi thi với một đề hoàn toàn lạ — ẩn dụ cho việc đánh giá trên dữ liệu mới

### Slide 3

- L03 · TRAIN / VALIDATION / TEST
- Ba vai trò của dữ liệu
- Train
- ~70% · để học
- Validation
- ~15% · tinh chỉnh
- Test
- ~15% · chấm cuối
- TRAIN
- Model học quy luật từ phần dữ liệu này.
- VALIDATION
- Tinh chỉnh tham số & chọn model tốt nhất.
- TEST
- Chỉ dùng một lần , cuối cùng, để chấm điểm thật.

### Slide 4

- L03 · CROSS-VALIDATION
- K-fold — luân phiên train & test
- Fold 1
- Fold 2
- Fold 3
- Fold 4
- Fold 5
- Chia dữ liệu thành k phần bằng nhau
- Lần lượt mỗi phần làm tập test (màu tím)
- Đánh giá ổn định hơn, ít phụ thuộc may rủi
- Đặc biệt hữu ích khi dữ liệu ít

### Slide 5

- L03 · DATA LEAKAGE
- Rò rỉ thông tin — lỗi nguy hiểm & khó thấy
- Thông tin từ tập test "rò" vào quá trình train
- Model vô tình thấy trước đáp án
- Kết quả đẹp giả tạo, sụp đổ khi lên production
- Rất khó phát hiện nếu không cẩn thận
- QUY TẮC VÀNG
- Scale & encode phải fit trên tập train trước , rồi mới transform tập test.

### Slide 6

- L03 · TÓM TẮT
- Chia dữ liệu đúng cách
- 01
- Split
- Train / validation / test tách bạch
- 02
- Cross-validation
- K-fold cho đánh giá ổn định
- 03
- Leakage
- Fit trên train trước — tránh rò rỉ
- BÀI TIẾP
- Linear Regression — model đầu tiên
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_