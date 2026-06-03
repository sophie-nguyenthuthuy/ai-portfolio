# Section 5 · Lecture 16 — Recommender System

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 16 · ~9 PHÚT
- 16
- Recommender System
- collaborative · content-based · hybrid

### Slide 2

- L16 · CONTENT-BASED
- Gợi ý theo đặc điểm sản phẩm
- Sản phẩm đã thích
- thể loại, từ khoá…
- ↓
- Cosine similarity
- tìm sản phẩm giống
- ↓
- Gợi ý sản phẩm tương tự
- So khớp đặc điểm sản phẩm với sở thích người dùng
- Nối lại cosine similarity ở Section 4
- Không cần dữ liệu người dùng khác
- Hoạt động tốt ngay cả khi ít người dùng

### Slide 3

- L16 · COLLABORATIVE FILTERING
- "Người giống bạn cũng thích…"
- P1
- P2
- P3
- P4
- U1
- 5
- ·
- 4
- ·
- U2
- 5
- 3
- ?
- ·
- U3
- ·
- 3
- 4
- 5
- Dựa trên ma trận user × item (đánh giá)
- Đoán ô "?" từ hành vi người tương tự
- User-based & item-based
- Sức mạnh đến từ hành vi cộng đồng

### Slide 4

- L16 · VẤN ĐỀ COLD START
- User / sản phẩm mới chưa có dữ liệu
- Người dùng mới: chưa từng đánh giá gì
- Không có cơ sở để tìm "người giống"
- Sản phẩm mới: chưa ai tương tác
- Collaborative filtering "bó tay"
- THÁCH THỨC KINH ĐIỂN
- Cold start là bài toán muôn thuở của mọi hệ gợi ý.

### Slide 5

- L16 · HYBRID
- Kết hợp content + collaborative
- Content-based
- +
- Collaborative
- →
- Hybrid
- khắc phục nhược điểm từng loại
- Hệ thống thực tế (Netflix, Shopee, TikTok) gần như luôn là hybrid.

### Slide 6

- L16 · TÓM TẮT
- Recommender System
- 01
- Content-based
- Theo đặc điểm sản phẩm
- 02
- Collaborative
- Theo hành vi cộng đồng
- 03
- Hybrid
- Kết hợp, khắc phục cold start
- BÀI TIẾP
- Feature Engineering — nâng chất lượng đầu vào
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_