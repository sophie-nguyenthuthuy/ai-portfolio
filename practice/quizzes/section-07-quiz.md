# Quiz — Section 7: DEEP LEARNING

_10 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Vì sao một perceptron đơn không học được bài toán XOR?
- A. Vì XOR quá phức tạp
- B. ✅ Vì XOR không tách được tuyến tính, cần mạng nhiều lớp + phi tuyến
- C. Vì thiếu dữ liệu
- D. Vì learning rate sai
*Giải thích: cần hidden layer + activation phi tuyến.*

**Câu 2.** Hàm kích hoạt nào là mặc định phổ biến cho lớp ẩn hiện nay?
- A. Sigmoid
- B. Tanh
- C. ✅ ReLU
- D. Softmax
*Giải thích: ReLU đơn giản, tránh vanishing gradient tốt hơn sigmoid/tanh.*

**Câu 3.** Vì sao cần hàm kích hoạt phi tuyến?
- A. Để tính nhanh hơn
- B. ✅ Vì xếp chồng nhiều lớp tuyến tính vẫn chỉ là 1 phép tuyến tính
- C. Để giảm overfitting
- D. Để tiết kiệm bộ nhớ
*Giải thích: phi tuyến cho phép mạng học mẫu phức tạp.*

**Câu 4.** Backpropagation dựa trên quy tắc toán học nào?
- A. Phép cộng ma trận
- B. ✅ Quy tắc chuỗi (chain rule) của đạo hàm
- C. Định lý Bayes
- D. Phép nhân vô hướng
*Giải thích: chain rule truyền gradient ngược qua các lớp.*

**Câu 5.** Optimizer nào là lựa chọn an toàn, phổ biến cho hầu hết bài toán?
- A. SGD thuần
- B. ✅ Adam
- C. Không cần optimizer
- D. Grid Search
*Giải thích: Adam tự điều chỉnh learning rate, hội tụ tốt.*

**Câu 6.** Dropout giúp ích gì?
- A. Tăng tốc training
- B. ✅ Chống overfitting bằng cách tắt ngẫu nhiên nơ-ron khi train
- C. Tăng độ chính xác train
- D. Giảm số lớp
*Giải thích: dropout buộc mạng không phụ thuộc 1 đường duy nhất.*

**Câu 7.** Khi loss = NaN trong lúc train, nguyên nhân thường gặp nhất là gì?
- A. Dữ liệu quá ít
- B. ✅ Learning rate quá lớn / exploding gradient
- C. Quá nhiều epoch
- D. Dùng GPU
*Giải thích: giảm lr hoặc gradient clipping thường khắc phục.*

**Câu 8.** Trong PyTorch, `nn.Module` dùng để làm gì?
- A. Vẽ biểu đồ
- B. ✅ Định nghĩa kiến trúc model bằng class
- C. Đọc dữ liệu
- D. Tính loss
*Giải thích: kế thừa nn.Module để xây model — đây là lý do học OOP.*

**Câu 9.** Epoch là gì?
- A. Một batch dữ liệu
- B. ✅ Một lượt train qua toàn bộ tập dữ liệu
- C. Một lớp neural network
- D. Một optimizer
*Giải thích: 1 epoch = mạng thấy toàn bộ data 1 lần (gồm nhiều batch).*

**Câu 10.** Mẹo debug: nếu mạng không thể overfit dù chỉ 1 batch nhỏ, điều đó gợi ý gì?
- A. Cần thêm dữ liệu
- B. ✅ Có khả năng code/pipeline đang có bug
- C. Cần GPU mạnh hơn
- D. Mạng quá tốt
*Giải thích: mạng đúng phải overfit nổi 1 batch nhỏ — nếu không là có lỗi.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-07-deep-learning/README.md)_
