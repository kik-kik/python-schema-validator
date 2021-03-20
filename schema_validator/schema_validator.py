import json
import logging
from collections import defaultdict
from datetime import datetime, timezone, tzinfo

from pydantic import ValidationError

from schema_validator.models.log_model import LogModel


def schema_validator(line: str, error_log: str = None):
    line_dict = json.loads(line)

    status = "SUCCESS"

    try:
        LogModel(**line_dict)
    except ValidationError as e:
        if error_log:
            with open(error_log, "a+") as _error_log:
                _error_log.write(f"{line}\\n")

        logging.error(line)
        status = "FAIL"

    logging.info(line)

    return {
        "date": line_dict["timestamp"].split(" ")[0].split("T")[0],
        "event": line_dict["event"],
        "status": status,
    }


def schema_validator_validate_file(filename: str, error_log: str = None):
    report = defaultdict(lambda: defaultdict(int))

    fails = 0
    success = 0

    with open(filename) as stream:
        for line in stream:
            result = schema_validator(line, error_log=error_log)

            report[result["date"]]["name of event"] = result["event"]
            report[result["date"]]["count of events"] += 1

            if result["status"] == "FAIL":
                fails += 1
            elif result["status"] == "SUCCESS":
                success += 1

    report[result["date"]]["FAIL"] = fails
    report[result["date"]]["SUCCESS"] = success

    return report
