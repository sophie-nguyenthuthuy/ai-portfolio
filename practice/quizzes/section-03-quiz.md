# Quiz — Section 3: SQL & CƠ SỞ DỮ LIỆU

_10 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Sự khác biệt giữa `WHERE` và `HAVING`?
- A. Không khác nhau
- B. ✅ WHERE lọc dòng trước khi gom nhóm, HAVING lọc nhóm sau GROUP BY
- C. HAVING nhanh hơn WHERE
- D. WHERE chỉ dùng với JOIN
*Giải thích: câu hỏi phỏng vấn kinh điển — thứ tự: WHERE → GROUP BY → HAVING.*

**Câu 2.** JOIN nào giữ tất cả dòng của bảng bên trái, kể cả không khớp?
- A. INNER JOIN
- B. ✅ LEFT JOIN
- C. RIGHT JOIN
- D. CROSS JOIN
*Giải thích: LEFT JOIN giữ toàn bộ bảng trái, dòng không khớp điền NULL.*

**Câu 3.** Window function khác GROUP BY ở điểm nào?
- A. Window function chậm hơn
- B. ✅ Window function tính trên cửa sổ dòng nhưng GIỮ NGUYÊN số dòng, GROUP BY gộp mất dòng
- C. GROUP BY không dùng được với SUM
- D. Không khác nhau
*Giải thích: window function giữ chi tiết từng dòng, rất mạnh cho phân tích.*

**Câu 4.** Index giúp tăng tốc thao tác nào và làm chậm thao tác nào?
- A. Tăng tốc INSERT, làm chậm SELECT
- B. ✅ Tăng tốc SELECT, làm chậm INSERT/UPDATE
- C. Tăng tốc cả hai
- D. Không ảnh hưởng gì
*Giải thích: index tăng tốc đọc nhưng tốn thêm chi phí khi ghi và tốn ổ đĩa.*

**Câu 5.** Hàm window nào lấy giá trị của dòng *trước đó*?
- A. LEAD
- B. ✅ LAG
- C. RANK
- D. ROW_NUMBER
*Giải thích: LAG lấy dòng trước, LEAD lấy dòng sau — dùng tính tăng trưởng.*

**Câu 6.** OLAP được tối ưu cho mục đích gì?
- A. Ghi giao dịch nhanh
- B. ✅ Phân tích, đọc nhiều và tổng hợp dữ liệu
- C. Cập nhật real-time
- D. Lưu trữ ảnh
*Giải thích: OLAP cho phân tích/báo cáo, OLTP cho giao dịch.*

**Câu 7.** Trong star schema, bảng Fact chứa gì?
- A. Mô tả sản phẩm
- B. ✅ Các số đo (metrics) như doanh thu, số lượng
- C. Danh sách khách hàng
- D. Thông tin thời gian
*Giải thích: Fact chứa số đo, Dimension chứa ngữ cảnh (thời gian, sản phẩm...).*

**Câu 8.** CTE (mệnh đề WITH) có ưu điểm gì so với subquery lồng nhiều tầng?
- A. Chạy nhanh hơn nhiều
- B. ✅ Dễ đọc và tái sử dụng hơn
- C. Dùng ít bộ nhớ hơn
- D. Tự động tạo index
*Giải thích: CTE đặt tên truy vấn con, code rõ ràng hơn.*

**Câu 9.** Để chống SQL injection khi nối Python với DB, nên dùng gì?
- A. Nối chuỗi trực tiếp
- B. ✅ Parameterized query (truy vấn tham số hoá)
- C. Tắt firewall
- D. Dùng SELECT *
*Giải thích: parameterized query tách dữ liệu khỏi câu lệnh, chống injection.*

**Câu 10.** `SELECT COUNT(*)` trả về gì?
- A. Tổng giá trị một cột
- B. ✅ Số lượng dòng
- C. Giá trị lớn nhất
- D. Danh sách cột
*Giải thích: COUNT(*) đếm số dòng trong kết quả.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-03-sql/README.md)_
