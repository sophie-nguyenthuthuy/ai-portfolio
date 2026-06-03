# Section 2 · Lecture 18 — Mini-Project Phân Tích Dataset TMĐT Việt Nam

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 18
- ~14 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Mini-Project Phân Tích Dataset TMĐT Việt Nam
- EDA
- Data Cleaning
- groupby
- Visualization
- Insight

### Slide 2

- Bài Toán & Dataset
- Dataset: đơn hàng sàn TMĐT 12 tháng — ~50,000 dòng
- Câu hỏi kinh doanh cần trả lời:
- Danh mục nào doanh thu cao nhất?
- Xu hướng doanh thu theo tháng?
- Khách hàng nào có giá trị cao nhất?
- 💡
- Đặt câu hỏi trước khi phân tích — không phải ngược lại
- 01_explore.py
- import pandas as  pd df = pd.read_csv("tmdt_vn.csv") df.head() # ma_dh  ngay_dat  ma_kh  san_pham  danh_muc  gia  sl  tinh # DH001  2024-01-05  KH123  Laptop  Điện tử  15M   1  HCM # DH002  2024-01-05  KH456  iPhone  Điện tử  25M   1  HN df.info()       # 50,000 rows × 9 cols df.describe()  # thống kê mô tả df.isna().sum()  # đếm null

### Slide 3

- Làm Sạch Dữ Liệu
- Xử lý missing values
- Sửa sai kiểu dữ liệu
- Xoá hàng trùng lặp
- Chuẩn hoá text
- 80% thời gian phân tích là làm sạch — bình thường!
- 02_clean.py
- # 1. Sửa kiểu datetime df["ngay_dat"] = pd.to_datetime(df["ngay_dat"]) # 2. Xử lý missing df.dropna(subset=["gia", "so_luong"], inplace=True) df["tinh"].fillna("Khác", inplace=True) # 3. Xoá trùng lặp df.drop_duplicates(subset="ma_dh", inplace=True) # 4. Tạo cột tính toán df["doanh_thu"] = df["gia"] * df["so_luong"] df["thang"]    = df["ngay_dat"].dt.month print("Còn:", df.shape)

### Slide 4

- Phân Tích Bằng groupby
- Doanh thu theo
- danh mục
- Xu hướng doanh thu theo
- tháng
- Top 10
- khách hàng
- giá trị cao nhất
- Mỗi groupby trả lời 1 câu hỏi kinh doanh
- 03_analyze.py
- # Doanh thu theo danh mục dt_dm = (df     .groupby("danh_muc")["doanh_thu" ]
- .
- sum ()
- .
- sort_values(ascending=False )
- )
- # Xu hướng theo tháng dt_thang = df.groupby("thang")["doanh_thu"].sum() # Top 10 khách hàng top_kh = (df     .groupby("ma_kh" )
- .
- agg(tong=("doanh_thu","sum"), so_don=("ma_dh","count" ))
- .
- nlargest(10, "tong" )
- )

### Slide 5

- Trực Quan Hoá Kết Quả
- Bar chart: doanh thu theo danh mục
- Line chart: xu hướng theo tháng
- Heatmap: doanh thu theo tháng × vùng
- Mỗi biểu đồ kèm
- 1 nhận định
- rõ ràng
- 04_visualize.py
- import plotly.express as px import seaborn as sns # Bar — top danh mục fig1 = px.bar(dt_dm.head(10 ),
- title="Top 10 Danh Mục") fig1.show() # Line — xu hướng tháng fig2 = px.line(dt_thang.reset_index (),
- x="thang", y="doanh_thu" ,
- title="Xu Hướng Doanh Thu") # Heatmap tương quan sns.heatmap(df.corr(numeric_only=True), annot=True)

### Slide 6

- Insight & Kết Luận
- 1
- Điện tử chiếm 42% doanh thu
- Danh mục Điện tử dẫn đầu, đặc biệt tháng 11–12 tăng đột biến do mùa lễ hội
- 2
- HCM + HN chiếm 68% tổng đơn
- 2 thành phố lớn áp đảo — cơ hội phát triển ở miền Trung còn lớn
- 3
- Top 100 KH đóng góp 35% doanh thu
- Tập trung giữ chân nhóm VIP — tỷ lệ ROI tốt nhất
- 🎯
- Đây là kỹ năng Storytelling bằng dữ liệu — insight phải dẫn đến hành động
- 📊
- Mỗi insight đi kèm đề xuất hành động cụ thể cho business

### Slide 7

- Section 2 ✓
- Python cho Data Science — Hoàn Thành!
- Python syntax
- Pandas
- NumPy
- OOP
- Matplotlib
- Seaborn
- Plotly
- Regex
- → Section 3: SQL & Truy Vấn Dữ Liệu

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_