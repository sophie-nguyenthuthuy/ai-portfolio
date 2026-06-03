# Section 2 · Lecture 7 — Lập Trình Hướng Đối Tượng (OOP) trong Python

_Phần của: **Section 2: Python cho Data Science**_

**Số slide:** 7

---

## Nội dung slide

### Slide 1

- LECTURE
- 07
- ~10 phút
- SECTION 2 — PYTHON CHO DATA SCIENCE
- Lập Trình Hướng Đối Tượng (OOP) trong Python
- class / object
- __init__
- method
- inheritance

### Slide 2

- Class & Object
- Class
- = bản thiết kế (blueprint)
- Object
- = thực thể được tạo từ class
- Ví von: class = khuôn đúc bánh → object = từng cái bánh
- PyTorch, scikit-learn đều dùng class — hiểu OOP = đọc được thư viện
- class KhachHang
- ↓ tạo object
- an = KhachHang()
- binh = KhachHang()
- cuong = KhachHang()
- 💡
- Mỗi object có attributes (thuộc tính) và methods (hành vi) riêng

### Slide 3

- Thuộc Tính & __init__
- __init__
- = hàm khởi tạo — chạy khi tạo object
- self
- = chính object đó — luôn là tham số đầu
- Thuộc tính (attribute) gán qua
- self.ten = ...
- __init__
- là dunder method — Python gọi tự động
- oop_init.py
- class KhachHang :
- def __init__(self, ten, tuoi, chi_tieu ):
- self.ten = ten         self.tuoi = tuoi         self.chi_tieu = chi_tieu # Tạo object an = KhachHang("An", 28, 12_000_000) binh = KhachHang("Bình", 35, 4_500_000) print(an.ten)        # "An" print(binh.chi_tieu) # 4_500_000

### Slide 4

- Method — Hành Vi Của Object
- Method = hàm định nghĩa bên trong class
- Luôn có
- self
- là tham số đầu tiên
- Method =
- động từ
- của object
- Gọi bằng:
- object.method()
- oop_method.py
- class KhachHang :
- def __init__(self, ten, chi_tieu ):
- self.ten = ten         self.chi_tieu = chi_tieu     def phan_khuc(self ):
- if self.chi_tieu >= 10_000_000 :
- return "VIP"         return "Phổ thông"     def __repr__(self ):
- return f"KH({self.ten})" an = KhachHang("An", 12_000_000) print(an.phan_khuc())  # VIP

### Slide 5

- Kế Thừa — Inheritance
- Class con
- kế thừa
- tất cả từ class cha
- Tái sử dụng + mở rộng thêm tính năng
- super().__init__()
- gọi init của cha
- Gặp lại khi viết model PyTorch:
- class Model(nn.Module)
- inheritance.py
- class NguoiDung:            # class cha     def __init__(self, ten ):
- self.ten = ten     def chao(self ):
- return f"Xin chào {self.ten}" class Admin(NguoiDung):       # kế thừa     def __init__(self, ten, quyen ):
- super().__init__(ten)   # gọi cha         self.quyen = quyen     def xoa_user(self, uid): ... a = Admin("An", "superadmin") print(a.chao())  # Xin chào An

### Slide 6

- Vì Sao Dân Data Cần OOP?
- PyTorch, scikit-learn đều dùng class
- Hiểu OOP =
- đọc được code thư viện
- Viết model PyTorch = kế thừa
- nn.Module
- Không cần master OOP — cần hiểu để đọc code
- 💡
- Mọi thứ trong Python đều là object: int, list, function đều là class
- pytorch_preview.py
- import torch.nn as nn # Model PyTorch = kế thừa nn.Module class LinearModel(nn.Module ):
- def __init__(self ):
- super().__init__ ()
- self.linear = nn.Linear(10, 1 )
- def forward(self, x ):
- return self.linear(x) model = LinearModel() # Sẽ học chi tiết ở phần Deep Learning

### Slide 7

- LECTURE 07 — TÓM TẮT
- OOP trong Python
- class = bản thiết kế · object = thực thể
- __init__ khởi tạo · self = chính object
- method = hành vi của object
- Kế thừa = tái sử dụng + mở rộng
- PyTorch / scikit-learn đều dùng OOP
- →
- Bài tiếp: Module, Package & Virtual Environment

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_