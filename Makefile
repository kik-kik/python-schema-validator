PY_PATHS=main.py schema_validator
PYTESTFLAGS?=-m 'not integration'

# Test commands
test-black: # code formatter
	black $(PY_PATHS)

test-mypy:  # typing check
	mypy $(PY_PATHS)

test-unit:
	pytest -vvv \
		$(PY_PATHS) \
		$(PYTESTFLAGS)
	
test-isort:
	isort -l80 --profile=black $(PY_PATHS)
	