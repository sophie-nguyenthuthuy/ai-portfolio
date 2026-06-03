# Section 2 · Lecture 9 — Đọc/Ghi File, Xử Lý Lỗi & Context Manager

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 09
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Đọc/Ghi File, Xử Lý Lỗi & Context Manager
- open() / read / write
- with statement
- try / except / finally

### Slide 2

- Đọc & Ghi File
- open(path, mode)
- mở file
- Mode:
- "r"
- đọc ·
- "w"
- ghi đè ·
- "a"
- ghi thêm
- ⚠️ Mode
- "w"
- xoá toàn bộ nội dung cũ
- Thêm
- "b"
- cho file nhị phân (ảnh, PDF)
- file_io.py
- # Đọc file f = open("data.txt", "r", encoding="utf-8") noi_dung = f.read()    # toàn bộ dong = f.readlines()  # danh sách dòng f.close()                # đóng file # Ghi file f = open("output.txt", "w", encoding="utf-8") f.write( "Xin chào Data Science!
- "
- ) f.close()               # phải đóng!

### Slide 3

- Context Manager — with
- with open(...) as f:
- — tự đóng file an toàn
- Dù có lỗi xảy ra, file vẫn được đóng
- Luôn dùng with
- — tránh quên đóng file, tránh memory leak
- Context manager hoạt động với database, lock, network...
- context.py
- # ❌ Không dùng with — dễ quên đóng f = open("data.txt") noi_dung = f.read() f.close()    # quên → resource leak! # ✅ Dùng with — tự đóng with open("data.txt", encoding="utf-8") as f :
- noi_dung = f.read() # file tự đóng khi thoát block # Đọc từng dòng (tiết kiệm RAM) with open("big.csv") as f :
- for line in f :
- xu_ly(line.strip())

### Slide 4

- Xử Lý Lỗi — try / except
- try
- — thử chạy code có thể lỗi
- except
- — bắt lỗi, không để chương trình crash
- finally
- — luôn chạy dù có lỗi hay không
- Code production
- không được sập
- vì 1 lỗi nhỏ
- try block
- ↓ thành công
- tiếp tục
- ↓ lỗi
- except block
- ↓ luôn
- finally block
- error_handling.py
- try :
- with open("data.csv") as f :
- df = pd.read_csv(f) except FileNotFoundError :
- print("❌ Không tìm thấy file") except ValueError as e :
- print("Giá trị sai:", e) except Exception as e :
- print("Lỗi không xác định:", e) finally :
- print("✅ Luôn chạy — dọn dẹp")

### Slide 5

- Các Lỗi Thường Gặp
- FileNotFoundError
- — file không tồn tại
- ValueError
- — sai giá trị (vd: int("abc"))
- KeyError
- — key không tồn tại trong dict
- TypeError
- — sai kiểu dữ liệu
- Đọc thông báo lỗi
- = kỹ năng debug số 1
- common_errors.py
- # ValueError int("abc")    # ValueError: invalid literal # KeyError d = {"a": 1} d["b"]       # KeyError: 'b' d.get("b", 0)  # 0 — an toàn # TypeError "hello" + 5   # TypeError: + str, int # IndexError lst = [1,2,3] lst[10]     # IndexError: out of range

### Slide 6

- LECTURE 09 — TÓM TẮT
- File I/O, Xử Lý Lỗi & Context Manager
- open() với mode r / w / a
- with — luôn đóng file an toàn
- try / except / finally — không để crash
- Đọc thông báo lỗi — kỹ năng debug số 1
- →
- Bài tiếp: Pandas Phần 1

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_