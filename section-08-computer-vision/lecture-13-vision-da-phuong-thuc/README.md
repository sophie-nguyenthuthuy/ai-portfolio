# Section 8 · Lecture 13 — Vision đa phương thức

_Phần của: **Section 8: Computer Vision**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 13
- LECTURE 13 · ~7 PHÚT · 5 SLIDES
- Vision đa phương thức
- CLIP · BLIP — cầu nối giữa thị giác và ngôn ngữ, nền của GenAI

### Slide 2

- L13 · CLIP
- Ảnh & text trong cùng một không gian
- Học ảnh và mô tả text khớp nhau
- Zero-shot: phân loại không cần train thêm
- 🖼️ Image encoder
- 📝 Text encoder
- →
- Không gian
- embedding
- chung

### Slide 3

- L13 · ỨNG DỤNG CLIP
- Tìm ảnh bằng câu mô tả
- "một chú mèo cam đang ngủ"
- câu mô tả
- →
- CLIP so khớp
- →
- ảnh ✓
- ảnh
- Cũng là nền cho Stable Diffusion — gặp lại ở Section Generative AI.

### Slide 4

- L13 · BLIP
- Mô tả ảnh & hỏi-đáp về ảnh
- ảnh
- Captioning
- "Một người đang lướt sóng"
- ↓
- VQA
- Hỏi: "Mấy người?" → "Một"
- Nền cho các multimodal LLM.

### Slide 5

- L13 · TÓM TẮT
- Nối ảnh với ngôn ngữ:
- CLIP
- BLIP
- multimodal
- BÀI TIẾP
- →
- Triển khai edge — đưa model lên thiết bị thật

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_