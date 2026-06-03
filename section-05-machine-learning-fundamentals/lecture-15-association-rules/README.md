# Section 5 · Lecture 15 — Association Rules

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- LECTURE 15 · ~7 PHÚT
- 15
- Association Rules
- Apriori · FP-Growth · market basket

### Slide 2

- L15 · BÀI TOÁN
- Tìm sản phẩm hay được mua cùng nhau
- Mua A
- vd: bỉm
- →
- Có xu hướng mua B
- vd: bia
- "Bỉm + bia" — huyền thoại market basket
- Phân tích giỏ hàng siêu thị
- Cơ sở cho gợi ý & sắp xếp kệ hàng
- Bán chéo, bố trí sản phẩm

### Slide 3

- L15 · BA CHỈ SỐ
- Support · Confidence · Lift
- SUPPORT
- Độ phổ biến
- Tần suất tập sản phẩm xuất hiện trong tổng số giao dịch.
- CONFIDENCE
- Độ tin cậy
- Mua A thì khả năng mua B là bao nhiêu.
- LIFT
- Độ liên kết
- Lift > 1 = quan hệ thật, không phải ngẫu nhiên.

### Slide 4

- L15 · THUẬT TOÁN
- Apriori & FP-Growth
- market_basket.py
- from mlxtend.frequent_patterns import  apriori, association_rules
- freq =
- apriori(basket, min_support=0.02 ,
- use_colnames=
- True )
- rules =
- association_rules(freq, metric="lift" ,
- min_threshold=
- 1.0)
- Apriori
- : tìm các tập sản phẩm phổ biến
- Trực quan nhưng có thể chậm
- FP-Growth
- : nhanh hơn cho dữ liệu lớn
- Cùng mục tiêu, thuật toán hiệu quả hơn

### Slide 5

- L15 · TÓM TẮT
- Association Rules
- 01
- Bài toán
- Tìm sản phẩm mua cùng nhau
- 02
- Ba chỉ số
- Support · Confidence · Lift
- 03
- Apriori / FP-Growth
- Tìm tập phổ biến & luật
- BÀI TIẾP
- Recommender System — xây hệ gợi ý đầy đủ
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_