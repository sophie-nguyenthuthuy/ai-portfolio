# Section 2 · Lecture 14 — Seaborn — Phân Phối, Tương Quan & Pairplot

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 14
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Seaborn — Phân Phối, Tương Quan & Pairplot
- histplot / boxplot
- heatmap
- pairplot
- EDA nhanh

### Slide 2

- Vì Sao Dùng Seaborn?
- MATPLOTLIB
- Nhiều code để làm đẹp
- Không tích hợp sẵn với DataFrame
- Cần tuỳ biến thủ công nhiều
- plt.figure(figsize=(8,6)) plt.hist(df["tuoi"], bins=20) plt.title("Phân phối tuổi") plt.xlabel("Tuổi") plt.show()
- SEABORN
- Đẹp mặc định
- — ít code hơn
- Tích hợp sẵn với
- Pandas DataFrame
- Nhiều chart thống kê sẵn có
- import seaborn as  sns sns.histplot(data=df ,
- x="tuoi" ,
- kde=True)

### Slide 3

- Biểu Đồ Phân Phối
- histplot
- — histogram + KDE
- kdeplot
- — đường mật độ xác suất
- boxplot
- — phát hiện
- outlier nhanh
- violinplot
- — boxplot + KDE kết hợp
- Boxplot là chart đầu tiên nên vẽ khi khám phá data
- distribution.py
- import seaborn as sns # Histogram + đường KDE sns.histplot(data=df, x="thu_nhap", kde=True) # Boxplot theo nhóm sns.boxplot(data=df, x="vung", y="chi_tieu") # Violin plot sns.violinplot(data=df, x="phan_khuc" ,
- y="thu_nhap") # Đặt theme đẹp sns.set_theme(style="darkgrid")

### Slide 4

- Heatmap Tương Quan
- Ma trận tương quan
- — Pearson correlation
- Giá trị từ -1 đến +1
- Tìm nhanh feature
- liên quan tới target
- Tìm multicollinearity trước khi đưa vào model
- 💡
- |r| > 0.7 = tương quan cao · |r| < 0.3 = tương quan yếu
- heatmap.py
- # Tính ma trận tương quan corr = df.corr(numeric_only=True) # Vẽ heatmap sns.heatmap (
- corr ,
- annot=True,       # hiện số     fmt=".2f",         # 2 chữ số thập phân     cmap="coolwarm",  # màu sắc     vmin=-1, vmax=1 ) plt.title("Correlation Matrix") plt.show()

### Slide 5

- Pairplot — Khám Phá Toàn Bộ Dataset
- Vẽ
- mọi cặp biến
- cùng một lúc
- Đường chéo = phân phối từng biến
- Màu phân biệt nhóm (hue)
- 1 lệnh → thấy toàn bộ bức tranh dữ liệu
- 🎯
- Dùng cuối bước EDA để có cái nhìn tổng quan trước khi build model
- pairplot.py
- # Pairplot cơ bản sns.pairplot(df) # Pairplot với màu theo nhóm sns.pairplot (
- df[["tuoi","thu_nhap","chi_tieu","phan_khuc" ]],
- hue="phan_khuc" ,
- diag_kind="kde" ) # Chỉ chọn 1 vài cột cols = ["gia", "so_luong", "doanh_thu"] sns.pairplot(df[cols], corner=True) plt.show()

### Slide 6

- LECTURE 14 — TÓM TẮT
- Seaborn
- Đẹp mặc định · ít code · tích hợp DataFrame
- histplot · boxplot · violinplot — phân phối
- heatmap(df.corr()) — tương quan feature
- pairplot — khám phá toàn bộ dataset 1 lệnh
- →
- Bài tiếp: Plotly — biểu đồ tương tác

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_