from utils.websocket_api.book_instrument_depth_util import BookInstrumentDepth


def get_book_instrument_depth(instrument_name: str, depth: int):
    book_instrument_depth = BookInstrumentDepth()
    result = book_instrument_depth.subscribe_book_instrument_depth(instrument_name, depth)
    assert result["code"] == 0
    assert result["method"] == "subscribe"
    assert result["result"]["instrument_name"] == instrument_name
    assert result["result"]["subscription"] == f"book.{instrument_name}.{depth}"
    assert result["result"]["channel"] == "book"
    assert result["result"]["depth"] == depth
    assert len(result["result"]["data"]) > 0
