# Section 2 · Lecture 11 — Pandas Phần 2 groupby, merge, pivot & Missing Data

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 11
- ~12 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Pandas Phần 2 groupby, merge, pivot & Missing Data
- groupby
- agg
- merge / join
- pivot_table
- fillna

### Slide 2

- groupby — Split · Apply · Combine
- Gom nhóm + tính tổng hợp —
- cốt lõi phân tích
- Tư duy:
- Split → Apply → Combine
- Ví dụ: doanh thu trung bình theo vùng, tháng
- Tương đương
- GROUP BY
- trong SQL
- Split chia nhóm
- →
- Apply tính toán
- →
- Combine gộp kết quả
- groupby.py
- # Tổng doanh thu theo vùng df.groupby("vung")["doanh_thu"].sum() # Nhiều thống kê cùng lúc df.groupby("vung")["doanh_thu"].agg (
- [
- "mean", "sum", "count", "max" ]
- )
- # Nhóm theo nhiều cột df.groupby(["vung", "thang"])["dt"].sum() # agg với hàm tự viết df.groupby("loai").agg (
- tong=("dt", "sum" ),
- tb=("dt", "mean" )
- )

### Slide 3

- Hàm Tổng Hợp — agg
- Dùng sau
- groupby
- để tính nhiều thống kê
- Các hàm:
- sum
- ·
- mean
- ·
- count
- ·
- min
- ·
- max
- ·
- std
- .agg()
- — nhiều hàm cùng lúc
- Ví dụ: doanh thu trung bình & tổng theo vùng
- agg.py
- # Một hàm df.groupby("vung")["doanh_thu"].mean() # Nhiều hàm cùng lúc df.groupby("vung")["doanh_thu"].agg (
- [
- "sum", "mean", "count", "std" ]
- )
- # Đặt tên cột kết quả df.groupby("vung").agg (
- tong_dt=("doanh_thu", "sum" ),
- tb_dt =("doanh_thu", "mean" ),
- so_don=("ma_dh",    "count" )
- )

### Slide 4

- merge & join — Nối DataFrame
- Nối 2 DataFrame theo
- key chung
- how:
- "inner"
- ·
- "left"
- ·
- "right"
- ·
- "outer"
- Tương đương
- JOIN trong SQL
- merge.py
- # Inner join — chỉ hàng có ở cả 2 ket_qua = df_don.merge (
- df_kh, on="ma_kh", how="inner" ) # Left join — giữ hết df trái ket_qua = df_don.merge (
- df_kh, on="ma_kh", how="left" ) # Merge trên nhiều key ket_qua = df1.merge (
- df2 ,
- on=["ma_sp", "thang" ],
- how="left" )

### Slide 5

- pivot_table — Xoay Dữ Liệu
- Xoay dữ liệu dài → rộng —
- multidimensional summary
- Giống PivotTable trong Excel
- values
- : cột tính ·
- index
- : hàng ·
- columns
- : cột
- Nhanh thấy pattern nhiều chiều
- pivot.py
- # Doanh thu theo vùng × tháng pivot = df.pivot_table (
- values = "doanh_thu" ,
- index  = "vung" ,
- columns= "thang" ,
- aggfunc= "sum" ,
- fill_value=0 ) # Kết quả: # thang    T1     T2     T3 # vung # HCM    500    620    580 # HN     300    280    320 # DN     150    130    160

### Slide 6

- Xử Lý Dữ Liệu Thiếu — Missing Values
- df.isna()
- — phát hiện giá trị null
- df.dropna()
- — xoá hàng có null
- df.fillna()
- — điền giá trị thay thế
- Điền
- median
- tốt hơn mean cho dữ liệu lệch (income, price)
- Điền
- mode
- cho cột categorical
- missing.py
- # Kiểm tra null df.isna().sum()       # đếm null mỗi cột df.isna().mean() * 100   # % null # Xoá hàng có null df.dropna(subset=["gia", "so_luong"]) # Điền median (cho số) trung_vi = df["thu_nhap"].median() df["thu_nhap"].fillna(trung_vi, inplace=True) # Điền mode (cho text) mode = df["tinh"].mode()[0] df["tinh"].fillna(mode, inplace=True)

### Slide 7

- LECTURE 11 — TÓM TẮT
- Pandas Phần 2 — Thực Chiến
- groupby → agg — split/apply/combine
- merge / join — nối DataFrame theo key
- pivot_table — tóm tắt đa chiều
- isna / dropna / fillna — xử lý missing
- Điền median cho số lệch, mode cho categorical
- →
- Bài tiếp: NumPy

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_