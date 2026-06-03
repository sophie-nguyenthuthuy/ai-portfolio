# Section 7 · Lecture 10 — Vòng lặp huấn luyện thực tế

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 10
- SECTION 7 · LECTURE 10
- Vòng lặp huấn luyện thực tế
- ~7 phút · 5 slides

### Slide 2

- EPOCH / BATCH
- Epoch vs Batch
- EPOCH
- Một lượt
- Đi qua toàn bộ tập dữ liệu một lần
- BATCH
- Một phần
- Chia nhỏ dữ liệu để train từng bước
- Batch size ảnh hưởng tới tốc độ và bộ nhớ — mỗi epoch gồm nhiều batch.

### Slide 3

- PHẦN CỨNG
- CPU vs GPU
- CPU
- Ít lõi, mạnh tuần tự
- Chậm với ma trận lớn
- vs
- GPU
- Hàng nghìn lõi song song
- Nhanh gấp nhiều lần với ma trận
- Tận dụng GPU miễn phí trên Google Colab.

### Slide 4

- MIXED PRECISION
- float16 để tăng tốc
- amp.py
- scaler = torch.cuda.amp.GradScaler() with torch.autocast("cuda" ):
- loss = criterion(model(xb), yb)
- scaler.scale(loss).backward()
- scaler.step(optimizer); scaler.update()
- Dùng float16 để tăng tốc và tiết kiệm bộ nhớ trên GPU hiện đại.

### Slide 5

- SECTION 7 · LECTURE 10
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- epoch / batch
- GPU
- mixed precision
- BÀI TIẾP THEO
- →
- Debug neural network

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_