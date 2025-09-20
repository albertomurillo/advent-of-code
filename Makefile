all: format lint test

format: deps
	uv run ruff check --select I --fix
	uv run ruff format

test: deps
	uv run pytest --cov

coverage: test
	uv run coverage html
	open htmlcov/index.html

deps:
	uv sync

update:
	./scripts/uv_bump.py

lint: deps ruff pylint pyright

watch:
	uv run pytest -f

ruff:
	uv run ruff check

pylint:
	uv run pylint src

pyright:
	uv run pyright src
