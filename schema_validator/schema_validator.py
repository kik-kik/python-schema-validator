import json
import logging
from collections import defaultdict

from pydantic import ValidationError

from schema_validator.models.log_model import LogModel


def schema_validator(line: str) -> dict:
    line_dict: dict = json.loads(line)

    success: bool = True

    try:
        LogModel(**line_dict)
    except ValidationError:
        logging.error(line.rstrip("\n"))
        success = False

    logging.info(line.rstrip("\n"))

    return {
        "date": line_dict["timestamp"].split(" ")[0].split("T")[0],
        "event": line_dict["event"],
        "success": success,
    }


def schema_validator_validate_file(filename: str) -> dict:
    report = dict()  # type: ignore

    with open(filename) as stream:
        for line in stream:
            result: dict = schema_validator(line)

            try:
                report[result["date"]]
            except KeyError:
                report[result["date"]] = dict()

            try:
                report[result["date"]]["events"]
            except KeyError:
                report[result["date"]]["events"] = list()

            try:
                report[result["date"]]["success"]
            except KeyError:
                report[result["date"]]["success"] = 0

            try:
                report[result["date"]]["fail"]
            except KeyError:
                report[result["date"]]["fail"] = 0

            report[result["date"]]["events"].append(result["event"])

            if result["success"]:
                report[result["date"]]["success"] += 1
            else:
                report[result["date"]]["fail"] += 1

    report_keys = report.keys()

    for key in report_keys:
        event_metrics = defaultdict(int)

        for event in report[key]["events"]:
            event_metrics[event] = report[key]["events"].count(event)

        try:
            report[key]["event_metrics"]
        except KeyError:
            report[key]["event_metrics"] = dict

        report[key]["event_metrics"] = event_metrics

    for key in report_keys:
        report[key]["events"] = list(set(report[key]["events"]))
        report[key]["unique_events"] = report[key].pop("events")

    return report
