# Section 5 · Lecture 11 — Naive Bayes

_Phần của: **Section 5: Machine Learning Fundamentals**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- LECTURE 11 · ~7 PHÚT
- 11
- Naive Bayes
- khi nào dùng được, khi nào không

### Slide 2

- L11 · DỰA TRÊN ĐỊNH LÝ BAYES
- Tính xác suất mỗi lớp rồi chọn lớp cao nhất
- P(lớp | dữ liệu) ∝ P(dữ liệu | lớp) · P(lớp)
- Nối lại định lý Bayes đã học ở Section 4
- Với mỗi lớp, tính xác suất dữ liệu thuộc lớp đó
- Chọn lớp có xác suất hậu nghiệm lớn nhất
- Đơn giản, nhanh, mạnh bất ngờ cho văn bản
- Nhắc lại kiến thức xác suất nền tảng

### Slide 3

- L11 · GIẢ ĐỊNH "NGÂY THƠ"
- Giả định mọi feature độc lập nhau
- Coi như các feature không ảnh hưởng lẫn nhau
- "Naive" (ngây thơ) chính là ở giả định này
- Thường sai trong thực tế — nhưng vẫn hiệu quả
- Đặc biệt tốt với dữ liệu văn bản nhiều chiều
- NGHỊCH LÝ THÚ VỊ
- Giả định sai mà kết quả vẫn tốt — vì ta chỉ cần xếp hạng lớp đúng, không cần xác suất chính xác.

### Slide 4

- L11 · ỨNG DỤNG
- Lọc spam & phân loại văn bản
- spam_filter.py
- from sklearn.naive_bayes import  MultinomialNB
- model =
- MultinomialNB ()
- model.
- fit (X_train_tfidf, y_train)
- model.
- predict(new_emails)   # spam / ham
- Nhanh, tốn ít dữ liệu để huấn luyện
- Baseline tốt cho bài toán NLP
- Kinh điển: lọc spam email
- Vẫn được dùng làm điểm khởi đầu

### Slide 5

- L11 · TÓM TẮT
- Naive Bayes
- 01
- Định lý Bayes
- Tính xác suất hậu nghiệm mỗi lớp
- 02
- Giả định độc lập
- "Naive" — thường sai nhưng hiệu quả
- 03
- Văn bản & spam
- Baseline nhanh cho NLP
- BÀI TIẾP
- K-Means — hết phần có nhãn, sang phân cụm
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_