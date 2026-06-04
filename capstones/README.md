# Capstone Projects — Production-Grade

7 end-to-end, production-grade projects — the portfolio payload of the course.
Each is a self-contained service following the **same platform blueprint**:
typed config, training pipeline with **MLflow** tracking, a **FastAPI** service
with `/health` · `/ready` · Prometheus `/metrics`, **pytest** suite (green
offline), **Docker + docker-compose**, **Kubernetes** manifests, **Terraform**
skeleton, and a **GitHub Actions** CI workflow.

| # | Project | Section | Domain | Key stack |
|---|---------|:-------:|--------|-----------|
| 1 | [Churn Prediction](capstone-1-churn-prediction/) | 5 | Tabular ML | scikit-learn · XGBoost · MLflow · drift (PSI) |
| 2 | [Time-Series Forecast (VN)](capstone-2-timeseries-forecast/) | 6 | Forecasting | Prophet · SARIMA · LSTM · backtesting |
| 3 | [CV — Invoice/Medical](capstone-3-cv-invoice-ocr/) | 8 | Computer Vision | PyTorch transfer learning · OCR |
| 4 | [Vietnamese Sentiment](capstone-4-vietnamese-sentiment/) | 9 | NLP (VI) | PhoBERT · underthesea · Transformers |
| 5 | [RAG Chatbot (SME docs)](capstone-5-rag-chatbot/) | 12 | RAG | sentence-transformers · Qdrant · Ollama |
| 6 | [Research Agent](capstone-6-research-agent/) | 13 | Agentic | LangGraph · tools · Ollama |
| 7 | [MLOps Platform](capstone-7-mlops-platform/) | 14 | MLOps | MLflow registry · orchestration · Grafana/Evidently |

## Shared blueprint

```
capstone-N-<slug>/
├── src/<pkg>/        # config · data · pipeline · train · predict · api/
├── tests/            # pytest — green offline (heavy paths marked integration)
├── conf/             # config.yaml consumed by typed Settings
├── monitoring/       # prometheus.yml · grafana dashboard · drift.py
├── k8s/              # deployment · service · configmap · hpa
├── infra/            # terraform skeleton
├── Dockerfile · docker-compose.yml · Makefile · pyproject.toml
└── .github/workflows/ci.yml
```

## Run any capstone

```bash
cd capstone-1-churn-prediction
make setup          # create venv + install
make train          # train, log to MLflow, save model artifact
make test           # pytest (offline-green)
make serve          # uvicorn FastAPI on :8000
make compose-up     # full stack (api + mlflow + monitoring + backing services)
```

> LLM-backed capstones (5, 6) default to a local **Ollama** endpoint; LLM calls
> are mocked in tests so the suite never hits the network.

_← [Về trang khoá học](../README.md)_
