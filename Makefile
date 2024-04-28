## Studying FastAPI by wrighting tests with pytest to original documentation examples

help:		## Show this help.
	egrep -h '(\s##\s|^##\s)' $(MAKEFILE_LIST) | egrep -v '^--' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m  %-35s\033[0m %s\n", $$1, $$2}'


.PHONY: ruff 
ruff:		## Ruff formatting
	poetry run ruff format . --config pyproject.toml


.PHONY: mypy
mypy:		## Linting
	poetry run mypy ./ --config-file ./pyproject.toml


.PHONY: codestyle
codestyle:ruff mypy		## Formatting and linting
			


.PHONY: test
test:		## Testing
	poetry run pytest -c pyproject.toml 