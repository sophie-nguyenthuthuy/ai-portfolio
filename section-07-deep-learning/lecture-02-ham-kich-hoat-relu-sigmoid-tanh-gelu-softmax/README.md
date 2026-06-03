# Section 7 · Lecture 2 — Hàm kích hoạt — ReLU, Sigmoid, Tanh, GELU, Softmax

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Hàm kích hoạt (Activation)

**🎨 Visual:** `[AI image]` Các đường cong activation.
**🎤 Speaker note:** "Không có cái này, mạng chỉ là 1 phép tuyến tính."

### Slide 2 — Vì sao cần phi tuyến

- Xếp chồng tuyến tính vẫn tuyến tính
- Phi tuyến mở khoá sức mạnh

**🎨 Visual:** `[Mermaid]` Tuyến tính vs phi tuyến.
**🎤 Speaker note:** Đây là lý do tồn tại của activation.

### Slide 3 — Sigmoid & Tanh

- Sigmoid: [0,1]
- Tanh: [-1,1]
- Vấn đề vanishing gradient

**🎨 Visual:** `[Mermaid]` 2 đường cong.
**🎤 Speaker note:** Cũ, ít dùng ở lớp ẩn hiện nay.

### Slide 4 — ReLU & biến thể

- ReLU: đơn giản, hiệu quả
- Leaky ReLU, GELU

**🎨 Visual:** `[Mermaid]` ReLU + biến thể.
**🎤 Speaker note:** ReLU là mặc định cho lớp ẩn.

### Slide 5 — Softmax

- Cho lớp output phân loại nhiều lớp
- Biến số thành xác suất tổng = 1

**🎨 Visual:** `[Mermaid]` Softmax → phân phối xác suất.
**🎤 Speaker note:** Dùng ở output, không ở lớp ẩn.

### Slide 6 — Tóm tắt & chuyển bài

- ReLU · Sigmoid/Tanh · GELU · Softmax
- Bài tiếp: forward propagation →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta xem dữ liệu chảy qua mạng thế nào."

---

_← [Về Section README](../README.md)_
