# Section 2 · Lecture 10 — Pandas Phần 1 — Series, DataFrame, indexing

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7 · ~11 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Pandas — Excel trên steroid

**🎨 Visual:** `[AI image]` Logo Pandas + bảng dữ liệu.
**🎤 Speaker note:** "90% thời gian làm data là với Pandas."

### Slide 2 — Series vs DataFrame

- Series = 1 cột
- DataFrame = bảng (nhiều cột)

**🎨 Visual:** `[Mermaid]` Series → ghép thành DataFrame.
**🎤 Speaker note:** Hình dung DataFrame như 1 sheet Excel.

### Slide 3 — Đọc dữ liệu

- `pd.read_csv()`, `read_excel()`
- `.head()`, `.info()`, `.describe()`

**🎨 Visual:** `[Screen]` Đọc CSV + head().
**🎤 Speaker note:** 3 lệnh đầu tiên với mọi dataset mới.

### Slide 4 — Chọn cột & dòng

- `df['cot']`, `df[['c1','c2']]`
- Lọc theo điều kiện

**🎨 Visual:** `[Screen]` Lọc df[df['tuoi']>30].
**🎤 Speaker note:** Boolean indexing — dùng cực nhiều.

### Slide 5 — loc vs iloc

- `loc` = theo nhãn (label)
- `iloc` = theo vị trí (số)

**🎨 Visual:** `[Mermaid]` Bảng minh hoạ loc vs iloc.
**🎤 Speaker note:** ⚠️ Câu hỏi phỏng vấn kinh điển.

### Slide 6 — Thêm/sửa/xoá cột

- Tạo cột mới từ cột cũ
- `drop()` để xoá

**🎨 Visual:** `[Screen]` Tạo cột tính toán.
**🎤 Speaker note:** Đây là bước đầu feature engineering.

### Slide 7 — Tóm tắt & chuyển bài

- Series · DataFrame · loc/iloc
- Bài tiếp: Pandas nâng cao →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta gộp, nối và làm sạch dữ liệu thật."

---

_← [Về Section README](../README.md)_
