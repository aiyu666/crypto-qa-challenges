import pytest
from utils.websocket_api.book_instrument_depth_steps import get_book_instrument_depth


@pytest.mark.parametrize(
    "instrument_name, depth",
    [
        ("ETH_USDT", 150),
        ("EOS_USDT", 10),
        ("ETH_CRO", 10),
        ("YFI_USDT", 150),
    ],
)
@pytest.mark.book_instrument_depth
def test_user_can_get_instrument_depth(instrument_name, depth):
    print(instrument_name, depth)
    get_book_instrument_depth(instrument_name, depth)
