# Quiz — Section 10: GENERATIVE AI

_8 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Mô hình generative khác discriminative ở điểm nào?
- A. Generative chỉ phân loại
- B. ✅ Generative học phân phối dữ liệu và TẠO mẫu mới; discriminative học ranh giới phân lớp
- C. Không khác nhau
- D. Discriminative tạo ảnh
*Giải thích: generative sinh nội dung mới, discriminative phân biệt.*

**Câu 2.** Trong GAN, Discriminator có vai trò gì?
- A. Tạo ảnh giả
- B. ✅ Phân biệt ảnh thật và ảnh giả
- C. Lưu dữ liệu
- D. Tăng tốc training
*Giải thích: Generator tạo, Discriminator phán thật/giả — đối kháng.*

**Câu 3.** Vì sao GAN nổi tiếng khó train?
- A. Cần ít dữ liệu
- B. ✅ Không ổn định, dễ mode collapse
- C. Chạy quá nhanh
- D. Không dùng GPU
*Giải thích: cân bằng G và D rất khó.*

**Câu 4.** Diffusion model sinh ảnh bằng cách nào?
- A. Phân loại pixel
- B. ✅ Học khử nhiễu từng bước, biến nhiễu thành ảnh
- C. Đối kháng 2 mạng
- D. Tìm kiếm ảnh có sẵn
*Giải thích: forward thêm nhiễu, reverse khử nhiễu.*

**Câu 5.** Diffusion model có ưu điểm gì so với GAN?
- A. Train nhanh hơn nhiều
- B. ✅ Ổn định hơn, chất lượng & đa dạng cao hơn
- C. Cần ít tính toán hơn
- D. Không cần dữ liệu
*Giải thích: diffusion đã vượt GAN về chất lượng ảnh.*

**Câu 6.** ControlNet dùng để làm gì?
- A. Tăng tốc diffusion
- B. ✅ Kiểm soát bố cục/tư thế/đường nét của ảnh sinh ra
- C. Nén model
- D. Đánh giá ảnh
*Giải thích: ControlNet cho kiểm soát chính xác thay vì hên xui.*

**Câu 7.** Mô hình nào làm cầu nối text–ảnh trong text-to-image?
- A. BERT
- B. ✅ CLIP
- C. YOLO
- D. ARIMA
*Giải thích: CLIP đưa ảnh & text vào cùng không gian embedding.*

**Câu 8.** Autoencoder gồm những thành phần nào?
- A. Generator & Discriminator
- B. ✅ Encoder (nén) và Decoder (tái tạo)
- C. Q, K, V
- D. Conv & Pool
*Giải thích: encoder→latent→decoder; nền của VAE.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-10-generative-ai/README.md)_
