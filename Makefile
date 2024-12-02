all: format lint test

format: deps
	poetry run ruff check --select I --fix
	poetry run ruff format

test: deps
	poetry run pytest --cov

coverage: test
	poetry run coverage html
	open htmlcov/index.html

deps:
	poetry install --sync

update:
	scripts/poetry_update_deps.sh

lint: deps ruff pylint pyright

watch:
	poetry run pytest -f test

ruff:
	poetry run ruff check aoc

pylint:
	poetry run pylint aoc

pyright:
	poetry run pyright aoc
