.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

PROJECT_NAME = ds_utility
PYTHON_INTERPRETER = python3

.PHONY: install
## Install this repo in develop mode
install:
	pip install -r requirements/prod.txt -r requirements/ci.txt
	pip install -e .
	pre-commit install

.PHONY: clean
## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: lint
## Lint using flake8
lint:
	pre-commit run --all-files

.PHONY: test
## Run pytest
test:
	pre-commit run --all-files
	python -m pytest
