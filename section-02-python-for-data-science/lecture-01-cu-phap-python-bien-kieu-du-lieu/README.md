# Section 2 · Lecture 1 — Cú Pháp Python Biến & Kiểu Dữ Liệu

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 01
- ~9 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Cú Pháp Python Biến & Kiểu Dữ Liệu
- Variables
- Data Types
- Dynamic Typing
- Mutable / Immutable

### Slide 2

- Vì Sao Python Thống Trị AI / Data?
- Python
- Pandas — phân tích & làm sạch dữ liệu
- NumPy — tính toán số học / ma trận
- scikit-learn — Machine Learning
- PyTorch / TensorFlow — Deep Learning
- Matplotlib · Seaborn · Plotly — Visualization
- FastAPI · Streamlit — Deploy & Dashboard
- 💡
- Python thắng vì cộng đồng + hệ sinh thái khổng lồ — không phải vì tốc độ thực thi

### Slide 3

- Biến & Gán Giá Trị
- x = 10
- — không cần khai báo kiểu
- Python
- tự suy kiểu
- —
- dynamic typing
- Tên biến: rõ nghĩa, dùng
- snake_case
- Kiểm tra kiểu bằng
- type()
- ⚠️
- Tránh đặt tên trùng với keyword: list type print
- variables.py
- # Python tự suy kiểu — dynamic typing x           = 10       # int gia         = 99.5    # float ten         = "An"    # str la_hoc_vien = True    # bool # Kiểm tra kiểu print(type(x))      # <class 'int'> print(type(ten))     # <class 'str'> # Gán nhiều biến cùng lúc a, b, c = 1, 2, 3

### Slide 4

- 4 Kiểu Dữ Liệu Cơ Bản
- int
- Số nguyên, không có phần thập phân
- tuoi = 25 count = -3
- float
- Số thực, có phần thập phân
- gia = 99.9 pi = 3.14159
- str
- Chuỗi ký tự trong nháy đơn hoặc kép
- ten = "An" msg = 'Xin chào'
- bool
- Chỉ có True hoặc False
- co_data = True da_chay = False
- 💡
- Ép kiểu: int("5") → 5 · float(3) → 3.0 · str(99) → "99" · bool(0) → False

### Slide 5

- Mutable vs Immutable
- ✏️ MUTABLE — CÓ THỂ THAY ĐỔI
- list → [1, 2, 3]
- dict → {"a": 1}
- set → {1, 2, 3}
- Thay đổi trực tiếp trong bộ nhớ — thêm, xoá, sửa phần tử được
- 🔒 IMMUTABLE — KHÔNG THỂ THAY ĐỔI
- int · float · bool
- str → "hello"
- tuple → (1, 2)
- Mỗi lần "sửa" = tạo object mới trong bộ nhớ
- 🔑
- Immutable = an toàn hơn khi truyền vào hàm · Mutable = linh hoạt khi cần thay đổi dữ liệu

### Slide 6

- LECTURE 01 — TÓM TẮT
- Cú Pháp Python, Biến & Kiểu Dữ Liệu
- Biến & dynamic typing — Python tự suy kiểu
- 4 kiểu cơ bản: int · float · str · bool
- Mutable (list/dict/set) vs Immutable (int/str/tuple)
- Ép kiểu: int() · float() · str() · bool()
- →
- Bài tiếp: Toán Tử & Biểu Thức Điều Kiện

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_