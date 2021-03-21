PY_PATHS=main.py schema_validator
PYTESTFLAGS?=-m 'not integration'
YAML_CONFIGS=schema_validator/config.yaml

default:
	make help

format-all:
	$(MAKE) -j4 \
		run-black \
		run-isort

run-black:
	black -l 80 $(PY_PATHS)

run-isort:
	isort -l80 --profile=black $(PY_PATHS)


test-all:
	$(MAKE) -j4 \
		test-black \
		test-mypy \
		test-unit \
		test-isort \
		test-yaml \

# Test commands
test-black: # code formatter
	black -l 80 --check $(PY_PATHS)

test-mypy:  # typing check
	mypy $(PY_PATHS)

test-unit:
	pytest -vvv \
		$(PY_PATHS) \
		$(PYTESTFLAGS)

test-isort:
	isort -l80 --profile=black -c $(PY_PATHS)

test-yaml:
	yamllint $(YAML_CONFIGS)\

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
