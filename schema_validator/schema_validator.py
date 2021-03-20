import json
import logging
from collections import defaultdict
from datetime import datetime, timezone, tzinfo

from pydantic import ValidationError

from schema_validator.models.log_model import LogModel


def schema_validator(line: str, error_log: str = None) -> dict:
    line_dict: dict = json.loads(line)

    success: bool = True

    try:
        LogModel(**line_dict)
    except ValidationError as e:
        if error_log:
            with open(error_log, "a+") as _error_log:
                _error_log.write(line)

        logging.error(line)
        success = False

    logging.info(line)

    return {
        "date": line_dict["timestamp"].split(" ")[0].split("T")[0],
        "event": line_dict["event"],
        "success": success,
    }


def schema_validator_validate_file(
    filename: str, error_log: str = None
) -> dict:
    # metrics: dict = defaultdict(lambda: defaultdict(int))
    # events: dict = defaultdict(lambda: defaultdict(list))

    report = dict()

    with open(filename) as stream:
        for line in stream:
            result: dict = schema_validator(line, error_log=error_log)

            try:
                report[result['date']]
            except KeyError:
                report[result['date']] = dict()

            try:
                report[result['date']]['events']
            except KeyError:
                report[result['date']]['events'] = list()

            try:
                report[result['date']]['success']
            except KeyError:
                report[result['date']]['success'] = 0

            try:
                report[result['date']]['fail']
            except KeyError:
                report[result['date']]['fail'] = 0
            
            report[result['date']]['events'].append(result['event'])

            if result['success']:
                report[result['date']]['success'] += 1
            else:
                report[result['date']]['fail'] += 1


    for date in report.keys():
        event_metrics = defaultdict(int)

        for event in report[date]["events"]:
            event_metrics[event] = report[date]["events"].count(event)
        
        try:
            report[date]['event_metrics']
        except KeyError:
            report[date]['event_metrics'] = dict
        
        report[date]['event_metrics'] = event_metrics

        # report[result['date']]['events'] = list(set(report[result['date']]['events']))

    return report
