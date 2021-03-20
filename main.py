import os
import pandas

from schema_validator.models.log_model import LogModel
from schema_validator.schema_validator import (
    schema_validator,
    schema_validator_validate_file,
)



def main(
    filename: str, show_model_schema: bool = False, error_log_file: str = None
) -> None:
    if show_model_schema:
        model_schema = LogModel.model_schema()
        print(model_schema)

    if error_log_file:
        if os.path.exists(error_log_file):
            raise Exception(
                "File already exists, please delete %s first to continue..."
                % error_log_file
            )

    return schema_validator_validate_file(filename, error_log=error_log_file)


if __name__ == "__main__":
    # TODO: would be nice to have some sort of cli args parsing
    FILENAME = "schema_validator/tests/test_data/test_data.json"
    ERROR_LOG_FILE = "error_log.json"
    report = main(FILENAME, show_model_schema=False, error_log_file=ERROR_LOG_FILE)


    # for r, v in report.values():
    #     print(r)
    #     print(f"{r}|{v['count of events']}")
    #     break

    pandas_report = pandas.DataFrame.from_dict(report).fillna(0)
    print(pandas_report)
