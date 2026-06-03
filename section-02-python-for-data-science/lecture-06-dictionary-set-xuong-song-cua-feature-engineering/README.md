# Section 2 · Lecture 6 — Dictionary & Set Xương Sống của Feature Engineering

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 06
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Dictionary & Set Xương Sống của Feature Engineering
- dict — key/value
- set — không trùng
- set operations

### Slide 2

- Dictionary — Key → Value
- Cặp
- key → value
- · tra cứu O(1) cực nhanh
- Key phải immutable · Value bất kỳ kiểu
- Ứng dụng: mã SP → giá, encoding nhãn
- "ten"
- "tuoi"
- "luong"
- →
- "An"
- 25
- 15_000_000
- dict.py
- nv  = {
- "ten"  : "An" ,
- "tuoi": 25 ,
- "luong": 15_000_000 } print(nv["ten"])            # "An" print(nv.get("dc", "N/A"))  # "N/A" nv["phong"] = "Data"          # thêm del nv["tuoi"]               # xoá print("ten" in nv)           # True

### Slide 3

- Thao Tác Dictionary
- .keys()
- — danh sách keys
- .values()
- — danh sách values
- .items()
- — danh sách (key, value) pairs
- Dict comprehension:
- {k: v*1.1 for k,v in d.items()}
- Gộp dict (Python 3.9+):
- d1 | d2
- dict_ops.py
- dt = {"HCM":500, "HN":300, "DN":150} # Duyệt for vung, tri in dt.items ():
- print(vung, "→", tri) # Dict comprehension co_vnd = {k: v*1_000_000            for k, v in dt.items()} # Gộp 2 dict them = {"CT": 80, "VT": 60} tat_ca = dt | them   # Python 3.9+ # defaultdict — tránh KeyError from collections import defaultdict d = defaultdict(int)

### Slide 4

- Set — Tập Hợp Không Trùng
- Tạo bằng
- { }
- hoặc
- set()
- — không có thứ tự, không trùng
- Tra cứu, thêm, xoá rất nhanh O(1)
- Mẹo:
- list(set(lst))
- để khử trùng nhanh
- set.py
- kh = ["An","Bình","An","Cường"] unique = set(kh) # {'An', 'Bình', 'Cường'} # Khử trùng trong list sach = list(set(kh)) s = {1, 2, 3, 4} s.add(5) s.discard(2)  # xoá, không lỗi 3 in s         # True — cực nhanh

### Slide 5

- Phép Toán Tập Hợp
- Hợp
- A | B
- — tất cả phần tử
- Giao
- A & B
- — phần chung
- Hiệu
- A - B
- — A trừ đi B
- Ứng dụng: so sánh tập khách hàng, loyalty
- set_ops.py
- t1 = {"An","Bình","Cường","Dung"} t2 = {"Bình","Dung","Hiếu"} # Hợp — tất cả khách hàng t1 | t2 # {'An','Bình','Cường','Dung','Hiếu'} # Giao — loyal cả 2 tháng t1 & t2     # {'Bình', 'Dung'} # Hiệu — chỉ mua tháng 1 (churn?) t1 - t2    # {'An', 'Cường'}

### Slide 6

- LECTURE 06 — TÓM TẮT
- Dictionary & Set
- dict = key/value · tra cứu O(1)
- .get() an toàn · .items() để duyệt · dict comprehension
- set = không trùng · khử duplicate nhanh
- union | · intersection & · difference -
- →
- Bài tiếp: Lập Trình Hướng Đối Tượng (OOP)

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_