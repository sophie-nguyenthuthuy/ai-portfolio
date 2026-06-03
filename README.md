# Mastering AI & Data Science

> _Từ con số 0 đến AI Engineer thực chiến._ — Khoá học toàn diện bằng **tiếng Việt**.

Repo đồng hành của khoá học: slide theo từng lecture, mã nguồn, dataset và bài thực hành.
**16 sections · ~198 lectures · 7 Capstone projects.**

## Lộ trình

| # | Section | Lectures | Capstone | Trạng thái |
|---|---------|:--------:|:--------:|:----------:|
| 1 | [Giới thiệu & Định hướng](section-01-introduction/README.md) | 6 |  | ✅ |
| 2 | [Python cho Data Science](section-02-python-for-data-science/README.md) | 18 |  | ✅ |
| 3 | [SQL — Cơ sở dữ liệu & truy vấn](section-03-sql/README.md) | 12 |  | ✅ |
| 4 | [Toán & Thống kê cho AI](section-04-math-and-statistics/README.md) | — |  | 🚧 |
| 5 | [Machine Learning Fundamentals](section-05-machine-learning-fundamentals/README.md) | 20 | 🏆1 | ✅ |
| 6 | [Time Series — Dự báo chuỗi thời gian](section-06-time-series/README.md) | 9 | 🏆2 | ✅ |
| 7 | [Deep Learning](section-07-deep-learning/README.md) | 12 |  | ✅ |
| 8 | [Computer Vision](section-08-computer-vision/README.md) | 16 | 🏆3 | ✅ |
| 9 | [Natural Language Processing](section-09-nlp/README.md) | — | 🏆4 | 🚧 |
| 10 | [Generative AI](section-10-generative-ai/README.md) | — |  | 🚧 |
| 11 | [Large Language Models](section-11-large-language-models/README.md) | 14 |  | ✅ |
| 12 | [RAG & Vector Database](section-12-rag/README.md) | 11 | 🏆5 | ✅ |
| 13 | [Agentic AI](section-13-agentic-ai/README.md) | 11 | 🏆6 | ✅ |
| 14 | [MLOps & Production](section-14-mlops/README.md) | 16 | 🏆7 | ✅ |
| 15 | [Responsible AI](section-15-responsible-ai/README.md) | 6 |  | ✅ |
| 16 | [Career & Interview](section-16-career/README.md) | 10 |  | ✅ |

✅ = có slide deck & nội dung &nbsp;·&nbsp; 🚧 = đang bổ sung &nbsp;·&nbsp; 🏆N = Capstone project N

> Đã import nội dung slide cho **161 lectures / 961 slides** từ các deck .pptx.
> Sections 4 (Toán & Thống kê), 9 (NLP), 10 (Generative AI) chưa có deck nguồn — đã scaffold sẵn khung.

## Cấu trúc repo

```
section-NN-slug/
├── README.md              # mục tiêu + danh sách lecture
├── slides.pptx            # slide deck của section
└── lecture-NN-slug/
    └── README.md          # nội dung slide của lecture đó
```

## 7 Capstone Projects (portfolio)

1. **Churn Prediction** — Section 5
2. **Dự báo doanh số / chứng khoán VN** — Section 6
3. **Computer Vision thực chiến** (ảnh y tế / OCR hoá đơn) — Section 8
4. **Sentiment / Chatbot tiếng Việt** — Section 9
5. **RAG chatbot tài liệu nội bộ cho SME** — Section 12
6. **Research Agent (LangGraph)** — Section 13
7. **Pipeline MLOps production đầy đủ** — Section 14

## Bắt đầu

```bash
# tạo môi trường
conda create -n ai-course python=3.12 && conda activate ai-course
pip install -r requirements.txt
```

Một số thư viện nặng / theo section (PyTorch, TensorFlow, Prophet, bitsandbytes…) được ghi chú trong `requirements.txt` — chỉ cài khi học tới section tương ứng.
