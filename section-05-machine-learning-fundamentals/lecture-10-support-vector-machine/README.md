# Section 5 · Lecture 10 — Support Vector Machine

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE 10 · ~8 PHÚT
- 10
- Support Vector Machine
- margin · support vector · kernel

### Slide 2

- L10 · SIÊU PHẲNG PHÂN TÁCH
- Có vô số đường chia — chọn đường nào?
- Siêu phẳng = đường (2D) / mặt (nhiều chiều) chia hai lớp
- Tìm ranh giới phân tách "rộng rãi" nhất
- Vô số đường tách được — SVM chọn đường tối ưu
- Tiêu chí: lề (margin) rộng nhất

### Slide 3

- L10 · MARGIN & SUPPORT VECTOR
- Chọn đường có lề rộng nhất
- Margin = khoảng trống hai bên ranh giới
- Lề càng rộng → tổng quát hoá càng tốt
- Support vector
- = các điểm sát lề
- Chỉ vài điểm này quyết định ranh giới

### Slide 4

- L10 · KERNEL TRICK
- Ánh xạ sang chiều cao hơn để tách dữ liệu phi tuyến
- 2D — không tách được
- cụm lồng nhau
- →
- Kernel nâng chiều
- →
- 3D — tách được bằng mặt phẳng
- Một mẹo toán học rất đẹp: tính như đã nâng chiều mà không thực sự nâng chiều.

### Slide 5

- L10 · ƯU / NHƯỢC ĐIỂM
- Mạnh với nhiều chiều, chậm với dữ liệu lớn
- Ưu điểm
- Rất mạnh với dữ liệu nhiều chiều
- Hiệu quả khi số feature lớn
- Nhược điểm
- Chậm với dữ liệu rất lớn
- Khó tinh chỉnh & diễn giải hơn cây
- Hợp dữ liệu vừa, nhiều feature

### Slide 6

- L10 · TÓM TẮT
- Support Vector Machine
- 01
- Margin
- Chọn ranh giới có lề rộng nhất
- 02
- Support vector
- Vài điểm sát lề quyết định ranh giới
- 03
- Kernel
- Nâng chiều để tách phi tuyến
- BÀI TIẾP
- Naive Bayes — model dựa trên xác suất
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_