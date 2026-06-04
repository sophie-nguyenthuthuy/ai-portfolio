"""MLOps Platform — end-to-end ML lifecycle around a reference tabular model.

This capstone is the "meta" project: it ties together orchestration (a base-deps
DAG runner with an optional Prefect flow), a model registry (a base-deps
LocalRegistry with stage transitions, plus an optional MLflow path), a FastAPI
serving layer that loads the current Production model, drift monitoring (PSI +
optional Evidently), and full platform infra (Docker, Kubernetes, Terraform, CI/CD).
"""

__version__ = "0.1.0"
