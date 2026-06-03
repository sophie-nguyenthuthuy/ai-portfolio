# Section 10 · Lecture 5 — Diffusion model — quá trình thuận & nghịch

_Phần của: **Section 10: Generative AI**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- Diffusion Models

**🎨 Visual:** `[AI image]` Nhiễu dần thành ảnh rõ.
**🎤 Speaker note:** "Công nghệ đằng sau Midjourney, Stable Diffusion."

### Slide 2 — Quá trình thuận (forward)

- Thêm nhiễu dần vào ảnh
- Cho tới khi thành nhiễu thuần

**🎨 Visual:** `[Mermaid]` Ảnh → nhiễu từng bước.
**🎤 Speaker note:** Phá huỷ ảnh có kiểm soát.

### Slide 3 — Quá trình nghịch (reverse)

- Học khử nhiễu từng bước
- Nhiễu → ảnh

**🎨 Visual:** `[Mermaid]` Nhiễu → ảnh từng bước.
**🎤 Speaker note:** Đây là phần model học để sinh ảnh.

### Slide 4 — Vì sao mạnh

- Ổn định hơn GAN
- Chất lượng & đa dạng cao

**🎨 Visual:** `[Mermaid]` Diffusion vs GAN.
**🎤 Speaker note:** Đã vượt GAN về chất lượng.

### Slide 5 — Text-to-image

- Dẫn hướng bằng text (CLIP)
- Nối lại CLIP Section 8

**🎨 Visual:** `[Mermaid]` Text → ảnh.
**🎤 Speaker note:** CLIP làm cầu nối text-ảnh.

### Slide 6 — Tóm tắt & chuyển bài

- forward/reverse · khử nhiễu · text-to-image
- Bài tiếp: Stable Diffusion thực hành →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Giờ ta thực hành tạo ảnh thật."

---

_← [Về Section README](../README.md)_
