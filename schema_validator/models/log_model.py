from datetime import datetime

from pydantic.dataclasses import dataclass


true = True
false = False
null = None


@dataclass
class Log(BaseModel):
    id: str
    received_at: str  # timestamp validator?
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
    original_timestamp: str  # timestamp validator? perhaps can just use type of datetime
    sent_at: str  # timestamp validator?
    timestamp: str  # timestamp validator?
    user_id: int = None
    context_network_carrier: str
    context_device_token: str = None
    context_traits_taxfix_language: str

    @validator("received_at", "original_timestamp", "sent_at", "timestamp")
    def is_timestamp_format_valid(cls, timestamp: str) -> bool:
        try:
            datetime.datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            # raise ValueError("Incorrect data format, should be YYYY-MM-DD")  #TODO: this could be logged
            return False
        return True

# json.dumps(MainModel.schema(), indent=2)
# OR
# print(Log.schema_json(indent=2))