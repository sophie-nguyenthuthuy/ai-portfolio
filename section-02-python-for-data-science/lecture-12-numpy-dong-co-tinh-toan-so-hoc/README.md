# Section 2 · Lecture 12 — NumPy — Động Cơ Tính Toán Số Học

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 12
- ~10 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- NumPy — Động Cơ Tính Toán Số Học
- ndarray
- vectorization
- broadcasting
- dot product

### Slide 2

- ndarray vs Python list
- PYTHON LIST — CHẬM, TỐN RAM
- Mỗi phần tử là object riêng biệt
- Lưu pointer đến object — overhead lớn
- Không thể tính toán vector trực tiếp
- Tốt cho: dữ liệu hỗn hợp kiểu
- NUMPY NDARRAY — NHANH, TIẾT KIỆM
- Tất cả cùng 1 kiểu (dtype)
- Lưu liên tục trong bộ nhớ — cache-friendly
- Tính toán vector/ma trận cực nhanh
- Tốt cho: số học, ML, deep learning
- 💡
- NumPy array nhanh hơn list 10–100x cho phép toán số học · Pandas dùng NumPy bên dưới

### Slide 3

- Tạo & Thao Tác Array
- np.array()
- — từ list Python
- np.zeros()
- ,
- np.ones()
- ,
- np.arange()
- np.linspace()
- — dãy đều từ a đến b
- reshape()
- — thay đổi hình dạng
- reshape dùng nhiều khi đưa dữ liệu vào model
- numpy_basics.py
- import numpy as  np a = np.array([1,2,3,4,5]) np.zeros((3, 4))   # ma trận 3×4 toàn 0 np.ones((2, 5))    # ma trận 2×5 toàn 1 np.arange(0, 10, 2)  # [0,2,4,6,8] np.linspace(0, 1, 100)   # 100 điểm # Reshape b = np.arange(12).reshape(3, 4) # [[0,1,2,3],[4,5,6,7],[8,9,10,11]] print(b.shape)   # (3, 4) print(b.dtype)   # int64

### Slide 4

- Vectorization — Không Cần for
- Tính toán trên
- cả array
- — không cần for
- Nhanh hơn for hàng chục lần nhờ C/BLAS backend
- Thấy
- for
- trên số liệu lớn → nghĩ tới vectorize ngay
- 🚀
- 1 triệu phép nhân: for loop ~200ms · vectorized ~1ms → nhanh 200×
- vectorize.py
- prices = np.array([100, 200, 300]) qtys   = np.array([5, 3, 8]) # ❌ For loop — chậm revenue = [] for p, q in zip(prices, qtys ):
- revenue.append(p * q) # ✅ Vectorized — nhanh hơn 200x revenue = prices * qtys # [500, 600, 2400] # Các hàm NumPy np.sqrt(prices)   # căn tất cả np.log(prices)    # log tất cả np.mean(prices)   # trung bình

### Slide 5

- Broadcasting
- Tự động "nở" array kích thước nhỏ hơn
- Tính toán array kích thước khác nhau —
- không cần lặp
- Sẽ gặp lại nhiều trong
- deep learning
- A (3×3)
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- +
- B (1×3)
- 10
- 20
- 30
- =
- Kết quả (3×3)
- 11
- 22
- 33
- 14
- 25
- 36
- 17
- 28
- 39
- broadcasting.py
- A = np.array([[1,2,3 ],
- [
- 4,5,6 ],
- [
- 7,8,9]]) B = np.array([10, 20, 30])   # 1D # B tự "nở" thành 3×3 rồi cộng C = A + B # Chuẩn hoá cột (mean subtraction) X_norm = (X - X.mean(axis=0)) / X.std(axis=0) # Broadcasting trong chuẩn hoá!

### Slide 6

- Dot Product & Ma Trận
- np.dot(A, B)
- hoặc
- A @ B
- — nhân ma trận
- Nền tảng của
- mọi neural network
- A.T
- — transpose ma trận
- Cả deep learning = nhân ma trận lặp lại + activation
- 🧠
- Linear Regression: y = X @ w + b — chỉ là 1 phép nhân ma trận
- matrix.py
- A = np.array([[1,2],[3,4]]) B = np.array([[5,6],[7,8]]) # Nhân ma trận C = np.dot(A, B)   # [[19,22],[43,50]] C = A @ B            # toán tử @ — rõ hơn # Transpose A.T    # [[1,3],[2,4]] # Linear Regression X = np.array([[1,2],[3,4],[5,6]]) w = np.array([0.5, 0.3]) y_pred = X @ w     # [1.1, 2.7, 4.3]

### Slide 7

- LECTURE 12 — TÓM TẮT
- NumPy — Động Cơ Tính Toán
- ndarray đồng nhất kiểu — nhanh hơn list 10–100x
- zeros / ones / arange / linspace / reshape
- Vectorization — không cần for, nhanh hơn 200x
- Broadcasting — tự "nở" array kích thước nhỏ
- A @ B — nhân ma trận, nền tảng Deep Learning
- →
- Bài tiếp: Matplotlib

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_