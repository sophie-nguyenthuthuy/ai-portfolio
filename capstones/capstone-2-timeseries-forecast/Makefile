.DEFAULT_GOAL := help
VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PKG := forecast
IMAGE := capstone-2-timeseries-forecast:latest

.PHONY: help setup install lint test train predict drift serve docker-build compose-up compose-down clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

setup: ## Create venv + install base + dev deps
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

install: ## Install base deps into the active environment
	pip install -e .

lint: ## Ruff lint
	$(VENV)/bin/ruff check src tests monitoring

test: ## Run pytest (offline, baseline model)
	$(PY) -m pytest -q

train: ## Train + log to MLflow + save artifact
	$(PY) -m $(PKG).train

predict: ## Forecast the configured horizon and print JSON
	$(PY) -m $(PKG).predict

drift: ## Run the drift check on the configured series
	$(PY) monitoring/drift.py

serve: ## Run the API locally on :8000
	$(VENV)/bin/uvicorn $(PKG).api.main:app --host 0.0.0.0 --port 8000 --reload

docker-build: ## Build the container image
	docker build -t $(IMAGE) .

compose-up: ## Start api + mlflow + prometheus + grafana
	docker compose up -d --build

compose-down: ## Stop the stack
	docker compose down

clean: ## Remove caches and build artifacts
	rm -rf .pytest_cache .ruff_cache build dist *.egg-info src/*.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
