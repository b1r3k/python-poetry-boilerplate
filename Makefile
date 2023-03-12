APP_VERSION := $(shell grep -oP '(?<=^version = ")[^"]*' pyproject.toml)
APP_DIR := "app_name"
NPROCS = $(shell grep -c 'processor' /proc/cpuinfo)
MAKEFLAGS += -j$(NPROCS)


install:
	poetry install
	test -d .git/hooks/pre-commit || poetry run pre-commit install

test:
	poetry run pytest --failed-first -x

lint-fix:
	poetry run isort --profile black .
	poetry run black ${APP_DIR}

lint-check:
	poetry run flake8 ${APP_DIR}
	poetry run mypy .

lint: lint-fix lint-check
