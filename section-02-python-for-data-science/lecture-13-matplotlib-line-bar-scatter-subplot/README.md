# Section 2 · Lecture 13 — Matplotlib Line, Bar, Scatter & Subplot

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 13
- ~9 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Matplotlib Line, Bar, Scatter & Subplot
- figure / axes
- plot · bar · scatter · hist
- subplot

### Slide 2

- Cấu Trúc Figure / Axes
- Figure
- = khung tổng thể (cửa sổ)
- Axes
- = vùng vẽ thực sự (có trục x, y)
- 1 Figure có thể chứa nhiều Axes (subplot)
- Hiểu cấu trúc giúp tuỳ biến mọi thứ chính xác
- Figure
- Axes
- title · xlabel · ylabel xlim · ylim · legend plot · bar · scatter · hist
- 💡
- Cách OOP: fig, ax = plt.subplots() → tuỳ biến qua ax.set_*() — chuyên nghiệp hơn

### Slide 3

- Các Loại Biểu Đồ Cơ Bản
- plot()
- —
- xu hướng
- theo thời gian (line)
- bar()
- —
- so sánh
- giữa các nhóm
- scatter()
- —
- tương quan
- 2 biến số
- hist()
- —
- phân phối
- của 1 biến
- Mỗi loại trả lời 1 câu hỏi phân tích khác nhau
- charts.py
- import matplotlib.pyplot as  plt fig, ax = plt.subplots() # Line — xu hướng doanh thu ax.plot(thang, doanh_thu, color="#3776AB") # Bar — top 5 sản phẩm ax.bar(san_pham, doanh_so) # Scatter — chi tiêu vs thu nhập ax.scatter(thu_nhap, chi_tieu, alpha=0.5) # Histogram — phân phối tuổi ax.hist(df["tuoi"], bins=20) plt.show()

### Slide 4

- Nhãn, Tiêu Đề & Chú Thích
- ax.set_title()
- — tiêu đề biểu đồ
- ax.set_xlabel() / set_ylabel()
- — nhãn trục
- ax.legend()
- — chú thích
- ax.grid(True)
- — lưới nền
- Biểu đồ
- không có nhãn = vô dụng
- — luôn thêm
- labels.py
- fig, ax = plt.subplots(figsize=(10, 6)) ax.plot(thang, dt_2023, label="2023") ax.plot(thang, dt_2024, label="2024") ax.set_title("Doanh Thu Theo Tháng") ax.set_xlabel("Tháng") ax.set_ylabel("Doanh Thu (triệu đ)") ax.legend() ax.grid(True, alpha=0.3) plt.tight_layout() plt.savefig("chart.png", dpi=150)

### Slide 5

- Subplot — Nhiều Biểu Đồ
- plt.subplots(rows, cols)
- — tạo lưới biểu đồ
- Trả về
- fig
- và mảng
- axes
- Dùng khi cần so sánh nhiều chỉ số cùng lúc
- Tiết kiệm không gian, nhìn thấy toàn cảnh
- subplot.py
- fig, axes = plt.subplots(2, 2 ,
- figsize=(12, 8)) # Top-left axes[0,0].plot(thang, doanh_thu) axes[0,0].set_title("Doanh thu") # Top-right axes[0,1].bar(vung, don_hang) axes[0,1].set_title("Đơn hàng") # Bottom-left axes[1,0].hist(df["tuoi"], bins=20) plt.tight_layout() plt.show()

### Slide 6

- LECTURE 13 — TÓM TẮT
- Matplotlib
- Figure = khung · Axes = vùng vẽ
- plot · bar · scatter · hist — mỗi loại 1 câu hỏi
- title · xlabel · ylabel · legend — luôn thêm nhãn
- subplots(rows, cols) — nhiều biểu đồ cùng lúc
- →
- Bài tiếp: Seaborn — đẹp hơn, ít code hơn

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_