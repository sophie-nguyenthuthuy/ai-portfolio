# Section 2 · Lecture 17 — Regex — Săn Mẫu Trong Văn Bản

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 17
- ~7 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Regex — Săn Mẫu Trong Văn Bản
- pattern
- re.findall
- re.sub
- text cleaning

### Slide 2

- Regex Là Gì?
- Mẫu (pattern) để
- tìm/thay thế chuỗi
- Thư viện
- re
- tích hợp sẵn trong Python
- Ứng dụng: email, số điện thoại, mã đơn hàng
- Bước tiền xử lý quan trọng cho
- NLP
- Trông đáng sợ nhưng chỉ cần nhớ vài ký hiệu
- Input: "Liên hệ: 0909-123-456"
- ↓
- Pattern: r"09d{2}-d{3}-d{3}"
- ↓
- Match: "0909-123-456"

### Slide 3

- Ký Hiệu Cốt Lõi
- KÝ HIỆU
- Ý NGHĨA
- VÍ DỤ MATCH
- d
- Một chữ số 0–9
- ddd → "123"
- w
- Chữ cái / số / _
- w+ → "hello_1"
- s
- Khoảng trắng
- s+ → " "
- .
- Bất kỳ ký tự nào
- a.c → "abc", "a1c"
- +
- 1 lần trở lên
- d+ → "1", "123"
- *
- 0 lần trở lên
- d* → "", "5", "99"
- {n}
- Đúng n lần
- d{4} → "2024"
- [abc]
- Một trong a, b, c
- [aeiou] → nguyên âm

### Slide 4

- Hàm re — Tìm & Thay Thế
- re.search()
- — tìm lần khớp đầu tiên
- re.findall()
- — tìm tất cả lần khớp
- re.sub()
- — thay thế tất cả lần khớp
- re.match()
- — khớp từ đầu chuỗi
- Dùng
- r"..."
- raw string cho pattern
- regex.py
- import  re text = "Email: an@gmail.com, binh@yahoo.com" # findall — tìm tất cả email emails = re.findall(rr"[w.]+@[w.]+.w+", text) # ['an@gmail.com', 'binh@yahoo.com'] # sub — xoá số trong văn bản sach = re.sub(rr"d+", "", "Order123: 4500đ") # "Order: đ" # search — kiểm tra có match không if re.search(rr"09d{8}", text ):
- print("Có số điện thoại")

### Slide 5

- Ví Dụ Thực Tế — Làm Sạch Text
- Tách số điện thoại Việt Nam từ văn bản
- Chuẩn hoá text trước khi làm NLP
- Trích thông tin từ chuỗi lộn xộn
- Kết hợp với Pandas:
- df["col"].str.findall(r"...")
- text_cleaning.py
- import re def lam_sach_text(text ):
- # Xoá ký tự đặc biệt     text = re.sub(rr"[^ws]", " ", text )
- # Xoá số     text = re.sub(rr"d+", "", text )
- # Xoá khoảng trắng thừa     text = re.sub(rr"s+", " ", text).strip ()
- return text.lower() # Dùng với Pandas df["review_sach"] = df["review"].apply(lam_sach_text)

### Slide 6

- LECTURE 17 — TÓM TẮT
- Regex
- Regex = pattern để tìm/thay thế chuỗi
- d số · w chữ/số · . bất kỳ · + nhiều · {n} n lần
- re.findall — tìm tất cả · re.sub — thay thế
- Kết hợp Pandas: df["col"].str.findall()
- →
- Bài tiếp: Mini-Project — Phân tích TMĐT Việt Nam

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_