APP_VERSION := $(shell grep -oP '(?<=^version = ")[^"]*' pyproject.toml)
APP_DIR := "app_name"
NPROCS = $(shell grep -c 'processor' /proc/cpuinfo)
MAKEFLAGS += -j$(NPROCS)
PYTEST_FLAGS := --failed-first -x


install:
	poetry install
	test -d .git/hooks/pre-commit || poetry run pre-commit install

test:
	poetry run pytest ${PYTEST_FLAGS}

testloop:
	watch -n 3 poetry run pytest ${PYTEST_FLAGS}

lint-fix:
	poetry run isort --profile black .
	poetry run black ${APP_DIR}

lint-check:
	poetry run flake8 ${APP_DIR}
	poetry run mypy .

lint: lint-fix lint-check
