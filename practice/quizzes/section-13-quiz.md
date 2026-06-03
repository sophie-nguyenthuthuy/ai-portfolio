# Quiz — Section 13: AGENTIC AI

_10 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Điểm khác biệt cốt lõi giữa chatbot và agent là gì?
- A. Agent chạy nhanh hơn
- B. ✅ Agent tự lập kế hoạch, dùng tool và lặp (think-act-observe), không chỉ hỏi-đáp 1 lượt
- C. Chatbot mạnh hơn
- D. Không khác nhau
*Giải thích: agent = LLM + tool + vòng lặp + memory.*

**Câu 2.** Pattern ReAct kết hợp những gì?
- A. Retrieval & Augmentation
- B. ✅ Reasoning & Acting (suy nghĩ + hành động xen kẽ)
- C. Read & Action
- D. Regression & Activation
*Giải thích: suy nghĩ → dùng tool → quan sát → lặp.*

**Câu 3.** LangGraph giải quyết hạn chế nào của chain tuyến tính?
- A. Quá nhanh
- B. ✅ Cho phép rẽ nhánh, lặp, điều kiện (mô hình đồ thị trạng thái)
- C. Không cần LLM
- D. Giảm chi phí token
*Giải thích: agent cần luồng phức tạp hơn chain thẳng.*

**Câu 4.** MCP (Model Context Protocol) giải quyết vấn đề gì?
- A. Tăng tốc LLM
- B. ✅ Chuẩn hoá cách agent kết nối tool/dữ liệu (như "USB cho agent")
- C. Nén model
- D. Đánh giá agent
*Giải thích: viết tool 1 lần, dùng cho nhiều agent.*

**Câu 5.** Long-term memory của agent thường được lưu bằng gì?
- A. Biến toàn cục
- B. ✅ Vector database (truy xuất khi cần — như RAG)
- C. File CSV
- D. RAM
*Giải thích: memory dài hạn = retrieval từ vector DB.*

**Câu 6.** Một failure mode phổ biến của agent là gì?
- A. Chạy quá chính xác
- B. ✅ Vòng lặp vô hạn / dùng sai tool / context overflow
- C. Quá nhanh
- D. Không có lỗi
*Giải thích: phải có guardrail giới hạn số bước.*

**Câu 7.** Multi-agent system có lợi thế gì?
- A. Luôn rẻ hơn
- B. ✅ Chia việc lớn cho nhiều agent chuyên môn, phối hợp giải bài toán phức tạp
- C. Không cần LLM
- D. Không cần tool
*Giải thích: giống một team người — mỗi agent một vai trò.*

**Câu 8.** Công cụ nào dùng để observability (quan sát) agent?
- A. NumPy
- B. ✅ LangSmith / LangFuse / Arize Phoenix
- C. Matplotlib
- D. Docker
*Giải thích: trace từng bước agent để debug.*

**Câu 9.** Khi thiết kế tool cho agent, yếu tố nào quan trọng nhất?
- A. Tool phải phức tạp
- B. ✅ Mô tả tool rõ ràng (tên, mô tả, tham số) để agent gọi đúng
- C. Tool phải viết bằng C++
- D. Tool không cần xử lý lỗi
*Giải thích: mô tả tốt = agent dùng đúng tool.*

**Câu 10.** Sự khác biệt giữa MS Copilot Studio và Claude Agent SDK?
- A. Không khác nhau
- B. ✅ Copilot Studio thiên low-code (business user); Claude Agent SDK thiên code-first (dev linh hoạt)
- C. Cả hai chỉ low-code
- D. Cả hai chỉ code-first
*Giải thích: chọn theo team & độ phức tạp.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-13-agentic-ai/README.md)_
