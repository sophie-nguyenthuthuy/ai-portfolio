.PHONY: setup install lint test train predict serve drift docker-build compose-up compose-down clean

VENV ?= .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

setup: ## create venv + install base + dev deps
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

install: ## install base + dev deps into the active environment
	pip install -e ".[dev]"

lint: ## ruff lint
	$(VENV)/bin/ruff check src tests monitoring

test: ## run pytest (offline-green; integration skipped)
	$(PY) -m pytest -q

train: ## train + log to MLflow + save artifact
	$(PY) -m churn.train

predict: ## score a demo record
	$(PY) -m churn.predict

serve: ## run the FastAPI service on :8000
	$(VENV)/bin/uvicorn churn.api.main:app --host 0.0.0.0 --port 8000

drift: ## run the PSI drift demo
	$(PY) monitoring/drift.py

docker-build: ## build the container image
	docker build -t capstone-churn:latest .

compose-up: ## start api + mlflow + prometheus + grafana
	docker compose up -d --build

compose-down: ## stop the stack
	docker compose down -v

clean: ## remove caches, venv, artifacts
	rm -rf $(VENV) .pytest_cache **/__pycache__ models/*.joblib models/*.json mlruns
