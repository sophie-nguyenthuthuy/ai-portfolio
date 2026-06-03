# Quiz — Section 5: MACHINE LEARNING FUNDAMENTALS

_12 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Model đạt 99% accuracy trên dữ liệu fraud (1% là fraud). Vì sao có thể tệ?
- A. Accuracy luôn tốt
- B. ✅ Vì đoán "không fraud" cho tất cả cũng được 99%, nhưng bỏ sót toàn bộ fraud
- C. Vì dữ liệu quá lớn
- D. Vì thiếu feature
*Giải thích: với dữ liệu mất cân bằng, accuracy đánh lừa — dùng Recall/F1.*

**Câu 2.** Overfitting là hiện tượng gì?
- A. Model học kém trên cả train và test
- B. ✅ Model học tốt trên train nhưng kém trên dữ liệu mới
- C. Model train quá nhanh
- D. Dữ liệu quá ít cột
*Giải thích: overfit = thuộc lòng train, không tổng quát được.*

**Câu 3.** Bias-variance tradeoff: model quá đơn giản thường gặp vấn đề gì?
- A. Variance cao
- B. ✅ Bias cao (underfitting)
- C. Overfitting
- D. Không vấn đề gì
*Giải thích: model đơn giản → bias cao; model phức tạp → variance cao.*

**Câu 4.** Vì sao Logistic Regression dùng log-loss thay vì MSE?
- A. MSE tính chậm hơn
- B. ✅ Log-loss phù hợp đầu ra xác suất và phạt nặng dự đoán sai tự tin
- C. MSE không tồn tại
- D. Log-loss đơn giản hơn
*Giải thích: log-loss (cross-entropy) phù hợp bài toán phân loại.*

**Câu 5.** Random Forest cải thiện Decision Tree chủ yếu bằng cách nào?
- A. Tăng độ sâu cây
- B. ✅ Kết hợp nhiều cây (bagging) để giảm phương sai
- C. Bỏ bớt feature
- D. Dùng ít dữ liệu hơn
*Giải thích: bagging nhiều cây giảm variance, ổn định hơn 1 cây.*

**Câu 6.** Gradient Boosting (XGBoost) khác Bagging ở điểm nào?
- A. Boosting train song song
- B. ✅ Boosting train tuần tự, mỗi cây sửa lỗi của cây trước
- C. Boosting không dùng cây
- D. Không khác nhau
*Giải thích: boosting học từ sai số (residual) của model trước.*

**Câu 7.** Trong K-Means, Elbow method dùng để làm gì?
- A. Tính khoảng cách
- B. ✅ Chọn số cụm K hợp lý
- C. Khởi tạo tâm cụm
- D. Đánh giá overfitting
*Giải thích: nhìn "khuỷu tay" trên đồ thị inertia để chọn K.*

**Câu 8.** SMOTE dùng để giải quyết vấn đề gì?
- A. Overfitting
- B. ✅ Dữ liệu mất cân bằng lớp (sinh thêm mẫu lớp thiểu số)
- C. Thiếu feature
- D. Dữ liệu quá lớn
*Giải thích: SMOTE oversample lớp hiếm bằng mẫu nhân tạo, chỉ trên train.*

**Câu 9.** Cosine similarity được dùng trong loại recommender nào?
- A. Chỉ collaborative
- B. ✅ Content-based (so độ giống đặc điểm sản phẩm)
- C. Không dùng trong recommender
- D. Chỉ cho ảnh
*Giải thích: content-based dùng similarity giữa đặc trưng sản phẩm.*

**Câu 10.** Data leakage là gì?
- A. Mất dữ liệu
- B. ✅ Thông tin từ test/tương lai rò rỉ vào quá trình train, làm đánh giá ảo
- C. Dữ liệu bị trùng
- D. Dữ liệu quá lớn
*Giải thích: vd fit scaler trên toàn bộ data trước khi split → leakage.*

**Câu 11.** PCA chủ yếu dùng để làm gì?
- A. Tăng số chiều
- B. ✅ Giảm chiều dữ liệu, giữ thông tin quan trọng nhất
- C. Phân loại
- D. Vẽ confusion matrix
*Giải thích: PCA nén dữ liệu, tăng tốc & trực quan hoá.*

**Câu 12.** Optuna dùng cho mục đích gì?
- A. Vẽ biểu đồ
- B. ✅ Tinh chỉnh hyperparameter (Bayesian optimization)
- C. Làm sạch dữ liệu
- D. Triển khai model
*Giải thích: Optuna tìm hyperparameter thông minh hơn Grid/Random.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-05-machine-learning-fundamentals/README.md)_
