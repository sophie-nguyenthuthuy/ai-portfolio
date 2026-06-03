# Quiz — Section 8: COMPUTER VISION

_12 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Với ảnh input 224×224, conv kernel 3×3, stride 1, padding 1 → kích thước output là?
- A. 222×222
- B. ✅ 224×224
- C. 226×226
- D. 112×112
*Giải thích: padding 1 với kernel 3×3 stride 1 giữ nguyên kích thước.*

**Câu 2.** Ảnh màu RGB được biểu diễn bằng tensor mấy chiều?
- A. 1 chiều
- B. 2 chiều
- C. ✅ 3 chiều (Height × Width × Channel)
- D. 4 chiều
*Giải thích: H×W×C với C=3 cho RGB.*

**Câu 3.** Skip connection trong ResNet giải quyết vấn đề gì?
- A. Overfitting
- B. ✅ Vanishing gradient, giúp train được mạng rất sâu
- C. Thiếu dữ liệu
- D. Tốc độ chậm
*Giải thích: đường tắt cho gradient chảy thẳng qua các lớp.*

**Câu 4.** Vision Transformer (ViT) xử lý ảnh bằng cách nào?
- A. Như RNN
- B. ✅ Chia ảnh thành các patch và áp dụng attention
- C. Chỉ dùng pooling
- D. Không dùng học sâu
*Giải thích: ViT coi ảnh như chuỗi patch, dùng self-attention.*

**Câu 5.** Transfer learning có lợi ích chính gì?
- A. Cần nhiều dữ liệu hơn
- B. ✅ Tận dụng model pretrained, tiết kiệm dữ liệu/thời gian/GPU
- C. Chỉ dùng cho NLP
- D. Luôn cho kết quả 100%
*Giải thích: dùng đặc trưng đã học, không train từ đầu.*

**Câu 6.** Data augmentation nên áp dụng ở đâu?
- A. Cả train và test
- B. ✅ Chỉ trên tập train
- C. Chỉ trên test
- D. Không bao giờ
*Giải thích: augment test sẽ làm đánh giá sai.*

**Câu 7.** IoU (Intersection over Union) dùng trong bài toán nào?
- A. Phân loại ảnh
- B. ✅ Object detection (đo độ khớp bounding box)
- C. Tạo ảnh
- D. OCR
*Giải thích: IoU = diện tích giao / hợp của 2 box.*

**Câu 8.** Khi nào nên chọn YOLO thay vì Faster R-CNN?
- A. Khi cần độ chính xác tối đa, không quan tâm tốc độ
- B. ✅ Khi cần tốc độ real-time (one-stage detector)
- C. Khi chỉ phân loại
- D. Khi dữ liệu rất ít
*Giải thích: YOLO one-stage nhanh; Faster R-CNN two-stage chính xác hơn.*

**Câu 9.** U-Net mạnh nhất ở bài toán nào?
- A. Object detection
- B. ✅ Image segmentation (đặc biệt ảnh y tế)
- C. Phân loại
- D. OCR
*Giải thích: kiến trúc encoder-decoder chữ U cho segmentation.*

**Câu 10.** Quantization (vd float32 → int8) mang lại lợi ích gì?
- A. Tăng độ chính xác
- B. ✅ Model nhỏ & nhanh hơn, ít tốn điện (mất ít accuracy)
- C. Tăng kích thước model
- D. Cần nhiều GPU hơn
*Giải thích: giảm độ chính xác số để nén model cho edge.*

**Câu 11.** ONNX dùng để làm gì?
- A. Train model
- B. ✅ Định dạng model chung để chạy trên nhiều nền tảng
- C. Làm sạch ảnh
- D. Vẽ biểu đồ
*Giải thích: "train một nơi, chạy mọi nơi".*

**Câu 12.** PaddleOCR được khuyên dùng cho lý do gì trong khoá này?
- A. Chỉ chạy trên GPU
- B. ✅ Hỗ trợ tiếng Việt tốt
- C. Miễn phí duy nhất
- D. Nhanh nhất tuyệt đối
*Giải thích: lưu ý hỗ trợ dấu tiếng Việt khi chọn OCR.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-08-computer-vision/README.md)_
