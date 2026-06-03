# Section 1 · Lecture 5 — Git & GitHub trong 8 phút

_Phần của: **Section 1: Giới thiệu & Định hướng**_

**Số slide:** 8

---

## Nội dung slide

### Slide 1

- L5
- LECTURE 5 · ~8 PHÚT
- Git & GitHub trong 8 phút
- "Đây là kỹ năng nhà tuyển dụng KIỂM TRA đầu tiên."

### Slide 2

- LECTURE 5
- Git vs GitHub — 2 khái niệm hay nhầm
- 🗂️
- Git
- Công cụ quản lý phiên bản
- Chạy trên máy bạn Lưu lịch sử thay đổi
- LOCAL
- ⇄
- push / pull
- ☁️
- GitHub
- Nơi lưu & chia sẻ online
- Cộng tác nhóm Portfolio công khai
- CLOUD

### Slide 3

- Vì sao Git quan trọng với AI Developer?
- 📚
- Lưu lịch sử code & model
- Rollback khi model bị break — không bao giờ mất công trình
- 👥
- Hợp tác nhóm
- Nhiều người cùng làm việc trên 1 codebase — không bị conflict
- 💼
- Portfolio = GitHub profile
- Repo chính là CV của dân kỹ thuật — nhà tuyển dụng xem đầu tiên

### Slide 4

- LECTURE 5
- 4 lệnh cốt lõi — 90% công việc hàng ngày
- add
- Stage thay đổi
- Chọn file sẽ commit
- git add .
- commit
- Lưu snapshot
- Lịch sử vĩnh viễn
- git commit -m "msg"
- push
- Lên GitHub
- Upload lên cloud
- git push origin main
- pull
- Về máy
- Download từ cloud
- git pull origin main

### Slide 5

- THỰC HÀNH 1
- Tạo repo đầu tiên trên GitHub
- 1
- Tạo repo mới trên github.com
- 2
- Clone về máy
- 3
- Mở trong VS Code
- git clone https://github.com/ username/ai-portfolio.git
- Terminal
- $ git clone https://github.com/username/ai-portfolio.git
- Cloning into 'ai-portfolio'...
- remote: Counting objects: 3, done.
- $ cd ai-portfolio
- (ai-portfolio) $
- ▶
- SCREEN RECORDING
- Tạo repo + clone về máy

### Slide 6

- THỰC HÀNH 2
- Commit & Push lên GitHub
- Quy trình chuẩn
- git add .
- git commit -m "message"
- git push origin main
- 💡 Commit message rõ ràng
- "Add EDA for Titanic dataset" tốt hơn "update file"
- Terminal — ai-portfolio
- $ touch hello.py
- $ git add .
- $ git commit -m "Add hello.py - first commit"
- [main a1b2c3d] Add hello.py - first commit
- $ git push origin main
- ✓ Pushed to github.com/username/ai-portfolio
- ▶
- SCREEN RECORDING
- Thêm file → commit → push lên GitHub

### Slide 7

- THỰC HÀNH 3
- .gitignore & README — điểm cộng lớn
- .gitignore — bỏ file không cần
- *.csv # data lớn
- .env # API keys
- __pycache__/
- README.md — giới thiệu dự án
- Mục tiêu · Tech stack · Cách chạy · Screenshots
- README tốt = điểm cộng lớn với nhà tuyển dụng
- .gitignore
- # Python bytecode
- __pycache__/
- *.py[cod]
- # Large data files
- *.csv
- *.parquet
- # Environment
- .env
- .venv/
- # Jupyter
- .ipynb_checkpoints/
- ▶
- SCREEN RECORDING
- Tạo .gitignore & README cho dự án Python/AI

### Slide 8

- ✓
- Git & GitHub xong!
- Bài cuối Section 1: Tài nguyên & cộng đồng →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_