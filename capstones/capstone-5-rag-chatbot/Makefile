.PHONY: setup install lint test ingest eval serve drift docker-build compose-up compose-down clean

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

ingest: ## ingest the sample corpus and ask a demo question
	$(PY) -m ragbot.pipeline

eval: ## run the offline RAGAS-style evaluation
	$(PY) -m ragbot.eval

serve: ## run the FastAPI service on :8000
	$(VENV)/bin/uvicorn ragbot.api.main:app --host 0.0.0.0 --port 8000

drift: ## run the PSI query-drift demo
	$(PY) monitoring/drift.py

docker-build: ## build the container image
	docker build -t capstone-rag:latest .

compose-up: ## start api + qdrant + ollama + prometheus + grafana
	docker compose up -d --build

compose-down: ## stop the stack
	docker compose down -v

clean: ## remove caches, venv, artifacts
	rm -rf $(VENV) .pytest_cache .ruff_cache **/__pycache__ src/*.egg-info
