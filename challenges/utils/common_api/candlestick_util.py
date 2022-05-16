from attr import attrs, attrib
import os
from dotenv import load_dotenv
from utils.common_util.requests_util import RestClient

load_dotenv()


@attrs
class Candlestick(object):
    client = RestClient()
    host = attrib(type=str, default=os.getenv("REST_API_HOST"))
    uri = attrib(type=str, default="/public/get-candlestick")

    def get_candlestick(self, instrument_name: str, timeframe: str):
        url = f"{self.host}{self.uri}"
        params = {"instrument_name": instrument_name, "timeframe": timeframe}
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get(url, params)
        return response
