# Section 9 · Lecture 2 — Bag-of-Words & TF-IDF

_Phần của: **Section 9: Natural Language Processing**_

**Số slide:** 6 · ~8 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Biểu diễn văn bản: BoW & TF-IDF

**🎨 Visual:** `[AI image]` Túi đựng các từ.
**🎤 Speaker note:** "Cách đơn giản nhất biến văn bản thành số."

### Slide 2 — Bag-of-Words

- Đếm tần suất từ
- Bỏ qua thứ tự

**🎨 Visual:** `[Mermaid]` Văn bản → vector đếm.
**🎤 Speaker note:** Đơn giản nhưng mất ngữ cảnh.

### Slide 3 — Vấn đề của BoW

- Từ phổ biến (và, là) lấn át
- Vector thưa, lớn

**🎨 Visual:** `[Mermaid]` Từ thường lấn át.
**🎤 Speaker note:** Cần cân nhắc tầm quan trọng của từ.

### Slide 4 — TF-IDF

- Term Frequency × Inverse Doc Frequency
- Đề cao từ đặc trưng

**🎨 Visual:** `[Mermaid]` Công thức TF-IDF.
**🎤 Speaker note:** Từ hiếm mà quan trọng được điểm cao.

### Slide 5 — Ứng dụng

- Phân loại văn bản, tìm kiếm
- Baseline mạnh & nhanh

**🎨 Visual:** `[Screen]` TfidfVectorizer.
**🎤 Speaker note:** Vẫn dùng nhiều dù đã có deep learning.

### Slide 6 — Tóm tắt & chuyển bài

- BoW · TF-IDF · baseline
- Bài tiếp: word embedding →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta cho từ một 'ý nghĩa' thực sự."

---

_← [Về Section README](../README.md)_
