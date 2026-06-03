# Section 2 · Lecture 10 — Pandas Phần 1 Series, DataFrame & Indexing

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 10
- ~11 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Pandas Phần 1 Series, DataFrame & Indexing
- Series
- DataFrame
- read_csv
- loc / iloc
- Boolean indexing

### Slide 2

- Series vs DataFrame
- SERIES — 1 CỘT
- Index
- doanh_thu
- 0
- 500
- 1
- 300
- 2
- 150
- 1 chiều · dtype đồng nhất · nhanh
- DATAFRAME — BẢNG NHIỀU CỘT
- idx
- vung
- doanh_thu
- don_hang
- 0
- HCM
- 500
- 1200
- 1
- HN
- 300
- 800
- 2
- DN
- 150
- 350
- 2 chiều · nhiều kiểu cột · hình dung như Excel

### Slide 3

- Đọc Dữ Liệu & Khám Phá Ban Đầu
- pd.read_csv()
- ,
- read_excel()
- ,
- read_json()
- .head(n)
- — n dòng đầu (mặc định 5)
- .info()
- — kiểu dữ liệu, giá trị null
- .describe()
- — thống kê mô tả
- 3 lệnh đầu tiên với
- mọi dataset mới
- explore.py
- import pandas as  pd df = pd.read_csv("don_hang.csv") df.head(10)    # 10 dòng đầu df.tail(5)     # 5 dòng cuối df.info()      # kiểu dữ liệu + null df.describe()  # min, max, mean, std df.shape       # (rows, cols) df.columns      # danh sách cột # Chọn cột df["gia"]               # 1 cột → Series df[["gia", "so_luong"]] # nhiều cột → DF

### Slide 4

- Boolean Indexing — Lọc Dữ Liệu
- Lọc dòng theo điều kiện —
- boolean indexing
- Kết hợp:
- &
- (and) ·
- |
- (or) ·
- ~
- (not)
- .isin()
- — lọc theo danh sách giá trị
- Dùng
- cực nhiều
- trong mọi bài phân tích
- filter.py
- # Lọc theo 1 điều kiện cao_tuoi = df[df["tuoi"] > 30] # Kết hợp điều kiện vip_hcm = df [
- (
- df["chi_tieu"] >= 10_000_000 ) &
- (
- df["vung"] == "HCM" )
- ]
- # isin — lọc nhiều giá trị mien_bac = df[df["tinh"].isin (
- [
- "Hà Nội", "HP", "QB" ]
- )]
- # Loại bỏ hàng null sach = df[df["gia"].notna()]

### Slide 5

- loc vs iloc
- Tiêu chí
- .loc[ ]
- .iloc[ ]
- Truy cập theo
- Nhãn (label) — tên cột/index
- Vị trí số — 0, 1, 2...
- Stop index
- Bao gồm điểm dừng
- Không bao gồm (như Python)
- Ví dụ hàng
- df.loc[0:3, "ten"]
- df.iloc[0:3, 2]
- Dùng khi nào
- Biết tên cột/index
- Cần vị trí số tuyệt đối
- 🎯
- Câu hỏi phỏng vấn kinh điển — loc vs iloc: sự khác biệt quan trọng nhất là label-based vs position-based

### Slide 6

- Thêm / Sửa / Xoá Cột
- Tạo cột mới từ cột cũ —
- feature engineering
- df["cot_moi"] = biểu_thức
- df.drop("cot", axis=1)
- — xoá cột
- Đây là bước đầu của
- feature engineering
- columns.py
- # Tạo cột tính toán df["doanh_thu"] = df["gia"] * df["so_luong"] df["gia_vat"] = df["gia"] * 1.1 # Cột phân loại df["phan_khuc"] = df["chi_tieu"].apply (
- lambda x: "VIP" if x>=10e6 else "Std" ) # Đổi tên cột df.rename(columns={"old":"new"}, inplace=True) # Xoá cột df.drop(["cot_thua"], axis=1, inplace=True)

### Slide 7

- LECTURE 10 — TÓM TẮT
- Pandas Phần 1
- Series (1 cột) vs DataFrame (bảng)
- read_csv · head · info · describe
- Boolean indexing — lọc theo điều kiện
- loc (nhãn) vs iloc (vị trí)
- Thêm/sửa/xoá cột — feature engineering
- →
- Bài tiếp: Pandas Phần 2 — groupby, merge, pivot

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_