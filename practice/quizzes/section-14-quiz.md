# Quiz — Section 14: MLOps & PRODUCTION

_12 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Bốn trụ cột của MLOps là gì?
- A. Train, test, deploy, monitor
- B. ✅ Code, Data, Model, Hạ tầng (Infrastructure)
- C. Python, SQL, Docker, K8s
- D. Encode, decode, serve, scale
*Giải thích: cả 4 đều cần version & quản lý.*

**Câu 2.** Experiment tracking (MLflow) giải quyết vấn đề gì?
- A. Train nhanh hơn
- B. ✅ Ghi lại params/metrics/artifacts để so sánh & tái lập thí nghiệm
- C. Triển khai model
- D. Làm sạch dữ liệu
*Giải thích: tránh "model tốt mà không nhớ chạy sao".*

**Câu 3.** Vì sao cần version dữ liệu (DVC) chứ không chỉ version code?
- A. Để dữ liệu nhỏ hơn
- B. ✅ Vì cùng code khác data → kết quả khác; cần cả hai để tái lập (reproducibility)
- C. Để chạy nhanh hơn
- D. Không cần thiết
*Giải thích: reproducibility cần version cả data + code + model.*

**Câu 4.** Feature store giúp tránh vấn đề gì?
- A. Overfitting
- B. ✅ Training-serving skew (feature tính khác nhau lúc train và serve)
- C. Vanishing gradient
- D. Data leakage
*Giải thích: cùng định nghĩa feature cho cả offline & online.*

**Câu 5.** Trong Airflow, DAG là gì?
- A. Một model
- B. ✅ Đồ thị các task có thứ tự phụ thuộc (workflow)
- C. Một database
- D. Một metric
*Giải thích: mỗi bước pipeline là 1 task trong DAG.*

**Câu 6.** Docker giải quyết vấn đề kinh điển nào?
- A. Model thiếu chính xác
- B. ✅ "Trên máy tôi chạy được" — đóng gói cả môi trường để chạy mọi nơi
- C. Thiếu dữ liệu
- D. Overfitting
*Giải thích: container đóng gói app + môi trường.*

**Câu 7.** Sự khác biệt giữa Docker image và container?
- A. Không khác nhau
- B. ✅ Image là bản thiết kế (như class), container là thực thể đang chạy (như object)
- C. Container tạo image
- D. Image chạy được, container thì không
*Giải thích: nối lại class/object — image→container.*

**Câu 8.** Kubernetes giúp gì cho ML serving?
- A. Train model
- B. ✅ Tự co giãn, tự phục hồi, điều phối nhiều container ở quy mô lớn
- C. Làm sạch dữ liệu
- D. Tạo embedding
*Giải thích: autoscale + self-healing cho hệ thống lớn.*

**Câu 9.** Data drift khác concept drift thế nào?
- A. Giống nhau
- B. ✅ Data drift: phân phối input đổi; concept drift: quan hệ input→output đổi
- C. Concept drift chỉ xảy ra với ảnh
- D. Data drift không ảnh hưởng model
*Giải thích: câu hỏi phỏng vấn — cả hai làm model xuống cấp.*

**Câu 10.** TTFT trong LLMOps là gì?
- A. Total Training Free Time
- B. ✅ Time To First Token — thời gian tới token đầu tiên
- C. Tokens To Final Text
- D. Test Then Fine-Tune
*Giải thích: TTFT ảnh hưởng trải nghiệm người dùng nhiều nhất.*

**Câu 11.** Vì sao prompt cũng cần versioning?
- A. Để tốn ít token hơn
- B. ✅ Vì đổi prompt = đổi hành vi model, cần track & A/B test
- C. Để bảo mật
- D. Không cần version prompt
*Giải thích: prompt là 1 phần của hệ thống cần quản lý.*

**Câu 12.** Trong stack lakehouse hiện đại, Debezium đảm nhiệm vai trò gì?
- A. Lưu trữ object
- B. ✅ CDC — bắt thay đổi từ database và stream vào Kafka
- C. Truy vấn dữ liệu
- D. Train model
*Giải thích: Debezium là công cụ Change Data Capture phổ biến.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-14-mlops/README.md)_
