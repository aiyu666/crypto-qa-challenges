import os
import json
import logging
from utils.common_util.websocket_util import WebsocketClient
from dotenv import load_dotenv

load_dotenv()


class BookInstrumentDepth:
    def __init__(self):
        host = os.getenv("WEBSOCKET_API_HOST")
        market_url = f"{host}/market"
        self.ws_url = market_url
        self.ws_client = WebsocketClient(market_url)

        def __delete__(self):
            self.ws_client.close()

    def subscribe_book_instrument_depth(self, instrument_name: str, depth: int):
        params = {
            "method": "subscribe",
            "params": {"channels": [f"book.{instrument_name}.{depth}"]},
        }
        self.ws_client.send_message(json.dumps(params))
        subscribe_result = self.ws_client.on_message()
        subscribe_response = json.loads(subscribe_result)
        assert subscribe_response["method"] == "subscribe"
        assert subscribe_response["id"] == 0
        assert subscribe_response["code"] == 0
        book_instrument_depth_result = self.ws_client.on_message()
        logging.info(f"book_instrument_depth_result: {book_instrument_depth_result}")
        return json.loads(book_instrument_depth_result)
