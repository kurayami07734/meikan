PYTHON := uv

.PHONY: run test lint format check

run:
	$(PYTHON) run uvicorn app.main:app --reload

test:
	$(PYTHON) run pytest

lint:
	$(PYTHON) run ruff check .

format:
	$(PYTHON) run ruff format .

check: lint test
