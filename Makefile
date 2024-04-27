# Ruff
.PHONY: ruff
ruff:
	poetry run ruff format . --config pyproject.toml

.PHONY: mypy
mypy:
	poetry run mypy ./ --config-file ./pyproject.toml

.PHONY: codestyle
codestyle: ruff mypy

.PHONY: test
test:
	poetry run pytest -c pyproject.toml 