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

fix_lint:
	uv run ruff check --fix brain_games

brain-even:
	uv run brain-even

.PHONY: install brain-games build package-install upgrade lint fix_lint brain-even
