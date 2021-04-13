import pytest

from schema_validator import schema_validator


true = True
false = False
null = None

schema_validator_fixture = (
    (
        '{"id": "AED96FC7-19F1-46AB-B79F-D412117119BD",  "received_at": "2018-02-03 18:28:12.378000",  "anonymous_id": "8E0302A3-2184-4592-851D-B93C32E410AB", "context_device_manufacturer": "Apple", "context_device_model": "iPhone8,4", "context_device_type": "ios",  "context_library_name": "analytics-ios","context_library_version":"3.6.7", "context_locale": "de-DE",  "context_network_wifi": true,  "context_os_name": "iOS",  "event":"registration_initiated", "event_text": "registrationInitiated", "original_timestamp": "2018-02-03T19:28:06.291+0100",  "sent_at":"2018-02-03 18:28:12.000000", "timestamp": "2018-02-03 18:28:06.561000", "context_network_carrier": "o2-de",   "context_traits_taxfix_language": "de-DE"}',
        {
            "date": "2018-02-03",
            "event": "registration_initiated",
            "success": False,
        },
    ),
    (
        '{"id": "AED96FC7-19F1-46AB-B79F-D412117119BD",  "received_at": "2018-02-03 18:28:12.378000",  "anonymous_id": "8E0302A3-2184-4592-851D-B93C32E410AB", "context_device_manufacturer": "Apple", "context_device_model": "iPhone8,4", "context_device_type": "ios",  "context_library_name": "analytics-ios","context_library_version":"3.6.7", "context_locale": "de-DE",  "context_network_wifi": true,  "context_os_name": "iOS",  "event":"registration_initiated", "event_text": "registrationInitiated", "original_timestamp": "2018-02-03T19:28:06.291+0100",  "sent_at":"2018-02-03 18:28:12.000000", "timestamp": "2018-02-03 18:28:06.561000", "context_network_carrier": "o2-de",   "context_traits_taxfix_language": "de-DE"}',
        {
            "date": "2018-02-03",
            "event": "registration_initiated",
            "success": False,
        },
    ),
    (
        '{"id": "AED96FC7-19F1-46AB-B79F-D412117119BD",  "received_at": "2018-02-03 18:28:12.378000",  "anonymous_id": "8E0302A3-2184-4592-851D-B93C32E410AB", "context_device_manufacturer": "Apple", "context_device_model": "iPhone8,4", "context_device_type": "ios",  "context_library_name": "analytics-ios","context_library_version":"3.6.7", "context_locale": "de-DE",  "context_network_wifi": true,  "context_os_name": "iOS",  "event":"registration_initiated", "event_text": "registrationInitiated", "original_timestamp": "2018-02-03T19:28:06.291+0100",  "sent_at":"2018-02-03 18:28:12.000000", "timestamp": "2018-02-03 18:28:06.561000", "context_network_carrier": "o2-de",   "context_traits_taxfix_language": "de-DE"}',
        {
            "date": "2018-02-03",
            "event": "registration_initiated",
            "success": False,
        },
    ),
    (
        '{"id": "AED96FC7-19F1-46AB-B79F-D412117119BD",  "received_at": "2018-02-03 18:28:12.378000",  "anonymous_id": "8E0302A3-2184-4592-851D-B93C32E410AB", "context_device_manufacturer": "Apple", "context_device_model": "iPhone8,4", "context_device_type": "ios",  "context_library_name": "analytics-ios","context_library_version":"3.6.7", "context_locale": "de-DE",  "context_network_wifi": true,  "context_os_name": "iOS",  "event":"registration_initiated", "event_text": "registrationInitiated", "original_timestamp": "2018-02-03T19:28:06.291+0100",  "sent_at":"2018-02-03 18:28:12.000000", "timestamp": "2018-02-03 18:28:06.561000", "context_network_carrier": "o2-de",   "context_traits_taxfix_language": "de-DE"}',
        {
            "date": "2018-02-03",
            "event": "registration_initiated",
            "success": False,
        },
    ),
    (
        '{"id": "AED96FC7-19F1-46AB-B79F-D412117119BD",  "received_at": "2018-02-03 18:28:12.378000",  "anonymous_id": "8E0302A3-2184-4592-851D-B93C32E410AB", "context_device_manufacturer": "Apple", "context_device_model": "iPhone8,4", "context_device_type": "ios",  "context_library_name": "analytics-ios","context_library_version":"3.6.7", "context_locale": "de-DE",  "context_network_wifi": true,  "context_os_name": "iOS",  "event":"registration_initiated", "event_text": "registrationInitiated", "original_timestamp": "2018-02-03T19:28:06.291+0100",  "sent_at":"2018-02-03 18:28:12.000000", "timestamp": "2018-02-03 18:28:06.561000", "context_network_carrier": "o2-de",   "context_traits_taxfix_language": "de-DE"}',
        {
            "date": "2018-02-03",
            "event": "registration_initiated",
            "success": False,
        },
    ),
)


@pytest.mark.parametrize("test_input,expected", schema_validator_fixture)
def test_schema_validator(test_input, expected):
    assert schema_validator.schema_validator(test_input) == expected
