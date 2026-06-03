# Section 5 · Lecture 7 — Decision Tree

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 07 · ~9 PHÚT
- 07
- Decision Tree
- Gini vs Entropy · overfitting & cắt tỉa

### Slide 2

- L07 · CẤU TRÚC CÂY
- Node hỏi · nhánh trả lời · lá kết luận
- Thu nhập > 50tr?
- có →
- Có nợ xấu?
- không →
- Duyệt vay
- có →
- Từ chối
- không →
- Từ chối
- Giống cách con người ra quyết định
- Một chuỗi câu hỏi if-then
- Diễn giải được
- — điểm cộng lớn
- Có thể vẽ ra & giải thích cho stakeholder

### Slide 3

- L07 · CHIA NHÁNH THẾ NÀO
- Chọn câu hỏi tách dữ liệu tốt nhất
- Mỗi bước, thử mọi feature & ngưỡng có thể
- Chọn cách chia làm nhánh con "thuần" nhất
- Mục tiêu: mỗi nhánh càng ít trộn lẫn càng tốt
- Lý tưởng: mỗi lá chỉ chứa một lớp
- TRỰC GIÁC
- "Thuần khiết" = nếu đi tới lá này, gần như chắc chắn biết nhãn là gì.

### Slide 4

- L07 · ĐO ĐỘ "LỘN XỘN"
- Gini vs Entropy
- GINI IMPURITY
- Nhanh, mặc định
- Xác suất phân loại sai nếu gán nhãn ngẫu nhiên theo tỉ lệ lớp.
- ≈
- ENTROPY
- Lý thuyết thông tin
- Đo mức "bất định" — chọn split giảm tạp chất nhiều nhất.
- THỰC TẾ
- Hai cách thường cho kết quả gần như giống nhau — đừng quá bận tâm chọn cái nào.

### Slide 5

- L07 · OVERFITTING & CẮT TỈA
- Cây quá sâu = thuộc lòng dữ liệu
- Cây không giới hạn sẽ chia tới từng mẫu
- Khớp hoàn hảo train nhưng tệ trên dữ liệu mới
- Kiểm soát bằng các tham số cắt tỉa
- max_depth · min_samples_leaf · min_samples_split
- LƯU Ý
- Cây đơn lẻ là model dễ overfit nhất — gần như luôn phải cắt tỉa.

### Slide 6

- L07 · TÓM TẮT
- Decision Tree
- 01
- Cấu trúc
- Node hỏi → nhánh → lá kết luận
- 02
- Gini / Entropy
- Đo độ thuần khi chia nhánh
- 03
- Cắt tỉa
- Kiểm soát overfitting
- BÀI TIẾP
- Random Forest — một cây yếu, nhiều cây mạnh
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_