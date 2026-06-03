# Section 10 · Lecture 3 — GAN — Generator, Discriminator, động lực huấn luyện

_Phần của: **Section 10: Generative AI**_

**Số slide:** 6 · ~9 phút

---

## Nội dung slide

### Slide 1 — Tiêu đề

- GAN — cuộc đấu của 2 mạng

**🎨 Visual:** `[AI image]` Hoạ sĩ giả vs giám định.
**🎤 Speaker note:** "Hai mạng đối đầu nhau để cùng giỏi lên."

### Slide 2 — Generator vs Discriminator

- Generator: tạo ảnh giả
- Discriminator: phân biệt thật/giả

**🎨 Visual:** `[Mermaid]` G tạo, D phán.
**🎤 Speaker note:** Ví von: kẻ làm giả vs cảnh sát.

### Slide 3 — Trò chơi đối kháng

- G cố lừa D, D cố bắt G
- Cùng tiến bộ

**🎨 Visual:** `[Mermaid]` Minimax game.
**🎤 Speaker note:** Cân bằng = ảnh giả như thật.

### Slide 4 — Khó khăn khi train

- Không ổn định, mode collapse

**🎨 Visual:** `[Mermaid]` Train dao động.
**🎤 Speaker note:** GAN nổi tiếng khó train.

### Slide 5 — StyleGAN, CycleGAN

- StyleGAN: mặt người siêu thực
- CycleGAN: chuyển phong cách

**🎨 Visual:** `[AI image]` Ảnh StyleGAN.
**🎤 Speaker note:** Ứng dụng nổi tiếng của GAN.

### Slide 6 — Tóm tắt & chuyển bài

- Generator/Discriminator · minimax · StyleGAN
- Bài tiếp: StyleGAN & CycleGAN →

**🎨 Visual:** `[AI image]` Mũi tên tiến.
**🎤 Speaker note:** "Đi sâu hơn vào ứng dụng image-to-image."

---

_← [Về Section README](../README.md)_
