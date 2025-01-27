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

.PHONY: install brain-games build package-install upgrade