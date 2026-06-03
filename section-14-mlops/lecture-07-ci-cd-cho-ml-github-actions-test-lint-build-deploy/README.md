# Section 14 · Lecture 7 — CI/CD cho ML — GitHub Actions (test, lint, build, deploy)

_Phần của: **Section 14: MLOps & Production**_

**Số slide:** 5

---

## Nội dung slide

### Slide 1

- 07
- SECTION 14 · LECTURE 07
- CI/CD cho ML — GitHub Actions (test, lint, build, deploy)
- ~7 phút · 5 slides

### Slide 2

- L07 · CI/CD
- CI/CD là gì
- CI: tự động test khi push
- CD: tự động deploy
- Push
- →
- Test
- →
- Build
- →
- Deploy

### Slide 3

- L07 · CI/CD
- Khác biệt cho ML
- Test cả data & model
- Reproducibility
- SOFTWARE
- Test code
- unit test
- ML
- + data & model
- test data
- test model

### Slide 4

- L07 · CI/CD
- GitHub Actions
- Tự động test, build Docker, push
- Nối lại Git / GitHub Section 1
- ci.yml
- on : [push]
- jobs:
- test:
- steps:
- -  run : pytest tests/
- -  run: docker build -t app .

### Slide 5

- L07 · CI/CD — TÓM TẮT
- Tóm tắt
- CI/CD
- test data / model
- GitHub Actions
- BÀI TIẾP
- Model serving
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_