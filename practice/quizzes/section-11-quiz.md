# Quiz — Section 11: LLMs

_12 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Năng lực "emergent" của LLM nghĩa là gì?
- A. Lỗi của model
- B. ✅ Khả năng xuất hiện khi model đủ lớn mà không được dạy trực tiếp
- C. Tốc độ sinh nhanh
- D. Khả năng vẽ
*Giải thích: reasoning, in-context learning nổi lên theo quy mô.*

**Câu 2.** Ba giai đoạn tạo nên một LLM trợ lý là gì?
- A. Train, test, deploy
- B. ✅ Pretraining → Supervised Fine-tuning → RLHF
- C. Encode, decode, output
- D. Clean, train, monitor
*Giải thích: RLHF làm model hữu ích & an toàn theo ý người.*

**Câu 3.** RLHF là viết tắt của gì?
- A. Random Learning от Human Feedback
- B. ✅ Reinforcement Learning from Human Feedback
- C. Recursive Layer Hidden Function
- D. Rapid LLM Hosting Framework
*Giải thích: học tăng cường từ phản hồi con người.*

**Câu 4.** So với fine-tuning, RAG phù hợp hơn khi nào?
- A. Khi cần đổi phong cách model
- B. ✅ Khi cần kiến thức cập nhật/nội bộ mà không train lại
- C. Khi không có dữ liệu
- D. Khi cần model nhỏ hơn
*Giải thích: RAG bơm ngữ cảnh; fine-tune dạy kỹ năng/phong cách.*

**Câu 5.** LoRA giúp fine-tune tiết kiệm bằng cách nào?
- A. Train lại toàn bộ tham số
- B. ✅ Chỉ train các ma trận nhỏ thêm vào, giữ nguyên model gốc
- C. Xoá bớt lớp
- D. Dùng ít dữ liệu hơn
*Giải thích: LoRA giảm mạnh tham số cần train.*

**Câu 6.** QLoRA khác LoRA ở điểm nào?
- A. Không dùng được trên GPU
- B. ✅ Kết hợp LoRA với quantization để fine-tune model lớn trên ít bộ nhớ
- C. Chậm hơn
- D. Chỉ cho ảnh
*Giải thích: QLoRA cho fine-tune ngay trên Colab.*

**Câu 7.** "Hallucination" của LLM là gì?
- A. Model chạy chậm
- B. ✅ Tạo thông tin sai một cách tự tin
- C. Lỗi cú pháp
- D. Hết token
*Giải thích: nguy hiểm vì nghe rất thuyết phục.*

**Câu 8.** Biện pháp nào KHÔNG giúp giảm hallucination?
- A. Grounding bằng RAG
- B. Yêu cầu trích dẫn nguồn
- C. Hạ temperature
- D. ✅ Tăng temperature lên cao
*Giải thích: temperature cao làm model "liều" hơn, dễ bịa hơn.*

**Câu 9.** Chain-of-Thought prompting là gì?
- A. Nối nhiều model
- B. ✅ Yêu cầu model suy nghĩ từng bước trước khi trả lời
- C. Một loại fine-tuning
- D. Một vector database
*Giải thích: tăng độ chính xác cho bài toán reasoning.*

**Câu 10.** Function calling cho phép LLM làm gì?
- A. Train nhanh hơn
- B. ✅ Gọi tool/API bên ngoài để làm việc thật
- C. Giảm hallucination hoàn toàn
- D. Sinh ảnh
*Giải thích: cho LLM "tay chân", nền của agent.*

**Câu 11.** Tiếng Việt thường có đặc điểm gì về token so với tiếng Anh?
- A. Ít token hơn
- B. ✅ Tốn nhiều token hơn (ảnh hưởng chi phí API)
- C. Bằng nhau
- D. Không tính được
*Giải thích: lưu ý chi phí khi xử lý tiếng Việt qua API.*

**Câu 12.** Công cụ nào dễ nhất để chạy LLM local cho người mới?
- A. vLLM
- B. ✅ Ollama
- C. Kubernetes
- D. MLflow
*Giải thích: Ollama tải & chạy bằng 1 lệnh.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-11-large-language-models/README.md)_
