install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

upgrade: build package-install

lint:
	uv run ruff check brain_games

fix_lint:
	uv run ruff check --fix brain_games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

.PHONY: brain-progression brain-gcd install brain-games build package-install upgrade lint fix_lint brain-even brain-calc
