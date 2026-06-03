# Quiz — Section 9: NLP

_12 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Trong tiếng Việt, vì sao khoảng trắng KHÔNG phải ranh giới từ?
- A. Vì tiếng Việt không có dấu cách
- B. ✅ Vì nhiều từ ghép như "học sinh" gồm 2 tiếng nhưng là 1 từ
- C. Vì tiếng Việt viết liền
- D. Không đúng, khoảng trắng luôn là ranh giới
*Giải thích: cần word segmentation (underthesea) cho tiếng Việt.*

**Câu 2.** TF-IDF cải thiện Bag-of-Words ở điểm nào?
- A. Giữ thứ tự từ
- B. ✅ Đề cao từ đặc trưng, giảm trọng số từ phổ biến
- C. Hiểu ngữ cảnh
- D. Tạo embedding dày
*Giải thích: IDF giảm điểm cho từ xuất hiện ở mọi tài liệu.*

**Câu 3.** Phép toán "king − man + woman ≈ queen" minh hoạ điều gì?
- A. BoW hoạt động tốt
- B. ✅ Word embedding nắm bắt quan hệ ngữ nghĩa
- C. TF-IDF chính xác
- D. Tokenization
*Giải thích: embedding mang ý nghĩa, không chỉ đếm từ.*

**Câu 4.** Cơ chế attention giải quyết hạn chế gì của RNN?
- A. Quá nhanh
- B. ✅ Xử lý tuần tự chậm và quên ngữ cảnh xa
- C. Thiếu dữ liệu
- D. Không có nhãn
*Giải thích: attention "nhìn" mọi từ cùng lúc, song song hoá được.*

**Câu 5.** BERT dùng phần nào của Transformer?
- A. Decoder
- B. ✅ Encoder
- C. Cả hai
- D. Không dùng Transformer
*Giải thích: BERT là encoder (hiểu), GPT là decoder (sinh).*

**Câu 6.** GPT sinh văn bản theo cách nào?
- A. Sinh cả câu cùng lúc
- B. ✅ Tự hồi quy — dự đoán token tiếp theo từng bước
- C. Dùng masked LM
- D. Phân loại
*Giải thích: autoregressive, decoder-only.*

**Câu 7.** Positional encoding trong Transformer dùng để làm gì?
- A. Tăng tốc độ
- B. ✅ Cung cấp thông tin thứ tự từ (vì attention xử lý song song)
- C. Giảm overfitting
- D. Mã hoá ý nghĩa
*Giải thích: Transformer không có thứ tự sẵn nên cần báo vị trí.*

**Câu 8.** PhoBERT là gì?
- A. OCR tiếng Việt
- B. ✅ Mô hình BERT cho tiếng Việt
- C. Công cụ tách từ
- D. Vector database
*Giải thích: PhoBERT pretrained cho tiếng Việt.*

**Câu 9.** Temperature cao khi sinh văn bản dẫn tới?
- A. Văn bản an toàn, lặp lại
- B. ✅ Văn bản đa dạng, sáng tạo, ngẫu nhiên hơn
- C. Không ảnh hưởng
- D. Lỗi model
*Giải thích: temperature thấp = xác định; cao = sáng tạo.*

**Câu 10.** BLEU thường dùng để đánh giá tác vụ nào?
- A. Phân loại
- B. ✅ Dịch máy
- C. Phân cụm
- D. Object detection
*Giải thích: BLEU so n-gram với bản tham chiếu, dùng cho dịch.*

**Câu 11.** Semantic search khác keyword search ở điểm nào?
- A. Chậm hơn
- B. ✅ Tìm theo NGHĨA chứ không chỉ khớp chữ chính xác
- C. Chỉ dùng tiếng Anh
- D. Không cần embedding
*Giải thích: "ô tô" tìm được cả "xe hơi" nhờ embedding.*

**Câu 12.** Hybrid search kết hợp những gì?
- A. 2 model phân loại
- B. ✅ Keyword (BM25) + tìm kiếm ngữ nghĩa (vector)
- C. CNN + RNN
- D. Train + test
*Giải thích: hybrid cho kết quả tốt nhất, dùng nhiều trong RAG.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-09-nlp/README.md)_
