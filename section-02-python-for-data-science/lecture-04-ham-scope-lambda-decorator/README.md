# Section 2 · Lecture 4 — Hàm, Scope, Lambda & Decorator

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 04
- ~10 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Hàm, Scope, Lambda & Decorator
- def / return
- *args / **kwargs
- Scope
- lambda
- @decorator

### Slide 2

- Định Nghĩa Hàm
- def
- khai báo ·
- return
- trả kết quả
- Parameter
- = biến trong def hàm
- Argument
- = giá trị truyền khi gọi
- Không có
- return
- = trả về
- None
- Hàm = viết một lần, dùng mãi mãi
- functions.py
- def tinh_doanh_thu(gia, so_luong ):
- return gia *  so_luong dt = tinh_doanh_thu(150_000, 20) print(dt)   # 3_000_000 # Trả nhiều giá trị (tuple) def thong_ke(data ):
- return min(data), max(data), sum(data)/len(data) mn, mx, avg = thong_ke([3,7,2,9]) print(mn, mx, avg)  # 2 9 5.25

### Slide 3

- Tham Số Mặc Định & *args / **kwargs
- Tham số mặc định → không bắt buộc truyền
- *args
- — nhiều argument tuỳ ý →
- tuple
- **kwargs
- — keyword arguments →
- dict
- Giúp hàm linh hoạt, tái sử dụng tốt
- args_kwargs.py
- # Tham số mặc định def chao(ten, loi="Xin chào" ):
- print(loi, ten) chao("An")            # Xin chào An chao("Bình", "Hola")   # Hola Bình # *args — nhận nhiều số def tong(*args ):
- return sum(args) tong(1, 2, 3, 4)    # 10 # **kwargs — keyword def profile(**kw ):
- for k, v in kw.items(): print(k, v) profile(ten="An", tuoi=25)

### Slide 4

- Scope — Phạm Vi Biến
- Global Scope — sống toàn chương trình
- TEN_APP = "DS Platform"
- Local Scope — bên trong hàm
- def tinh_vat(gia):
- vat = gia * 0.1 # chỉ sống trong hàm
- return vat
- print(vat) → NameError!
- ⚠️
- Lỗi scope là bug phổ biến nhất với người mới · Hạn chế dùng global — khó debug

### Slide 5

- Lambda — Hàm Ẩn Danh
- Hàm 1 dòng — không cần đặt tên
- Cú pháp:
- lambda tham_so: bieu_thuc
- Hay dùng với
- sorted()
- ,
- map()
- ,
- filter()
- Gọn cho hàm nhỏ, dùng 1 lần
- lambda.py
- # Hàm thường vs lambda def nhan_doi(x): return x * 2 nhan_doi = lambda x: x * 2 # Sort theo giá — thực tế nhất sp  = [
- {
- "ten":"A", "gia":300 },
- {
- "ten":"B", "gia":150 },
- ]
- sp.sort(key=lambda x: x["gia"]) # map, filter gia_vat = list(map(lambda x: x*1.1, [100,200])) dat = list(filter(lambda x: x>150, [100,200,300]))

### Slide 6

- Decorator — Hàm Bọc Hàm
- Hàm
- bọc ngoài hàm khác
- — thêm tính năng
- Cú pháp:
- @ten_decorator
- phía trên def
- Ứng dụng: logging, timing, caching, auth
- Gặp lại ở
- FastAPI
- — @app.get("/"), @app.post()
- @timer
- ↓
- wrapper(*args, **kwargs)
- ↓
- gọi hàm gốc bên trong
- decorator.py
- import time def timer(func ):
- def wrapper(*args, **kwargs ):
- t0 = time.time ()
- result = func(*args, **kwargs )
- print(time.time()-t0, "giây" )
- return result     return wrapper @timer def xu_ly_du_lieu(df ):
- return df.groupby("nhom").sum() xu_ly_du_lieu(df)  # in thời gian tự động

### Slide 7

- LECTURE 04 — TÓM TẮT
- Hàm, Scope, Lambda & Decorator
- def / return · parameter vs argument
- *args / **kwargs — tham số linh hoạt
- Scope: local vs global
- lambda — hàm ẩn danh 1 dòng
- @decorator — bọc hàm thêm tính năng
- →
- Bài tiếp: List vs Tuple

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_