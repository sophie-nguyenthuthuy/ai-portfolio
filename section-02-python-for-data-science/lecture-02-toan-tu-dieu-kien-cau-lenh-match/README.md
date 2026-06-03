# Section 2 · Lecture 2 — Toán Tử, Điều Kiện & Câu Lệnh Match

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 02
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Toán Tử, Điều Kiện & Câu Lệnh Match
- Operators
- if / elif / else
- match (Python 3.10+)

### Slide 2

- Các Loại Toán Tử
- SỐ HỌC
- +
- -
- *
- /
- //
- %
- **
- //
- chia nguyên:
- 7//2 = 3
- %
- chia dư:
- 7%2 = 1
- **
- luỹ thừa:
- 2**8 = 256
- SO SÁNH
- ==
- !=
- <
- >
- <=
- >=
- Luôn trả về
- bool
- (True/False)
- Dùng trong điều kiện if
- LOGIC
- and
- or
- not
- and
- — cả hai đúng mới True
- or
- — ít nhất một đúng là True
- not
- — đảo ngược kết quả

### Slide 3

- if / elif / else
- Cấu trúc
- rẽ nhánh
- — ra quyết định
- Indent
- quyết định khối lệnh — sai indent = lỗi ngay
- Python dùng indent thay cho
- {}
- Nhiều
- elif
- liên tiếp được
- Ternary:
- x if điều_kiện else y
- conditions.py
- diem = 78 if diem >= 90 :
- print("Xuất sắc") elif diem >= 75 :
- print("Giỏi")       # ← chạy dòng này elif diem >= 60 :
- print("Trung bình") else :
- print("Cần cố gắng") # Ternary (1 dòng) loai = "Đậu" if diem >= 50 else "Rớt"

### Slide 4

- Ví Dụ Thực Tế — Phân Khúc Khách Hàng
- Bài toán: phân loại theo
- chi tiêu/tháng
- VIP → ≥ 10 triệu
- Tiềm năng → 3–10 triệu
- Phổ thông → dưới 3 triệu
- Ứng dụng: banking, e-commerce, loyalty program
- 💡
- Đây là bước đầu của Customer Segmentation — bài toán cốt lõi Data Science
- segmentation.py
- def phan_khuc(chi_tieu ):
- if chi_tieu >= 10_000_000 :
- return "VIP"     elif chi_tieu >= 3_000_000 :
- return "Tiềm năng"     else :
- return "Phổ thông" print(phan_khuc(12_500_000)) # VIP print(phan_khuc(4_200_000))  # Tiềm năng print(phan_khuc(900_000))   # Phổ thông

### Slide 5

- Câu Lệnh match (Python 3.10+)
- Thay thế nhiều if-elif —
- gọn & rõ hơn
- Case
- _
- = default (giống else)
- Hoạt động với số, chuỗi, tuple, class
- Mạnh hơn if-elif nhiều: hỗ trợ pattern phức tạp
- match.py
- trang_thai = "pending" match trang_thai :
- case "success" :
- print("✅ Đơn hàng thành công" )
- case "pending" :
- print("⏳ Đang xử lý")  # ← chạy     case "failed" :
- print("❌ Giao dịch thất bại" )
- case "refunded" :
- print("↩️ Hoàn tiền" )
- case  _:
- print("❓ Không xác định")

### Slide 6

- LECTURE 02 — TÓM TẮT
- Toán Tử, Điều Kiện & Match
- 3 nhóm: số học · so sánh · logic
- if / elif / else — indent quyết định khối
- Phân khúc khách hàng — ứng dụng thực tế
- match — gọn hơn cho nhiều case (Python 3.10+)
- →
- Bài tiếp: Vòng Lặp

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_