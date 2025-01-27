install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

upgrade: build
	uv tool upgrade hexlet-code

lint:
	uv run ruff check brain_games

.PHONY: install brain-games build package-install upgrade lint