# Section 7 · Lecture 11 — Debug neural network

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 11
- SECTION 7 · LECTURE 11
- Debug neural network
- ~8 phút · 6 slides

### Slide 2

- LOSS PHẲNG
- Khi loss không giảm
- Learning rate đặt sai
- Quên scale dữ liệu đầu vào
- Kiểm tra lr & dữ liệu trước tiên

### Slide 3

- NAN
- Khi loss = NaN
- clip.py
- loss.backward()
- torch.nn.utils.clip_grad_norm_(
- model.parameters(), max_norm=
- 1.0 )
- optimizer.step()
- NaN gần như luôn do lr quá lớn / exploding gradient → dùng gradient clipping.

### Slide 4

- OVERFIT
- Overfit train, dở test
- Thêm regularization
- Thêm dữ liệu / augmentation

### Slide 5

- QUY TRÌNH
- Checklist debug
- Overfit một batch nhỏ trước
- ↓
- Kiểm tra shape & dữ liệu đầu vào
- ↓
- Điều chỉnh learning rate
- ↓
- Thêm regularization nếu overfit
- Mẹo: nếu không overfit nổi một batch nhỏ → gần như chắc chắn code có bug.

### Slide 6

- SECTION 7 · LECTURE 11
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- loss phẳng / NaN
- overfitting
- checklist debug
- BÀI TIẾP THEO
- →
- 🏆 Mini-Project: MLP from scratch

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_