# Section 2 · Lecture 15 — Plotly — Biểu Đồ Tương Tác & Dashboard

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 15
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Plotly — Biểu Đồ Tương Tác & Dashboard
- Plotly Express
- hover · zoom · filter
- Streamlit / Dash

### Slide 2

- Vì Sao Cần Biểu Đồ Tương Tác?
- STATIC CHART (MATPLOTLIB/SEABORN)
- Ảnh tĩnh — không tương tác
- Không zoom/filter được
- Không thấy giá trị khi hover
- Tốt cho: báo cáo PDF, publication
- INTERACTIVE CHART (PLOTLY)
- Hover để xem giá trị chính xác
- Zoom/pan/filter trực tiếp
- Bật/tắt series bằng click
- Tốt cho: trình bày stakeholder, dashboard
- 💼
- Sếp và stakeholder thích biểu đồ tương tác hơn ảnh tĩnh — trông chuyên nghiệp hơn

### Slide 3

- Plotly Express — API Ngắn Gọn
- Plotly Express = API cấp cao của Plotly
- 1 dòng code = 1 biểu đồ đẹp, tương tác
- Tương tự Seaborn nhưng interactive
- Dùng
- px
- cho 90% nhu cầu hàng ngày
- plotly_express.py
- import plotly.express as px # Line chart tương tác fig = px.line(df, x="thang", y="doanh_thu" ,
- color="vung", title="Doanh Thu") fig.show() # Scatter với bubble fig = px.scatter(df, x="thu_nhap" ,
- y="chi_tieu", size="so_don" ,
- color="phan_khuc", hover_name="ten") # Bar fig = px.bar(df, x="vung", y="doanh_thu")

### Slide 4

- Các Biểu Đồ Phổ Biến
- Thống kê
- px.bar
- px.line
- px.scatter
- px.histogram
- px.box
- Dùng hàng ngày trong EDA
- Địa lý
- px.choropleth
- px.scatter_map
- px.density_map
- Bản đồ dữ liệu — Plotly rất mạnh
- Nâng cao
- px.treemap
- px.sunburst
- px.funnel
- px.scatter_3d
- Trình bày ấn tượng cho stakeholder
- 💡
- Plotly mạnh nhất ở bản đồ và 3D — không thư viện nào sánh kịp

### Slide 5

- Hướng Tới Dashboard
- Plotly +
- Streamlit
- = web app data nhanh nhất
- Plotly +
- Dash
- = dashboard enterprise
- Deploy lên Streamlit Cloud — miễn phí, dễ chia sẻ
- Gặp lại khi deploy POC ở phần
- MLOps
- 🚀
- Streamlit: từ notebook → web app trong 10 phút
- streamlit_app.py
- import streamlit as st import plotly.express as px import pandas as  pd st.title("📊 Dashboard TMĐT") df = pd.read_csv("don_hang.csv") vung = st.selectbox("Chọn vùng", df["vung"].unique()) df_f = df[df["vung"]==vung] fig = px.line(df_f, x="thang", y="doanh_thu") st.plotly_chart(fig)

### Slide 6

- LECTURE 15 — TÓM TẮT
- Plotly
- Interactive: hover · zoom · filter · toggle
- Plotly Express — 1 dòng = biểu đồ tương tác
- Mạnh nhất: bản đồ, 3D, animation
- Plotly + Streamlit = web app data trong 10 phút
- →
- Bài tiếp: Ngày Tháng & Time-series

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_