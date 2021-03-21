import logging

import pandas  # type: ignore
import yaml

from schema_validator.models.log_model import LogModel
from schema_validator.schema_validator import schema_validator_validate_file


def main(filename: str, print_model_schema: bool = False) -> dict:
    if print_model_schema:
        model_schema = LogModel.model_schema()
        print(model_schema)

    return schema_validator_validate_file(filename)


if __name__ == "__main__":
    # TODO: would be nice to have some sort of cli args parsing,
    # this could be  for overriding defaults from config.yaml
    CONFIG_PATH = "schema_validator/config.yaml"

    with open(CONFIG_PATH) as _config:
        CONFIG = yaml.safe_load(_config)

    FILENAME = CONFIG["file_to_validate"]
    LOG_FILE = CONFIG["log_file"]
    LOG_LEVEL = CONFIG["log_level"]
    PRINT_MODEL_SCHEMA = CONFIG["print_model_schema"]
    PRINT_REPORT = CONFIG["print_report"]

    # In new version of Python we could also use the new pattern matching feature here
    LOG_LEVELS_MAPPING = {
        "ERROR": logging.ERROR,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }

    _log_level_options = LOG_LEVELS_MAPPING.keys()
    if LOG_LEVEL not in _log_level_options:
        raise ValueError(
            f"Invalid option provided for log level, possible options: {list(_log_level_options)}"
        )

    _log_level = LOG_LEVELS_MAPPING[LOG_LEVEL]

    logging.basicConfig(filename=LOG_FILE, level=logging.ERROR, filemode="w")

    report = main(FILENAME, print_model_schema=PRINT_MODEL_SCHEMA)

    if PRINT_REPORT:
        pandas_report = pandas.DataFrame.from_dict(report)
        print(pandas_report)
