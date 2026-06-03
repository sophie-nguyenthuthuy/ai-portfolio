# Section 2 · Lecture 8 — Module, Package, Import & Virtual Environment

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- LECTURE
- 08
- ~8 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Module, Package, Import & Virtual Environment
- module
- import
- pip / PyPI
- venv

### Slide 2

- Module & import
- Module
- = 1 file .py với code tái sử dụng
- import ten_module
- — import cả module
- from m import x
- — import phần cụ thể
- as
- — đặt alias ngắn gọn
- Không ai viết tất cả trong 1 file — tách theo chức năng
- imports.py
- # Import cả module import math print(math.sqrt(16))     # 4.0 # Import phần cụ thể from math import pi, factorial print(pi)                 # 3.14159... # Alias phổ biến trong Data Science import pandas as pd import numpy as np import matplotlib.pyplot as plt # Import từ file của mình from utils import tinh_vat, xu_ly

### Slide 3

- Package — Cây Thư Mục Code
- Package
- = thư mục chứa nhiều module
- Mỗi package có file
- __init__.py
- pandas, numpy chính là các package
- Cấu trúc package chuẩn giúp code dễ bảo trì
- 💡
- __init__.py có thể rỗng — chỉ để Python nhận diện đây là package
- my_project/
- ├── data/
- │ ├── __init__.py
- │ ├── loader.py
- │ └── cleaner.py
- ├── models/
- │ ├── __init__.py
- │ └── train.py
- ├── main.py
- └── requirements.txt

### Slide 4

- pip & PyPI
- pip
- = công cụ cài thư viện Python
- PyPI
- = kho 500,000+ thư viện mở — "App Store của Python"
- pip install ten
- — cài thư viện
- pip list
- — xem thư viện đã cài
- pip install pandas==2.1.0
- — chỉ định phiên bản
- terminal
- # Cài thư viện $ pip install pandas numpy matplotlib seaborn # Cài phiên bản cụ thể $ pip install pandas==2.1.4 # Cài từ requirements.txt $ pip install -r requirements.txt # Xem đã cài gì $ pip list
- $ pip show pandas
- # Gỡ cài đặt $ pip uninstall ten_thu_vien

### Slide 5

- Virtual Environment
- Mỗi dự án có
- môi trường riêng
- — tránh xung đột phiên bản
- requirements.txt
- — ghi lại tất cả thư viện
- Người khác chạy
- pip install -r
- là có đủ
- Trong khoá này dùng Google Colab — đã có venv sẵn
- terminal
- # Tạo virtual environment $ python -m venv .venv # Kích hoạt (macOS/Linux) $ source .venv/bin/activate # Kích hoạt (Windows) $ .venvScriptsactivate # Cài thư viện vào venv $ pip install pandas numpy # Lưu ra requirements.txt $ pip freeze > requirements.txt # Tắt venv $ deactivate

### Slide 6

- LECTURE 08 — TÓM TẮT
- Module, Package & Virtual Environment
- Module = file .py · import / from / as
- Package = thư mục chứa nhiều module
- pip install · PyPI — App Store của Python
- venv — môi trường riêng mỗi dự án
- requirements.txt — đảm bảo reproducibility
- →
- Bài tiếp: Đọc/Ghi File & Xử Lý Lỗi

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_