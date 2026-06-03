# Section 2 · Lecture 5 — List vs Tuple Khi Nào Dùng Cái Nào?

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 05
- ~7 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- List vs Tuple Khi Nào Dùng Cái Nào?
- list — mutable
- tuple — immutable
- slicing
- packing / unpacking

### Slide 2

- List — Mutable
- Tạo bằng
- [ ]
- — có thể thay đổi
- Index từ
- 0
- · Index âm từ
- -1
- (cuối)
- Thêm:
- append()
- ,
- insert()
- Xoá:
- remove()
- ,
- pop()
- Dùng khi dữ liệu
- sẽ thay đổi
- list_ops.py
- sp = ["Laptop", "Phone", "Tablet"] sp.append("Watch")      # thêm cuối sp.insert(1, "Pad")    # thêm vị trí 1 sp.remove("Phone")     # xoá theo giá trị sp.pop()                # xoá & trả về cuối sp.pop(0)               # xoá vị trí 0 sp[0] = "Gaming Laptop"  # sửa print(sp[-1])            # phần tử cuối print(len(sp))           # số phần tử

### Slide 3

- Slicing & Sort
- Slicing:
- lst[start:stop:step]
- lst[::-1]
- — đảo ngược list
- lst.sort()
- — sort tại chỗ (in-place)
- sorted(lst)
- — trả list mới
- Slicing dùng
- rất nhiều
- khi xử lý data
- slicing.py
- d = [10, 20, 30, 40, 50, 60] #     0    1    2    3    4    5 d[1:4]    # [20, 30, 40] d[:3]     # [10, 20, 30] d[3:]     # [40, 50, 60] d[::2]    # [10, 30, 50] bước 2 d[::-1]   # [60, 50, 40, 30, 20, 10] d.sort()              # tăng dần, tại chỗ d.sort(reverse=True) # giảm dần sorted(d)             # trả list mới

### Slide 4

- Tuple — Immutable
- Tạo bằng
- ( )
- —
- không thể thay đổi
- Nhanh hơn list, ít tốn bộ nhớ hơn
- Có thể làm
- key trong dict
- (list không được)
- Dùng cho dữ liệu cố định: toạ độ, RGB, hằng số
- tuple.py
- vi_tri = (10.78, 106.70)   # lat, lng mau = (255, 127, 0)          # RGB orange # Truy cập như list print(vi_tri[0])     # 10.78 # Thử sửa → lỗi ngay vi_tri[0] = 11.0 # TypeError: object does not #    support item assignment # Làm key trong dict gia_ve = {("HCM", "HN"): 800_000}

### Slide 5

- Packing & Unpacking
- Packing
- : gom nhiều giá trị vào tuple
- Unpacking
- : tách ra từng biến
- Dùng
- *
- để bắt phần còn lại
- Rất tiện khi hàm trả nhiều giá trị
- unpacking.py
- # Hoán đổi biến (Pythonic) a, b = 10, 20 a, b = b, a    # a=20, b=10 # Unpack kết quả hàm mn, mx, avg = thong_ke(data) # Star unpacking dau, *giua, cuoi = [1,2,3,4,5] # dau=1 · giua=[2,3,4] · cuoi=5 # Unpack trong for pairs = [("A",100), ("B",200)] for ten, gia in pairs :
- print(ten, gia)

### Slide 6

- LECTURE 05 — TÓM TẮT
- List vs Tuple
- Tiêu chí
- list
- tuple
- Có thể thay đổi?
- ✅ Có (mutable)
- 🔒 Không (immutable)
- Tốc độ
- Chậm hơn
- Nhanh hơn
- Dùng làm key dict?
- ❌ Không
- ✅ Được
- Khi nào dùng?
- Dữ liệu hay thay đổi
- Dữ liệu cố định
- →
- Bài tiếp: Dictionary & Set

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_