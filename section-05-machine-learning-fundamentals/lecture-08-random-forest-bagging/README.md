# Section 5 · Lecture 8 — Random Forest & Bagging

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 08 · ~8 PHÚT
- 08
- Random Forest & Bagging
- sức mạnh của số đông

### Slide 2

- L08 · VẤN ĐỀ CỦA MỘT CÂY
- Một cây đơn lẻ dễ dao động mạnh
- Dễ overfit & không ổn định
- Đổi vài mẫu dữ liệu → cây thay đổi hẳn
- Cần một cách giảm
- phương sai
- Ý tưởng: kết hợp nhiều cây lại
- TRỰC GIÁC
- Hỏi một chuyên gia dễ sai lệch; hỏi cả hội đồng thì ổn định hơn.

### Slide 3

- L08 · BAGGING
- Huấn luyện nhiều model trên các mẫu khác nhau
- Dữ liệu gốc
- →
- Mẫu bootstrap 1
- Mẫu bootstrap 2
- Mẫu bootstrap 3
- →
- Tổng hợp
- trung bình / bỏ phiếu
- Bootstrap = lấy mẫu có hoàn lại. Gộp nhiều cây → giảm phương sai, ổn định hơn.

### Slide 4

- L08 · RANDOM FOREST
- Bagging + chọn ngẫu nhiên feature
- Mỗi lần chia nhánh chỉ xét một tập feature ngẫu nhiên
- Khiến các cây khác biệt nhau hơn
- Các cây đa dạng → rừng mạnh & ổn định
- Một trong những model "đáng tin" nhất
- VÌ SAO MẠNH
- Cây càng đa dạng (ít tương quan), việc bỏ phiếu tập thể càng hiệu quả.

### Slide 5

- L08 · FEATURE IMPORTANCE
- Feature nào quan trọng nhất?
- tenure (thâm niên)
- 0.31
- monthly_charges
- 0.25
- contract_type
- 0.18
- total_charges
- 0.13
- tech_support
- 0.07
- Hữu ích để diễn giải model & chọn lọc feature.

### Slide 6

- L08 · TÓM TẮT
- Random Forest & Bagging
- 01
- Bagging
- Nhiều model trên mẫu bootstrap
- 02
- Random Forest
- Bagging + feature ngẫu nhiên
- 03
- Importance
- Đo & diễn giải tầm quan trọng feature
- BÀI TIẾP
- Gradient Boosting — nhà vô địch dữ liệu bảng
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_