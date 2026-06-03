# Section 6 · Lecture 7 — Tiếp cận ML — sliding window + XGBoost

_Phần của: **Section 6: Time Series — Dự báo chuỗi thời gian**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 07
- SECTION 6 · LECTURE 7
- Tiếp cận ML — sliding window + XGBoost
- ~8 phút · 6 slides

### Slide 2

- SLIDING WINDOW
- Biến time-series thành bài toán ML
- Dùng quá khứ làm feature dự đoán tương lai
- Bước chuẩn bị quan trọng — cả cho LSTM sau này
- y₍ₜ₋₃₎
- →
- y₍ₜ₋₂₎
- →
- y₍ₜ₋₁₎
- →
- ŷ₍ₜ₎

### Slide 3

- FEATURES
- Feature từ thời gian
- features.py
- for lag in [1, 7, 14 ]:
- df[f
- "lag_{lag}"] = df["y" ].shift(lag)
- df[
- "roll7"] = df["y"].shift(1).rolling(7 ).mean()
- df[
- "dow" ]   = df.index.dayofweek
- df[
- "month"] = df.index.month
- lag & rolling mean
- ngày / tháng / thứ trong tuần
- Nối lại feature engineering Section 2

### Slide 4

- XGBOOST
- Huấn luyện XGBoost cho dự báo
- xgb.py
- from xgboost import  XGBRegressor
- model = XGBRegressor(n_estimators=
- 400, max_depth=4 )
- model.fit(X_train, y_train)
- pred = model.predict(X_test)
- Đưa lag features vào XGBoost
- Bắt quan hệ phi tuyến tốt hơn ARIMA

### Slide 5

- BACKTESTING
- Đánh giá đúng với TimeSeriesSplit
- fold 1
- fold 2
- fold 3
- fold 4
- fold 5
- train (quá khứ)
- test (tương lai)
- ⚠ Lỗi kinh điển: shuffle dữ liệu time-series. Tập test phải luôn nằm sau tập train.

### Slide 6

- SECTION 6 · LECTURE 7
- Tóm tắt & chuyển bài
- ĐÃ HỌC TRONG BÀI NÀY
- sliding window
- lag features
- TimeSeriesSplit
- BÀI TIẾP THEO
- →
- LSTM & GRU

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_