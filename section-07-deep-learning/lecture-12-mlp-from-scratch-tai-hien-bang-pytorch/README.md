# Section 7 · Lecture 12 — MLP from scratch + tái hiện bằng PyTorch 🏆 **Capstone**

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 8

---

## Nội dung slide

### Slide 1

- 🏆
- SECTION 7 · MINI-PROJECT 🏆
- MLP from scratch + tái hiện bằng PyTorch
- ~13 phút · 7 slides · screen recording

### Slide 2

- MỤC TIÊU
- Hai phần của dự án
- PHẦN 1
- NumPy
- Cài forward + backward bằng tay
- PHẦN 2
- PyTorch
- Tái hiện bằng nn.Module
- So sánh hai cách để thấy rõ giá trị của framework.

### Slide 3

- PHẦN 1
- MLP from scratch — NumPy
- mlp_numpy.py
- z1 = x @ W1 + b1;  a1 = np.maximum(0 , z1)
- z2 = a1 @ W2 + b2; out = softmax(z2)
- loss = cross_entropy(out, y)
- # ... backprop thu cong + cap nhat W, b
- Áp dụng toàn bộ những gì đã học ở Section 7.

### Slide 4

- PHẦN 2
- Tái hiện bằng PyTorch
- mlp_torch.py
- model = MLP()
- opt   = torch.optim.Adam(model.parameters())
- for xb, yb in  loader:
- opt.zero_grad()
- loss = F.cross_entropy(model(xb), yb)
- loss.backward(); opt.step()
- Ít code hơn nhiều — autograd lo toàn bộ phần backprop.

### Slide 5

- THEO DÕI
- Huấn luyện & theo dõi
- Vẽ loss / accuracy curve
- Đọc curve để đánh giá quá trình học

### Slide 6

- BÀI HỌC
- So sánh & bài học
- NUMPY FROM SCRATCH
- PYTORCH
- Dòng code
- Nhiều, thủ công
- Ngắn gọn
- Backprop
- Tự cài chain rule
- autograd tự động
- Giá trị
- Hiểu bản chất
- Làm việc hiệu quả

### Slide 7

- DEEP LEARNING ✓
- Section 7 hoàn thành
- Neural network từ nền tảng đến PyTorch · Mini-Project MLP from scratch
- SECTION TIẾP THEO
- →
- Section 8 · Computer Vision

### Slide 8

- TIẾN ĐỘ KHOÁ HỌC
- 91 / 198 lectures hoàn thành
- BATCH
- SECTION
- LECTURES
- TRẠNG THÁI
- 1–4
- S1 → S5
- 70
- ✓ Hoàn thành
- 5
- S6 Time Series + S7 Deep Learning
- 21
- ✓ Hoàn thành
- 6
- S8 Computer Vision
- 16
- Tiếp theo
- 7–10
- S9 → S16
- 91
- Sắp tới

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_