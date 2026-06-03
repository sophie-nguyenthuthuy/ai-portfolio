# Section 7 · Lecture 9 — TensorFlow / Keras cấp tốc

_Phần của: **Section 7: Deep Learning**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 09
- SECTION 7 · LECTURE 9
- TensorFlow / Keras cấp tốc
- ~7 phút · 5 slides

### Slide 2

- SEQUENTIAL
- Sequential API
- sequential.py
- from tensorflow import  keras
- model = keras.Sequential([
- keras.layers.Dense(
- 128, activation="relu" ),
- keras.layers.Dense(
- 10,  activation="softmax" ),
- ])
- Xếp lớp tuần tự, đơn giản
- Nhanh cho các mạng đơn giản

### Slide 3

- FUNCTIONAL
- Functional API
- functional.py
- inp = keras.Input(shape=(784 ,))
- x   = keras.layers.Dense(
- 128, activation="relu" )(inp)
- out = keras.layers.Dense(
- 10, activation="softmax" )(x)
- model = keras.Model(inp, out)
- Mạng phức tạp, nhiều nhánh
- Linh hoạt hơn cho kiến trúc phức tạp

### Slide 4

- TRAIN
- compile · fit · evaluate
- keras_train.py
- model.compile(optimizer="adam" ,
- loss=
- "sparse_categorical_crossentropy" ,
- metrics=[
- "accuracy" ])
- model.fit(X, y, epochs=
- 10, batch_size=32)
- Quy trình train gọn của Keras — viết ngắn hơn PyTorch.

### Slide 5

- SO SÁNH
- PyTorch vs Keras
- PYTORCH
- KERAS
- Phong cách
- Linh hoạt, tường minh
- Ngắn gọn, cấp cao
- Hợp với
- Nghiên cứu, tuỳ biến sâu
- Người mới, prototyping nhanh
- Trong khoá
- Dùng chính
- Biết để đọc code

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_