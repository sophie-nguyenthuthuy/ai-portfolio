# Section 2 · Lecture 12 — NumPy — array, broadcasting, vectorization & hiệu năng

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~10 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- NumPy — động cơ tính toán

**🎨 Visual:** `[AI image]` Lưới số / ma trận phát sáng.
**🎤 Speaker note:** "Pandas xây trên NumPy. Mọi ML đều dùng nó."

### Slide 2 — ndarray vs list

- Array đồng nhất kiểu, nhanh hơn nhiều
- Tốn ít bộ nhớ hơn list

**🎨 Visual:** `[Mermaid]` So sánh list (chậm) vs array (nhanh).
**🎤 Speaker note:** Khác biệt tốc độ rõ khi dữ liệu lớn.

### Slide 3 — Tạo & thao tác array

- `np.array`, `np.zeros`, `np.arange`
- reshape, slicing

**🎨 Visual:** `[Screen]` Tạo array + reshape.
**🎤 Speaker note:** reshape rất hay dùng khi đưa dữ liệu vào model.

### Slide 4 — Vectorization

- Tính trên cả array, không cần for
- Nhanh hơn for hàng chục lần

**🎨 Visual:** `[Screen]` Benchmark for vs vectorized.
**🎤 Speaker note:** "Thấy for trên số liệu lớn → nghĩ ngay tới vectorize."

### Slide 5 — Broadcasting

- Tự "nở" array kích thước khác nhau
- Tính toán không cần lặp tay

**🎨 Visual:** `[Mermaid]` Minh hoạ broadcasting (1×3 + 3×1).
**🎤 Speaker note:** Quy tắc broadcasting — sẽ gặp lại trong deep learning.

### Slide 6 — Dot product & ma trận

- `np.dot`, `@`
- Nền tảng của neural network

**🎨 Visual:** `[Screen]` Nhân ma trận.
**🎤 Speaker note:** Cả deep learning chỉ là phép nhân ma trận lặp lại.

### Slide 7 — Tóm tắt & chuyển bài

- array · vectorize · broadcasting
- Bài tiếp: Matplotlib →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta biến số liệu thành biểu đồ."

---

_← [Về Section README](../README.md)_
