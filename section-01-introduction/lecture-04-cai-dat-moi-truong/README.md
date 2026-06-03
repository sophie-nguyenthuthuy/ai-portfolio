# Section 1 · Lecture 4 — Cài đặt môi trường

_Phần của: **Section 1: Giới thiệu & Định hướng**_

**Số slide:** 8

---

## Nội dung slide

### Slide 1

- L4
- LECTURE 4 · ~10 PHÚT
- Cài đặt môi trường
- Python · Anaconda · VS Code · Google Colab

### Slide 2

- LECTURE 4
- Chuẩn bị "xưởng làm việc" của bạn
- 🐍
- Python 3.12
- Ngôn ngữ lập trình chính của Data & AI
- 📦
- Anaconda
- Python + thư viện DS đóng gói sẵn
- 💻
- VS Code
- Editor mạnh nhất cho Python & AI
- ☁️
- Google Colab
- Cloud GPU miễn phí, không cần cài
- "Cài đúng từ đầu để không khổ về sau."

### Slide 3

- BƯỚC 1
- Cài Python & Anaconda
- Tải Anaconda
- anaconda.com/download
- Phiên bản
- Anaconda 2024 · Python 3.12
- Kèm sẵn
- NumPy · Pandas Matplotlib · Jupyter
- Terminal — bash
- $ bash Anaconda3-2024.10.py
- Welcome to Anaconda3 2024.10
- In order to continue the installation process,
- please review the license agreement.
- $ conda --version
- conda 24.9.2
- $
- ▶
- SCREEN RECORDING
- Tải & cài Anaconda step-by-step

### Slide 4

- BƯỚC 2 — QUAN TRỌNG
- Virtual environment
- Tại sao cần?
- Mỗi dự án có "phòng riêng" — thư viện không xung đột nhau
- Lệnh tạo env
- conda create -n ai-course python=3.12
- Lệnh kích hoạt
- conda activate ai-course
- Terminal — bash
- $ conda create -n ai-course python=3.12
- Collecting package metadata: done
- Solving environment: done
- $ conda activate ai-course
- (ai-course) $
- ▶
- SCREEN RECORDING
- Tạo và kích hoạt virtual environment

### Slide 5

- BƯỚC 3
- VS Code & Extensions
- Cài Extensions
- 🐍 Python (Microsoft)
- 📓 Jupyter (Microsoft)
- 🤖 GitHub Copilot
- ⚠️ Lỗi thường gặp #1
- Chọn sai Python interpreter — phải chọn env ai-course
- VS Code — settings.json
- // Python interpreter
- "python.defaultInterpreterPath":
- "~/anaconda3/envs/ai-course/bin/python"
- // Jupyter kernel → ai-course ✓
- "jupyter.kernelSpec":"ai-course"
- ▶
- SCREEN RECORDING
- Cài extension + chọn đúng Python interpreter

### Slide 6

- BƯỚC 4 — CLOUD OPTION
- Google Colab — GPU miễn phí
- Lợi thế
- ☁️ Chạy trên cloud
- 🆓 GPU/TPU miễn phí
- 📦 Không cần cài gì
- 🔗 Chia sẻ dễ dàng
- Dùng cho
- Deep Learning · LLM · Bài cần GPU mạnh
- colab.research.google.com
- colab.research.google.com
- [1]
- import torch
- print("GPU:", torch.cuda.get_device_name(0))
- GPU: Tesla T4
- ▶
- SCREEN RECORDING
- Mở Colab, chạy ô code đầu tiên với GPU

### Slide 7

- KIỂM TRA
- Môi trường đã sẵn sàng chưa?
- Chạy 2 lệnh này — nếu OK là sẵn sàng:
- python --version
- → Kỳ vọng: Python 3.12.x
- import pandas, numpy
- → Không báo lỗi = thành công
- Terminal (ai-course)
- (ai-course) $ python --version
- Python 3.12.4
- (ai-course) $ python -c "import pandas, numpy; print('OK')"
- OK ✓
- (ai-course) $
- ▶
- SCREEN RECORDING
- Kiểm tra môi trường cài đặt thành công

### Slide 8

- ✓
- Môi trường xong!
- Bài tiếp: Git & GitHub — lưu code và xây portfolio →
- "Giờ ta cần nơi lưu code — đó là Git."

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_