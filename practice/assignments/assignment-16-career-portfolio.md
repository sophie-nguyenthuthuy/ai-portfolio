# 🎯 ASSIGNMENT 16 — Sự nghiệp, Portfolio & Phỏng vấn (Capstone)
## Biến kỹ năng thành cơ hội nghề nghiệp

> **3 nguyên tắc xuyên suốt:** Chất hơn lượng · Demo chạy được · Luôn có con số.

> 📌 **Cách dùng tài liệu này:** Đây là **template + ví dụ mẫu** dựa trên các dự án trong khoá.
> Learner thay thông tin cá nhân (tên, link, số liệu thật của mình) vào các chỗ [trong ngoặc].
> Ví dụ dùng 3 dự án từ bootcamp để minh hoạ — bạn chọn 3 dự án MẠNH NHẤT của riêng mình.

---

## Câu 1 — Chọn 3 dự án mạnh nhất (đa dạng kỹ năng)

**Tiêu chí chọn:** không chọn 3 dự án giống nhau — chọn để phủ **đa dạng kỹ năng**, cho nhà tuyển dụng
thấy bề rộng. Gợi ý chọn từ khoá:

| # | Dự án | Kỹ năng thể hiện | Vì sao mạnh |
|---|-------|------------------|-------------|
| 1 | **Churn Prediction Pipeline** (A5) | ML cổ điển, xử lý mất cân bằng, chọn metric đúng | End-to-end, có business impact rõ |
| 2 | **RAG Chatbot tài liệu nội bộ** (A12) | LLM, vector DB, hybrid search, chống bịa | Hot nhất hiện nay, bài toán doanh nghiệp thật |
| 3 | **MLOps Pipeline** (A14) | Production: MLflow, Docker, drift monitoring | Phân biệt "biết train model" vs "ship được" |

**Vì sao 3 cái này:** phủ trọn vòng đời — (1) **ML nền tảng** + tư duy metric, (2) **GenAI/LLM** hiện đại,
(3) **MLOps production**. Bộ ba này kể câu chuyện: *"Tôi xây được model, hiểu LLM mới nhất, VÀ đưa được
lên production tự bảo trì"* — đúng thứ nhà tuyển dụng ML tìm. Tránh chọn 3 dự án classification giống nhau.

> 💡 Nếu nhắm vị trí cụ thể: nhắm **LLM Engineer** → đẩy RAG + Agent (A13) + fine-tune (A11); nhắm
> **MLOps/Platform** → đẩy A14 + A15 (responsible AI) + monitoring.

---

## Câu 2 — Làm đẹp 1 repo (README + demo + kết quả)

**Anatomy của README portfolio tốt** (cấu trúc chuẩn):

```markdown
# 🛒 Tên dự án — mô tả 1 dòng hấp dẫn

[![demo](badge)] [![python](badge)]   ← badges

## 🎯 Vấn đề
2-3 câu: giải quyết bài toán gì, vì sao quan trọng (có business context).

## 📊 Kết quả (đặt LÊN ĐẦU - quan trọng nhất!)
- Accuracy 91%, Recall churn 0.78 → giảm 30% khách rời bỏ (ước tính)
- Latency P95 < 200ms

## 🎬 Demo
![demo GIF](demo.gif)   ← GIF chạy thật là điểm cộng CỰC lớn
[Link demo trực tiếp](https://...)

## 🛠️ Công nghệ
Python · scikit-learn · FastAPI · Docker · MLflow

## 🚀 Chạy thử
\`\`\`bash
git clone ... && docker run ...
\`\`\`

## 📁 Cấu trúc / 🧠 Cách hoạt động / 📌 Hướng phát triển
```

**Checklist repo tốt:**
- [ ] README có **kết quả + số** ngay phần đầu (không bắt người đọc cuộn)
- [ ] **Demo GIF hoặc link live** — bấm thử được
- [ ] Hướng dẫn chạy rõ ràng (clone → run trong vài lệnh)
- [ ] Code sạch, có comment, .gitignore đúng
- [ ] KHÔNG commit data lớn / secret / .venv

> 🔗 **[Dán link repo đã làm đẹp của bạn vào đây]**

---

## Câu 3 — Profile README (trang GitHub cá nhân)

*Tạo repo trùng tên username → GitHub hiện README đó ở trang profile.*

```markdown
### Xin chào, mình là [Tên] 👋

🤖 **AI/ML Engineer** | Tập trung [LLM / MLOps / Data Engineering]

- 🔭 Đang xây: [dự án hiện tại]
- 🌱 Đang học: [công nghệ đang học]
- 💡 Quan tâm: RAG, LLM fine-tuning, production ML
- 📫 Liên hệ: [email] · [LinkedIn]

#### 🛠️ Tech Stack
`Python` `PyTorch` `scikit-learn` `FastAPI` `Docker` `MLflow` `LangGraph`

#### 🚀 Dự án nổi bật
| Dự án | Mô tả | Tech |
|-------|-------|------|
| [RAG Chatbot](link) | Hỏi-đáp tài liệu nội bộ, chống bịa | LLM, ChromaDB |
| [Churn Pipeline](link) | Dự đoán churn end-to-end | sklearn, MLflow |
| [MLOps Demo](link) | Train→serve→monitor | Docker, FastAPI |
```

> Giữ ngắn gọn, có link dự án, tech stack rõ. Đây là "trang chủ" của bạn trên GitHub.

---

## Câu 4 — 5 bullet CV ("hành động + công nghệ + kết quả số")

**Công thức:** `[Động từ mạnh] + [cái gì] + [bằng công nghệ gì] + [đạt kết quả số nào]`

1. **Xây dựng** pipeline dự đoán churn end-to-end **bằng** scikit-learn + SMOTE, **đạt** Recall 0.78 trên
   lớp thiểu số (cải thiện 40% so với baseline), giúp xác định khách rời bỏ sớm.

2. **Triển khai** RAG chatbot hỏi-đáp tài liệu nội bộ **dùng** ChromaDB + hybrid search (BM25+vector) +
   reranker, **giảm** thời gian tra cứu thủ công ~70%, có trích dẫn nguồn chống bịa.

3. **Đóng gói** model ML lên production **bằng** FastAPI + Docker + MLflow registry, **đạt** latency P95
   < 200ms, kèm giám sát drift tự động (KS test) trigger retrain.

4. **Fine-tune** LLM 7B cho domain CSKH tiếng Việt **bằng** QLoRA trên 1 GPU, **giảm** chi phí huấn luyện
   ~75% nhờ quantization 4-bit, cải thiện giọng văn nhất quán thương hiệu.

5. **Kiểm toán** công bằng model **bằng** SHAP + Disparate Impact analysis, **phát hiện** bias theo nhóm
   tuổi (DI=0.53) và đề xuất reweighting, soạn Model Card minh bạch.

> Mỗi bullet đều có **động từ mạnh** (xây/triển khai/đóng gói) + **công nghệ cụ thể** + **con số đo được**.

---

## Câu 5 — Sửa 1 bullet "xấu" → "tốt"

**❌ Bullet XẤU:**
> "Làm một dự án machine learning dự đoán khách hàng rời bỏ, sử dụng Python và đạt kết quả tốt."

**✅ Bullet TỐT:**
> "Xây dựng pipeline dự đoán churn bằng scikit-learn + SMOTE xử lý dữ liệu mất cân bằng (3:1), đạt
> Recall 0.78 và F1 0.61 trên lớp churn, giúp đội CSKH ưu tiên đúng nhóm khách rủi ro cao."

**Đã cải thiện gì:**
| Vấn đề bullet xấu | Cách sửa |
|-------------------|----------|
| "Làm một dự án" — động từ yếu | → "Xây dựng pipeline" (động từ mạnh, cụ thể) |
| "sử dụng Python" — mơ hồ | → "scikit-learn + SMOTE" (công nghệ cụ thể, cho thấy biết xử lý mất cân bằng) |
| "đạt kết quả tốt" — KHÔNG đo được | → "Recall 0.78, F1 0.61" (con số cụ thể) |
| Không có impact | → "giúp CSKH ưu tiên khách rủi ro cao" (business value) |

> Nguyên tắc: nhà tuyển dụng đọc CV trong ~6 giây. Bullet mơ hồ = bị bỏ qua. **Con số = đáng tin = nổi bật.**

---

## Câu 6 — Headline LinkedIn

**Công thức:** `[Vai trò mục tiêu] | [Chuyên môn cụ thể] | [Giá trị/điểm khác biệt]`

**Ví dụ theo vị trí:**

- **Nhắm ML Engineer:**
  > "Machine Learning Engineer | LLM & RAG Systems | Xây AI production-ready từ notebook đến Docker"

- **Nhắm MLOps:**
  > "MLOps Engineer | Đưa ML lên production: MLflow, Docker, CI/CD | Model monitoring & drift detection"

- **Nhắm Data/AI Engineer (fresher):**
  > "Aspiring AI/ML Engineer | Python · PyTorch · LLM | Vừa hoàn thành 15+ dự án ML end-to-end"

**Mẹo headline tốt:**
- Có **từ khoá** nhà tuyển dụng/recruiter search (ML Engineer, LLM, MLOps...).
- Cụ thể hơn "Software Engineer" chung chung.
- Thể hiện **điểm khác biệt** (production-ready, có demo, domain cụ thể).

> 🔗 **[Viết headline của riêng bạn ở đây]**

---

## Câu 7 — Pitch 90 giây

**Cấu trúc:** Bạn là ai → Làm được gì (bằng chứng) → Muốn gì → Vì sao phù hợp.

> "Chào anh/chị, em là [Tên]. Em là [background — vd kỹ sư/sinh viên] chuyển hướng sâu vào AI/ML,
> và vừa hoàn thành một khoá học chuyên sâu với hơn 15 dự án thực hành end-to-end.
>
> Điểm em tự hào nhất là không chỉ train được model trong notebook, mà **đưa được lên production**:
> em đã xây một pipeline churn hoàn chỉnh với FastAPI + Docker + MLflow, có giám sát drift tự động;
> và một RAG chatbot hỏi-đáp tài liệu tiếng Việt có trích dẫn nguồn để chống bịa.
>
> Em đặc biệt hứng thú với [LLM/MLOps] vì [lý do cá nhân ngắn]. Em đang tìm vị trí [vai trò mục tiêu]
> nơi em có thể [đóng góp gì]. Với nền tảng vừa rộng — từ ML cổ điển, LLM, đến MLOps — vừa có tư duy
> production, em tin mình có thể đóng góp ngay. Em rất mong được trao đổi thêm ạ."

**Mẹo:** ~150-180 từ ≈ 90 giây. Tập nói trôi chảy, KHÔNG đọc. Có **1-2 con số/dự án cụ thể** làm bằng chứng.
Kết bằng lời mời trao đổi.

> 🎥 **[Quay video 90s hoặc viết bản của bạn]**

---

## Câu 8 — ML System Design (khung 5 bước)

**Đề mẫu: Thiết kế hệ thống phát hiện gian lận giao dịch (Fraud Detection)**

### Khung 5 bước: Problem → Data → Model → Eval → Deploy

**1️⃣ PROBLEM (Làm rõ bài toán)**
- Mục tiêu: phát hiện giao dịch gian lận **real-time** trước khi duyệt.
- Ràng buộc: latency thấp (<100ms), gian lận cực hiếm (~0.1% — mất cân bằng nặng).
- Trade-off: chặn nhầm giao dịch thật (false positive) làm phiền khách vs bỏ sót gian lận (false negative)
  gây mất tiền. → ưu tiên **Recall** nhưng kiểm soát FP.

**2️⃣ DATA**
- Nguồn: lịch sử giao dịch (số tiền, thời gian, địa điểm, thiết bị, merchant), hồ sơ khách.
- Feature: tần suất giao dịch, độ lệch so với hành vi thường, vị trí bất thường, velocity (nhiều GD/phút).
- Thách thức: mất cân bằng cực đoan → SMOTE/undersampling; nhãn trễ (gian lận xác nhận sau vài ngày).

**3️⃣ MODEL**
- Baseline: Logistic Regression / Gradient Boosting (XGBoost) — nhanh, giải thích được.
- Nâng cao: thêm graph features (mạng lưới giao dịch), hoặc anomaly detection cho gian lận kiểu mới.
- Real-time → model nhẹ, inference nhanh.

**4️⃣ EVAL**
- Metric: **Recall** (bắt được gian lận), **Precision** (không làm phiền khách), **PR-AUC** (hợp dữ liệu
  mất cân bằng hơn ROC-AUC). Theo dõi $ tổn thất ngăn được vs $ chi phí review.
- Offline (backtest theo thời gian, KHÔNG shuffle) + online (A/B test, shadow mode).

**5️⃣ DEPLOY**
- Serve: API real-time, feature store cho feature tính sẵn, fallback rule-based khi model fail.
- Monitor: drift (hành vi gian lận đổi liên tục), latency, tỉ lệ alert. Retrain thường xuyên (gian lận
  tiến hoá nhanh → concept drift mạnh).
- Human-in-the-loop: alert độ tin cao → tự chặn; trung bình → đội review thủ công.

> Khung này áp dụng cho MỌI bài system design (recommendation, search, ETA...). Nhớ: luôn **hỏi làm rõ
> ràng buộc trước**, nói **trade-off**, và đừng quên **monitoring/retrain** (phần nhiều người bỏ sót).

---

## Câu 9 — Câu chuyện STAR

**Câu hỏi:** "Kể về một dự án ML bạn đã làm."

**Cấu trúc STAR:** Situation → Task → Action → Result.

> **Situation (Bối cảnh):** Trong khoá học, em nhận thấy nhiều doanh nghiệp SME Việt Nam tốn nhiều thời
> gian cho nhân viên hỏi-đáp chính sách nội bộ lặp đi lặp lại, nên em quyết định xây một RAG chatbot
> giải quyết vấn đề này.
>
> **Task (Nhiệm vụ):** Mục tiêu của em là xây hệ thống trả lời câu hỏi từ tài liệu nội bộ, yêu cầu
> **chính xác và chống bịa** — vì trả lời sai về chính sách công ty có thể gây hậu quả.
>
> **Action (Hành động):** Em ingest tài liệu, chunk có overlap, embed bằng model tiếng Việt, lưu vào
> ChromaDB. Em thêm **hybrid search** kết hợp BM25 và vector để bắt cả từ khoá lẫn ngữ nghĩa. Quan trọng
> nhất, em thiết kế prompt buộc model **chỉ trả lời dựa trên ngữ cảnh và kèm trích dẫn nguồn**, và test
> kỹ cả câu hỏi KHÔNG có trong tài liệu để đảm bảo model từ chối thay vì bịa.
>
> **Result (Kết quả):** Hệ thống trả lời đúng các câu trong tài liệu kèm nguồn, và từ chối đúng cách với
> câu ngoài phạm vi. Em học được rằng với RAG, **chunking và chống hallucination quan trọng hơn cả việc
> chọn model mạnh** — một bài học em sẽ áp dụng cho mọi dự án LLM sau này.

**Mẹo STAR:** nhấn mạnh **Action** (việc BẠN làm, dùng "em/tôi" không phải "nhóm em") và **Result** có học
hỏi/con số. Tránh kể lan man phần Situation.

---

## Câu 10 — Kế hoạch 30 ngày

**Tuần 1 — Hoàn thiện nền tảng portfolio**
- [ ] Làm đẹp 3 repo mạnh nhất (README + demo GIF + kết quả)
- [ ] Viết Profile README GitHub
- [ ] Cập nhật CV với 5 bullet có số + headline LinkedIn mới
- [ ] Quay/viết pitch 90 giây

**Tuần 2 — Mở rộng hiện diện & networking**
- [ ] Viết 1-2 bài blog/LinkedIn post về 1 dự án (vd "Bài học xây RAG chatbot tiếng Việt")
- [ ] Kết nối 20-30 người trong ngành (recruiter, ML engineer) trên LinkedIn, kèm lời nhắn cá nhân
- [ ] Tham gia 1-2 cộng đồng (VD VNTechies, MLOps VN, các group AI/ML)
- [ ] Xin 2-3 buổi cà phê/call học hỏi (informational interview)

**Tuần 3 — Apply có chiến lược**
- [ ] List 15-20 vị trí phù hợp (đọc kỹ JD, ưu tiên match kỹ năng)
- [ ] Tailor CV cho từng nhóm vị trí (LLM vs MLOps vs DS)
- [ ] Apply 10-15 chỗ, theo dõi bằng spreadsheet
- [ ] Nhờ người trong mạng lưới refer nếu có thể

**Tuần 4 — Luyện phỏng vấn & học tiếp**
- [ ] Luyện coding (LeetCode easy-medium), SQL, ML concept Q&A
- [ ] Luyện 3-5 câu ML system design theo khung 5 bước
- [ ] Mock interview với bạn/mentor
- [ ] **Học tiếp có chủ đích:** chọn 1 chủ đề đào sâu (vd LLM eval, distributed training, hoặc 1 cloud
      cert như AWS ML Specialty) — KHÔNG học lan man, chọn thứ bổ trợ vị trí mục tiêu

> 🎯 **Nguyên tắc 30 ngày:** đừng chờ "đủ giỏi" mới apply — apply song song với học. Phỏng vấn sớm =
> feedback sớm = biết cần cải thiện gì. Networking thường mở cửa nhiều hơn apply lạnh.

---

### 📦 Checklist nộp Capstone
- [ ] Link GitHub đã làm đẹp (≥ 1 repo chuẩn)
- [ ] Profile README
- [ ] CV / 5 bullet points có số
- [ ] Pitch 90 giây (viết hoặc video)
- [ ] Bản phác ML system design
- [ ] (Bonus) Headline LinkedIn + kế hoạch 30 ngày
