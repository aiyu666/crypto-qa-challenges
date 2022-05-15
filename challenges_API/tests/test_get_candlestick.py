import pytest
from utils.common_api.candlestick_steps import (
    user_can_get_candlestick_successfully,
    user_can_not_get_candlestick_successfully,
    verify_candlestick_data_is_correct,
    verify_candlestick_data_is_correct_when_timeframe_is_wrong,
    verify_candlestick_data_is_correct_when_instrument_name_is_wrong,
    verify_candlestick_data_is_correct_when_params_without_required_parameter
)


@pytest.mark.parametrize(
    "instrument_name, timeframe",
    [
        ("BTC_USDT", "1m"), ("ETH_USDT", "5m"), ("YFI_USDT", "15m"),
        ("BTC_USDT", "30m"), ("ETH_USDT", "1h"), ("YFI_USDT", "4h"),
        ("BTC_USDT", "6h"), ("ETH_USDT", "12h"), ("YFI_USDT", "1D"),
        ("BTC_USDT", "7D"), ("ETH_USDT", "14D"), ("YFI_USDT", "1M")
    ],
)
@pytest.mark.candlestick
def test_user_can_get_candlestick(instrument_name, timeframe):
    response = user_can_get_candlestick_successfully(instrument_name, timeframe)
    verify_candlestick_data_is_correct(response, instrument_name, timeframe)


@pytest.mark.parametrize(
    "instrument_name, timeframe",
    [
        ("BTC_USDT", "0m"), ("ETH_USDT", "-1m",), ("YFI_USDT", "!"),
        ("BTC_USDT", "99999999"), ("ETH_USDT", "15D",), ("YFI_USDT", "$!!@$@#%$"),
        ("BTC_USDT", "-100M"), ("ETH_USDT", "-15D",), ("YFI_USDT", "."),
    ],
)
@pytest.mark.candlestick
def test_user_can_not_get_candlestick_with_wrong_timeframe(instrument_name, timeframe):
    response = user_can_not_get_candlestick_successfully(instrument_name, timeframe, "get_candlestick_failed_with_wrong_timeframe")
    verify_candlestick_data_is_correct_when_timeframe_is_wrong(response, timeframe)

@pytest.mark.parametrize(
    "instrument_name, timeframe",
    [
        ("~", "1m"), ("&", "5m"), ("*", "15m"),
        ("@!#", "30m"), ("^", "1h"), ("!.", "4h"),
    ],
)
@pytest.mark.candlestick
def test_user_can_not_get_candlestick_with_invalid_instrument_name(instrument_name, timeframe):
    response = user_can_not_get_candlestick_successfully(instrument_name, timeframe, "get_candlestick_failed_with_wrong_instrument_name")
    verify_candlestick_data_is_correct_when_instrument_name_is_wrong(response)

@pytest.mark.parametrize(
    "instrument_name, timeframe",
    [
        (None, "1m"), (None, "-5m"), (None, "!"),
        ("TEST_TEST", None), ("^", None), ("USDT", None),
    ],
)
@pytest.mark.candlestick
def test_user_can_not_get_candlestick_without_required_parameter(instrument_name, timeframe):
    response = user_can_not_get_candlestick_successfully(instrument_name, timeframe, "get_candlestick_failed_without_required_parameter", 400)
    verify_candlestick_data_is_correct_when_params_without_required_parameter(response)
