.PHONY: setup install lint test run serve drift docker-build compose-up compose-down clean

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

run: ## ask the agent a demo question (offline FakeLLM)
	$(PY) -m agent.predict -q "What is retrieval augmented generation and why cite sources?"

serve: ## run the FastAPI service on :8000
	$(VENV)/bin/uvicorn agent.api.main:app --host 0.0.0.0 --port 8000

drift: ## run the behavioral-drift (PSI) demo
	$(PY) monitoring/drift.py

docker-build: ## build the container image
	docker build -t capstone-research-agent:latest .

compose-up: ## start api + ollama + prometheus + grafana
	docker compose up -d --build

compose-down: ## stop the stack
	docker compose down -v

clean: ## remove caches + venv
	rm -rf $(VENV) .pytest_cache .ruff_cache **/__pycache__ mlruns
