set dotenv-load

default:
    @just --list

_compose args:
    podman compose -f .devcontainer/compose.yaml {{ args }}

up *args:
    @just _compose up {{ args }}

down *args:
    @just _compose down {{ args }}

restart *args:
    @just _compose restart {{ args }}

logs *args:
    @just _compose logs -f {{ args }}

build *args:
    @just _compose build --no-cache {{ args }}

ps:
    @just _compose ps

shell-backend:
    @just _compose exec backend bash

makemigrations *args:
    @just _compose exec backend uv run python manage.py makemigrations {{ args }}

migrate *args:
    @just _compose exec backend uv run python manage.py migrate {{ args }}

showmigrations:
    @just _compose exec backend uv run python manage.py showmigrations

lint-backend:
    @just _compose exec backend uv run ruff check .

format-backend:
    @just _compose exec backend uv run ruff format .

fix-backend:
    @just _compose exec backend uv run ruff check --fix .
    @just _compose exec backend uv run ruff format .

shell-worker:
    podman compose exec worker bash
