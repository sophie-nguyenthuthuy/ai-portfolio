# Section 7 · Lecture 8 — PyTorch cấp tốc

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- 08
- SECTION 7 · LECTURE 8
- PyTorch cấp tốc
- ~10 phút · 7 slides · screen recording

### Slide 2

- TENSOR
- Tensor — khối dữ liệu cơ bản
- tensor.py
- import  torch
- x = torch.tensor([[
- 1., 2.], [3., 4 .]])
- x = x.to(
- "cuda")          # chuyen len GPU print(x.shape, x.device)
- Giống NumPy array + chạy được GPU
- Nối lại tensor ở Section 4

### Slide 3

- AUTOGRAD
- Autograd — tự tính gradient
- autograd.py
- w = torch.tensor(2.0, requires_grad=True )
- loss = (w *
- 3 - 1) ** 2 loss.backward() print(w.grad)             # dloss/dw
- Tự tính gradient qua computational graph
- Gọi .backward() — khỏi tự code backprop

### Slide 4

- NN.MODULE
- Định nghĩa model bằng class
- model.py
- import torch.nn as nn class  MLP(nn.Module):
- def  __init__(self):
- super ().__init__()
- self.net = nn.Sequential(
- nn.Linear(
- 784, 128 ), nn.ReLU(),
- nn.Linear(
- 128, 10 ))
- def  forward(self, x):
- return self.net(x)
- Định nghĩa model bằng class
- Đây là lý do ta học OOP từ Section 2

### Slide 5

- TRAINING LOOP
- Vòng lặp huấn luyện
- train_loop.py
- for epoch in  range(epochs):
- for xb, yb in  loader:
- optimizer.zero_grad()
- loss = criterion(model(xb), yb)
- loss.backward()
- optimizer.step()
- forward → loss → backward → step. Mẫu này lặp lại cho mọi model PyTorch.

### Slide 6

- THƯ VIỆN
- Optimizer & loss có sẵn
- optim.py
- optimizer = torch.optim.Adam(
- model.parameters(), lr=
- 1e-3 )
- criterion = nn.CrossEntropyLoss()
- torch.optim và torch.nn loss
- Mọi thứ đã học đều có sẵn trong thư viện

### Slide 7

- SECTION 7 · LECTURE 8
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- tensor
- autograd
- nn.Module
- training loop
- BÀI TIẾP THEO
- →
- TensorFlow / Keras

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_