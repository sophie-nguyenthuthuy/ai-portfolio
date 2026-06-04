.PHONY: setup install lint test pipeline registry-list train serve predict drift docker-build compose-up compose-down clean

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

pipeline: ## run the full ingest->...->deploy-check flow (base DAG runner)
	$(PY) -m mlops.pipeline run

registry-list: ## list registered model versions
	$(PY) -m mlops.registry list

train: ## one-shot train + register + promote to Production
	$(PY) -m mlops.train --promote

serve: ## run the FastAPI service on :8000
	$(PY) -m mlops.serve

predict: ## score a demo record with the Production model
	$(PY) -m mlops.predict

drift: ## run the PSI/Evidently drift demo
	$(PY) monitoring/drift.py

docker-build: ## build the container image
	docker build -t capstone-mlops:latest .

compose-up: ## start api + mlflow + postgres + prometheus + grafana
	docker compose up -d --build

compose-down: ## stop the stack
	docker compose down -v

clean: ## remove caches, venv, artifacts
	rm -rf $(VENV) .pytest_cache .ruff_cache **/__pycache__ mlruns
	find registry -mindepth 1 ! -name .gitkeep -exec rm -rf {} +
	find models -mindepth 1 ! -name .gitkeep -delete
