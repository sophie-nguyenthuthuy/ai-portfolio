# Section 2 · Lecture 3 — Vòng Lặp — for, while, Comprehension & Generator

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 03
- ~10 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Vòng Lặp — for, while, Comprehension & Generator
- for
- while
- break / continue
- List Comprehension
- Generator

### Slide 2

- Vòng Lặp for
- Lặp qua
- list, tuple, chuỗi, range
- Dùng khi biết trước số lần hoặc có tập để duyệt
- range(start, stop, step)
- — sinh dãy số
- enumerate()
- — lấy cả index và giá trị
- zip()
- — lặp song song 2 danh sách
- for_loop.py
- sp = ["Laptop", "Phone", "Tablet"] for item in sp :
- print(item) # range — dãy số for i in range(1, 6 ):
- print(i)    # 1 2 3 4 5 # enumerate — kèm index for i, ten in enumerate(sp ):
- print(i, ten) # zip — song song 2 list for n, g in zip(sp, [999,599,399 ]):
- print(n, g)

### Slide 3

- Vòng Lặp while
- Lặp khi
- điều kiện còn đúng
- Dùng khi không biết trước số lần lặp
- ⚠️ Phải có điều kiện thoát — tránh vòng lặp vô hạn
- Phổ biến: retry logic, đọc streaming data
- Kiểm tra điều kiện
- ↓ True
- Chạy block
- ↑ Lặp lại
- ↓ False
- Thoát vòng lặp
- while_loop.py
- n = 1 while n <= 5 :
- print(n )
- n += 1     # 1 2 3 4 5 # Retry logic thực tế so_lan = 0 while so_lan < 3 :
- ket_qua = goi_api ()
- if ket_qua.ok :
- break      # thoát khi OK     so_lan += 1 # Vòng lặp daemon while True :
- data = doc_stream ()
- if not data: break

### Slide 4

- break & continue
- break
- —
- thoát ngay
- khỏi vòng lặp
- continue
- —
- bỏ qua
- lượt hiện tại, tiếp tục lặp
- Dùng để lọc dữ liệu, tìm kiếm sớm
- Tránh lạm dụng — khó đọc khi lồng sâu
- break_continue.py
- # break — tìm phần tử đầu tiên > 5 for n in [3, 7, 2, 9, 4 ]:
- if n > 5 :
- print("Tìm thấy:", n)  # 7         break # continue — bỏ số chẵn for i in range(1, 9 ):
- if i % 2 == 0 :
- continue     print(i, end=" ")   # 1 3 5 7 # Lọc dữ liệu hợp lệ for row in du_lieu :
- if row["gia"] is None :
- continue     xu_ly(row)

### Slide 5

- List Comprehension
- Viết vòng lặp gọn trong
- 1 dòng
- Nhanh hơn for thông thường ~30–50%
- Cú pháp:
- [expr for x in tập if điều_kiện]
- Dict & set comprehension cũng tương tự
- 💡
- Rất phổ biến trong Pandas: tạo cột mới, lọc dữ liệu theo điều kiện
- comprehension.py
- nums = [1, 2, 3, 4, 5] # For thông thường kq = [] for x in nums :
- kq.append(x**2) # List comprehension — 1 dòng kq = [x**2 for x in nums] # [1, 4, 9, 16, 25] # Kèm điều kiện chan = [x for x in nums if x%2==0] # Dict comprehension bang = {x: x**2 for x in nums}

### Slide 6

- Generator — Lazy Evaluation
- Sinh giá trị
- lười (lazy)
- — không tính trước toàn bộ
- Dùng
- yield
- thay
- return
- Quan trọng: streaming data, pipeline ML lớn
- List — vào RAM hết
- 1M phần tử → ~8MB
- Generator — sinh dần
- 1M phần tử → ~200B
- generator.py
- def binh_phuong(n ):
- for x in range(n ):
- yield x**2   # sinh từng giá trị # Dùng như for bình thường for val in binh_phuong(1_000_000 ):
- xu_ly(val)   # tiết kiệm RAM # Generator expression gen = (x**2 for x in range(10)) next(gen)  # 0 next(gen)   # 1 # So sánh RAM lst = [x**2 for x in range(10)]   # list gen = (x**2 for x in range(10))   # gen

### Slide 7

- LECTURE 03 — TÓM TẮT
- Vòng Lặp
- for — duyệt tập hợp · range · enumerate · zip
- while — lặp theo điều kiện, cần điều kiện thoát
- break / continue — điều khiển luồng lặp
- List comprehension — Pythonic, nhanh hơn
- Generator + yield — lazy, tiết kiệm bộ nhớ
- →
- Bài tiếp: Hàm, Scope, Lambda & Decorator

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_