# python-schema-validator

## Description
A small project to experiment with `pydantic` library and how it could be used to validate schema of entries in a newline-delimited json file.

### Project Structure
```bash
.
├── Dockerfile
├── main.py
├── Makefile
├── README.md
├── requirements.txt
└── schema_validator
    ├── config.yaml
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── log_model.py
    ├── schema_validator.py
    └── tests
        ├── __init__.py
        ├── test_data
        │   └── test_data.json
        └── test_schema_validator.py
```


## Usage
### Docker
Build image
```
docker build -t schema_validator:latest .
```

Run image
```
docker run -v $(pwd):/schema_validator schema_validator:latest
```

### Local
Create virtual environment and activate
```
python -m venv .venv && . .venv/bin/activate 
```

Install requirements
```
python -m pip install -r requirements.txt
```

Run the application
```
python main.py
```

### Configuration
Configuration file for the app is located under `schema_validator/config.yaml`. It contains the following options:
- `file_to_validate` - json file to validate entries in
- `log_file` - file to which logging messages will be written to
- `log_level` - log level of messages that shoud be saved to to the log_file
- `print_model_schema` - prints out schema of the model
- `print_report` - prints out the results of the file validation

## Some possible improvements
- Adding CLI argument parsing to specify source file and options such as generate report, log errors console, log errors to file, etc.
- Generalise the code a bit more so that we can pass in file and the model we want to use for the validation.
- Reporting part could really use a refactor and simplification
- Unit and end-to-end tests should be written
- requirements (app vs dev packages) could be split up into seperate files