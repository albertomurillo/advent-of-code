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

lint: deps
	poetry run ruff check aoc
	poetry run pylint aoc
	poetry run pyright aoc
