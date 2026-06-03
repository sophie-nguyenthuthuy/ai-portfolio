# Section 11 · Lecture 6 — Vai trò system / user / assistant, prompt template

_Phần của: **Section 11: Large Language Models**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 06
- SECTION 11 · LECTURE 06
- Vai trò system / user / assistant, prompt template
- ~6 phút · 5 slides

### Slide 2

- L06 · ROLES & TEMPLATE
- Ba vai trò hội thoại
- System prompt định "tính cách" model
- SYSTEM
- Định hướng hành vi
- vai trò, ràng buộc
- USER
- Câu hỏi
- yêu cầu của người dùng
- ASSISTANT
- Trả lời
- phản hồi của model

### Slide 3

- L06 · ROLES & TEMPLATE
- System prompt
- Đặt ngữ cảnh, vai trò, ràng buộc
- Nơi kiểm soát model mạnh nhất
- messages.py
- messages = [
- { "role": "system" ,
- "content": "Bạn là trợ lý CSKH, trả lời ngắn gọn, lịch sự." },
- { "role": "user", "content": "Đơn của tôi đâu rồi?" },
- ]

### Slide 4

- L06 · ROLES & TEMPLATE
- Prompt template
- Mẫu prompt có biến
- Tái sử dụng, nhất quán cho sản phẩm
- template.py
- prompt =  """Tóm tắt văn bản sau trong {n} câu:
- {document}""" prompt.format(n=3, document=text)

### Slide 5

- L06 · ROLES & TEMPLATE — TÓM TẮT
- Tóm tắt
- system / user / assistant
- prompt template
- BÀI TIẾP
- Function calling / tool use
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_