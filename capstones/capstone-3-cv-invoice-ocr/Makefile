.PHONY: setup install lint test train serve docker-build compose-up compose-down clean

VENV ?= .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

setup: ## create venv + install base + dev deps
	python3.12 -m venv $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

install: ## install base + dev deps into the active environment
	pip install -e ".[dev]"

lint: ## ruff lint
	$(VENV)/bin/ruff check src tests monitoring

test: ## run the offline test suite
	$(PY) -m pytest -q

train: ## train classifier, log to MLflow, save artifact
	$(PY) -m vision.train

serve: ## run the API on :8000
	$(VENV)/bin/uvicorn vision.api.main:app --host 0.0.0.0 --port 8000

docker-build: ## build the container image
	docker build -t capstone-3-cv-invoice-ocr:latest .

compose-up: ## start api + mlflow + prometheus + grafana
	docker compose up -d --build

compose-down: ## stop the stack
	docker compose down -v

clean: ## remove caches + build artifacts
	rm -rf .pytest_cache .ruff_cache **/__pycache__ build dist *.egg-info
