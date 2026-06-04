.DEFAULT_GOAL := help
PY ?= python3
VENV := .venv
BIN := $(VENV)/bin
PKG := nlpvi
IMAGE := capstone-4-vietnamese-sentiment

.PHONY: help setup install lint test train serve docker-build compose-up compose-down clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

setup: ## Create venv + install base + dev deps
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"

install: ## Install base deps only (offline test surface)
	$(BIN)/pip install -e .

lint: ## Ruff lint
	$(BIN)/ruff check src tests monitoring

test: ## Run pytest (offline-green)
	PYTHONPATH=src $(BIN)/pytest -q

train: ## Train model + log to MLflow, write artifact under models/
	PYTHONPATH=src $(BIN)/python -m $(PKG).train

serve: ## Run the API on :8000
	PYTHONPATH=src $(BIN)/uvicorn $(PKG).api.main:app --host 0.0.0.0 --port 8000

docker-build: ## Build the API image
	docker build -t $(IMAGE):latest .

compose-up: ## Start api + mlflow + prometheus + grafana
	docker compose up -d --build

compose-down: ## Stop the stack
	docker compose down -v

clean: ## Remove caches, models, mlruns
	rm -rf .pytest_cache **/__pycache__ models/*.joblib models/*.json mlruns
