# Quiz — Section 12: RAG & VECTOR DATABASE

_10 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** RAG là viết tắt của gì?
- A. Random Access Generation
- B. ✅ Retrieval-Augmented Generation
- C. Rapid AI Gateway
- D. Recursive Agent Graph
*Giải thích: tìm tài liệu rồi đưa vào prompt để sinh câu trả lời.*

**Câu 2.** RAG giúp giải quyết hạn chế nào của LLM?
- A. Tốc độ chậm
- B. ✅ Không biết dữ liệu nội bộ, kiến thức cũ, hay hallucinate
- C. Không sinh được code
- D. Không dùng GPU
*Giải thích: RAG bơm ngữ cảnh tươi & nội bộ vào LLM.*

**Câu 3.** Trong RAG, embedding dùng để làm gì?
- A. Train model
- B. ✅ Biến văn bản thành vector để tìm theo độ tương đồng
- C. Nén model
- D. Vẽ biểu đồ
*Giải thích: embedding là trái tim của retrieval.*

**Câu 4.** Vì sao chunking quan trọng trong RAG?
- A. Để train nhanh hơn
- B. ✅ Chunk là đơn vị tìm kiếm; chunk sai làm retrieve sai → RAG hỏng
- C. Để giảm chi phí GPU
- D. Không quan trọng
*Giải thích: bước bị xem nhẹ nhưng quyết định chất lượng.*

**Câu 5.** Chunk overlap (chồng lấn) có tác dụng gì?
- A. Tốn bộ nhớ vô ích
- B. ✅ Giữ ngữ cảnh, tránh cắt đứt ý giữa chừng
- C. Tăng tốc tìm kiếm
- D. Giảm số chunk
*Giải thích: overlap giúp không mất ngữ cảnh ở ranh giới chunk.*

**Câu 6.** Reranker trong RAG làm gì?
- A. Tạo embedding
- B. ✅ Xếp lại các kết quả retrieve để chọn chunk liên quan nhất
- C. Sinh câu trả lời
- D. Lưu vector
*Giải thích: rerank cải thiện đáng kể chất lượng cuối.*

**Câu 7.** Vì sao chỉ dùng vector search đôi khi chưa đủ?
- A. Vector search quá nhanh
- B. ✅ Có thể miss từ khoá chính xác (mã, tên riêng) → cần hybrid với BM25
- C. Vector không lưu được
- D. Không hỗ trợ tiếng Việt
*Giải thích: vector giỏi nghĩa, kém khớp chính xác → hybrid.*

**Câu 8.** Với production 100M vector, lựa chọn nào hợp lý hơn?
- A. Tính tay bằng for loop
- B. ✅ Vector DB chuyên dụng (Qdrant/Pinecone/Milvus) với ANN
- C. Lưu trong file CSV
- D. Dùng Excel
*Giải thích: cần ANN + khả năng mở rộng cho quy mô lớn.*

**Câu 9.** RAGAS đo các chỉ số nào?
- A. Accuracy, F1
- B. ✅ Faithfulness, answer relevance, context precision
- C. BLEU, ROUGE
- D. Latency, throughput
*Giải thích: faithfulness chống hallucination trong RAG.*

**Câu 10.** Trích dẫn nguồn (citation) trong RAG production có lợi ích gì?
- A. Làm câu trả lời dài hơn
- B. ✅ Tăng niềm tin và giúp chống/kiểm chứng hallucination
- C. Tăng tốc retrieve
- D. Giảm chi phí token
*Giải thích: người dùng tin hơn khi thấy nguồn.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-12-rag/README.md)_
