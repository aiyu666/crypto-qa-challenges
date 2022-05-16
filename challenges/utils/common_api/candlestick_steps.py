from utils.common_api.candlestick_util import Candlestick
from utils.common_util.jsonschema_util import validate_json_schema
import logging
from datetime import datetime
from datetime import timezone


def user_can_get_candlestick_successfully(instrument_name: str, timeframe: str):
    candlestick = Candlestick()
    response = candlestick.get_candlestick(instrument_name, timeframe)
    assert response.status_code == 200
    response_data = response.json()
    validate_json_schema(response_data, "candlestick", "get_candlestick_successfully")
    return response_data


def user_can_not_get_candlestick_successfully(instrument_name: str, timeframe: str, schema: str, status_code: int = 200):
    candlestick = Candlestick()
    response = candlestick.get_candlestick(instrument_name, timeframe)
    assert response.status_code == status_code
    response_data = response.json()
    validate_json_schema(response_data, "candlestick", schema)
    return response_data


def verify_candlestick_data_is_correct(data: dict, instrument_name: str, timeframe: str, depth: int = 1000):
    assert data["code"] == 0
    assert data["method"] == "public/get-candlestick"
    assert data["result"]["instrument_name"] == instrument_name
    assert data["result"]["depth"] == depth
    assert data["result"]["interval"] == timeframe
    assert len(data["result"]["data"]) > 1


def verify_candlestick_data_is_correct_when_timeframe_is_wrong(data: dict, timeframe: str):
    assert data["code"] == 10004
    assert data["message"] == f"Timeframe {timeframe} is not supported."


def verify_candlestick_data_is_correct_when_instrument_name_is_wrong(data: dict):
    assert data["code"] == 10004
    assert data["result"] == ""
    assert data["message"] == "Invalid input"


def verify_candlestick_data_is_correct_when_params_without_required_parameter(data: dict):
    current_timestamp = datetime.now(timezone.utc)
    paste_two_min_unix_timestamp = current_timestamp.timestamp() - 120
    current_timestamp = current_timestamp.timestamp() + 10
    response_timestamp = datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z").timestamp()
    assert response_timestamp > paste_two_min_unix_timestamp
    assert current_timestamp > response_timestamp
    assert data["path"] == "/v2/public/get-candlestick"
    assert data["status"] == 400
    assert data["error"] == "Bad Request"
    assert type(data["requestId"]) == str
