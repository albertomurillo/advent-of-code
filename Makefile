all: format test lint

format: deps
	poetry run isort .
	poetry run black .

test: deps
	poetry run pytest 2023 --cov

coverage: test
	poetry run coverage html
	open htmlcov/index.html

deps:
	poetry install --sync

lint: deps
	poetry run flake8 .
	poetry run pylint 2023
