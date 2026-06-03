# Section 2 · Lecture 16 — Ngày Tháng & Time-series trong Pandas

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 16
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Ngày Tháng & Time-series trong Pandas
- datetime
- .dt accessor
- resample
- rolling window

### Slide 2

- Kiểu Datetime trong Pandas
- pd.to_datetime()
- — chuyển string thành datetime
- Đặt cột thời gian làm index cho time-series
- ⚠️ Sai kiểu datetime → mọi phân tích sau đều sai
- Doanh số, log server, giá cổ phiếu — đều là time-series
- datetime.py
- import pandas as  pd df = pd.read_csv("don_hang.csv") # Kiểm tra kiểu ban đầu df.dtypes   # ngay_dat: object (string) # Chuyển sang datetime df["ngay_dat"] = pd.to_datetime(df["ngay_dat"]) # Đặt làm index df = df.set_index("ngay_dat").sort_index() # Lọc theo khoảng thời gian q1 = df["2024-01":"2024-03"]

### Slide 3

- .dt Accessor — Trích Thành Phần Thời Gian
- .dt
- = accessor cho datetime column
- Trích:
- .year
- ,
- .month
- ,
- .day
- ,
- .dayofweek
- Tạo
- feature thời gian
- cho model ML
- weekday() = 0 (Thứ 2) đến 6 (Chủ nhật)
- dt_accessor.py
- # Trích thành phần df["nam"]     = df["ngay"].dt.year df["thang"]   = df["ngay"].dt.month df["ngay_so"] = df["ngay"].dt.day df["thu"]     = df["ngay"].dt.dayofweek df["quy"]     = df["ngay"].dt.quarter # Cuối tuần hay không? df["cuoi_tuan"] = df["ngay"].dt.dayofweek >= 5 # Giờ cao điểm? df["gio"] = df["ngay"].dt.hour df["cao_diem"] = df["gio"].between(11, 14)

### Slide 4

- Resample — Đổi Tần Suất
- Gom dữ liệu theo chu kỳ mới:
- "D"
- ngày ·
- "W"
- tuần ·
- "M"
- tháng ·
- "Q"
- quý
- Dữ liệu giờ → dữ liệu ngày/tháng — đổi tần suất dễ dàng
- Cực tiện cho phân tích xu hướng theo thời gian
- resample.py
- # Tổng doanh thu theo tháng df_monthly = df["doanh_thu"].resample("M").sum() # Trung bình theo tuần df_weekly = df["doanh_thu"].resample("W").mean() # Nhiều cột cùng lúc df.resample("M").agg ({
- "doanh_thu": "sum" ,
- "so_don": "count" }) # Quý — rất hay dùng báo cáo df_q = df["doanh_thu"].resample("Q").sum()

### Slide 5

- Rolling Window — Trung Bình Trượt
- Tính giá trị trên
- cửa sổ trượt
- .rolling(n)
- — cửa sổ n kỳ
- Làm mượt nhiễu — thấy xu hướng rõ hơn
- Phổ biến trong tài chính: MA7, MA20, MA200
- 💡
- n đầu tiên = NaN (chưa đủ dữ liệu để tính)
- rolling.py
- # Trung bình trượt 7 ngày df["ma7"] = df["doanh_thu"].rolling(7).mean() # MA 30 ngày df["ma30"] = df["doanh_thu"].rolling(30).mean() # Rolling sum và std df["sum7d"] = df["doanh_thu"].rolling(7).sum() df["std7d"] = df["doanh_thu"].rolling(7).std() # Vẽ so sánh ax.plot(df["doanh_thu"], alpha=0.4, label="Ngày") ax.plot(df["ma7"], label="MA7")

### Slide 6

- LECTURE 16 — TÓM TẮT
- Ngày Tháng & Time-series
- pd.to_datetime() — chuyển string thành datetime
- .dt accessor — trích year · month · dayofweek
- resample("M") — đổi tần suất dữ liệu
- rolling(7).mean() — trung bình trượt, làm mượt nhiễu
- →
- Bài tiếp: Regex cho dữ liệu văn bản

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_