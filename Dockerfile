# syntax=docker/dockerfile:1.0.0-experimental
# DOCKER_BUILDKIT=1 docker build --ssh=default -t forex-warrior .
FROM python:3.12

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN pip3 install -U pip>=23.1.2 poetry

ADD . /app
RUN --mount=type=ssh poetry install
