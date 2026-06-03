# Quiz — Section 2: PYTHON CHO DATA SCIENCE

_10 câu · mỗi câu 1 đáp án đúng (✅) kèm giải thích._

---

**Câu 1.** Trong Python, kiểu dữ liệu nào sau đây là *immutable* (không thể thay đổi)?
- A. list
- B. dict
- C. ✅ tuple
- D. set
*Giải thích: tuple không thể sửa sau khi tạo; list, dict, set đều mutable.*

**Câu 2.** Kết quả của `7 // 2` trong Python là gì?
- A. 3.5
- B. ✅ 3
- C. 1
- D. 4
*Giải thích: `//` là chia lấy phần nguyên (floor division).*

**Câu 3.** Cấu trúc dữ liệu nào phù hợp nhất để lưu cặp khoá–giá trị (vd mã sản phẩm → giá)?
- A. list
- B. tuple
- C. ✅ dict
- D. set
*Giải thích: dictionary lưu key-value và tra cứu nhanh.*

**Câu 4.** Trong Pandas, sự khác biệt cốt lõi giữa `loc` và `iloc` là gì?
- A. loc nhanh hơn iloc
- B. ✅ loc truy cập theo nhãn (label), iloc theo vị trí số (integer position)
- C. iloc chỉ dùng cho Series
- D. Không có khác biệt
*Giải thích: đây là câu hỏi phỏng vấn kinh điển — loc theo label, iloc theo index số.*

**Câu 5.** Vì sao vectorization với NumPy nhanh hơn vòng lặp Python thuần?
- A. Vì NumPy dùng nhiều RAM hơn
- B. ✅ Vì NumPy thực thi phép tính ở tầng C, song song trên cả mảng, tránh overhead vòng lặp Python
- C. Vì NumPy chạy trên GPU mặc định
- D. Vì list nhanh hơn array
*Giải thích: vectorization đẩy tính toán xuống C tối ưu, nhanh hơn nhiều lần.*

**Câu 6.** Để điền giá trị thiếu trong cột thu nhập (dữ liệu lệch), nên dùng giá trị nào?
- A. mean (trung bình)
- B. ✅ median (trung vị)
- C. giá trị max
- D. 0
*Giải thích: median bền với outlier hơn mean trong dữ liệu lệch.*

**Câu 7.** Hàm Pandas nào dùng để gom nhóm và tính tổng hợp?
- A. `merge()`
- B. `pivot()`
- C. ✅ `groupby()`
- D. `concat()`
*Giải thích: groupby theo tư duy split-apply-combine.*

**Câu 8.** `[x**2 for x in range(5)]` tạo ra kết quả gì?
- A. [0, 1, 2, 3, 4]
- B. ✅ [0, 1, 4, 9, 16]
- C. [1, 4, 9, 16, 25]
- D. Lỗi
*Giải thích: list comprehension bình phương 0→4.*

**Câu 9.** Thư viện nào tạo biểu đồ *tương tác* (zoom, hover)?
- A. Matplotlib
- B. Seaborn
- C. ✅ Plotly
- D. NumPy
*Giải thích: Plotly tạo biểu đồ tương tác; Matplotlib/Seaborn tạo ảnh tĩnh.*

**Câu 10.** Câu lệnh `with open('f.txt') as f:` có lợi ích gì?
- A. Đọc file nhanh hơn
- B. ✅ Tự động đóng file kể cả khi có lỗi
- C. Ghi file an toàn hơn
- D. Mã hoá file
*Giải thích: context manager đảm bảo file được đóng đúng cách.*

---

---

_← [Về practice](../README.md) · [Section README](../../section-02-python-for-data-science/README.md)_
