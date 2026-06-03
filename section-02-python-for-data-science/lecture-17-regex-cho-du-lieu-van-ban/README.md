# Section 2 · Lecture 17 — Regex cho dữ liệu văn bản

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6 · ~7 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Regex — săn mẫu trong văn bản

**🎨 Visual:** `[AI image]` Kính lúp trên chuỗi ký tự.
**🎤 Speaker note:** "Trông đáng sợ nhưng cực mạnh khi làm sạch dữ liệu."

### Slide 2 — Regex là gì

- Mẫu (pattern) để tìm/thay thế chuỗi
- Thư viện `re`

**🎨 Visual:** `[Mermaid]` Pattern → matches.
**🎤 Speaker note:** Dùng cho email, số điện thoại, mã đơn hàng.

### Slide 3 — Ký hiệu cốt lõi

- `\d` số · `\w` chữ · `.` bất kỳ
- `+ * ?` số lần lặp

**🎨 Visual:** `[Mermaid]` Bảng ký hiệu thường dùng.
**🎤 Speaker note:** Chỉ cần nhớ vài ký hiệu là làm được 80% việc.

### Slide 4 — Hàm re chính

- `re.search`, `re.findall`
- `re.sub` (thay thế)

**🎨 Visual:** `[Screen]` Trích email từ văn bản.
**🎤 Speaker note:** findall lấy tất cả; search lấy đầu tiên.

### Slide 5 — Ví dụ thực tế

- Tách số điện thoại VN
- Làm sạch text trước NLP

**🎨 Visual:** `[Screen]` Chuẩn hoá chuỗi bẩn.
**🎤 Speaker note:** Bước tiền xử lý quan trọng cho NLP sau này.

### Slide 6 — Tóm tắt & chuyển bài

- pattern · ký hiệu · re.findall/sub
- Bài tiếp: Mini-Project →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ráp tất cả lại trong 1 dự án thật."

---

_← [Về Section README](../README.md)_
