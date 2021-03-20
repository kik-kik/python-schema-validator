from datetime import datetime

from pydantic import BaseModel, json, validator


class LogModel(BaseModel):
    id: str
    received_at: str
    anonymous_id: str
    context_app_version: str
    context_device_ad_tracking_enabled: bool
    context_device_manufacturer: str
    context_device_model: str
    context_device_type: str
    context_library_name: str = None
    context_library_version: str = None
    context_locale: str
    context_network_wifi: bool
    context_os_name: str
    context_timezone: str = None
    event: str
    event_text: str
    original_timestamp: str
    sent_at: str
    timestamp: str
    user_id: int = None
    context_network_carrier: str
    context_device_token: str = None
    context_traits_taxfix_language: str

    @validator("received_at", "original_timestamp", "sent_at", "timestamp")
    def is_timestamp_format_valid(cls, timestamp: str) -> bool:
        timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
        if "+" in timestamp:
            timestamp_format = "%Y-%m-%dT%H:%M:%S.%f%z"

        try:
            datetime.strptime(timestamp, timestamp_format)
        except ValueError:
            logging.debug(e.json())
            # raise ValueError(f"Incorrect data format, should be '{timestamp_format}'")  # perhaps this should be logged rather than raise exception
        return timestamp

    @staticmethod
    def model_schema():
        return json.dumps(LogModel.schema(), indent=4)
