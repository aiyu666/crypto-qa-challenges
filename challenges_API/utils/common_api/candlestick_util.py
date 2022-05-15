from email.policy import default
from attr import attrs, attrib
import os
from dotenv import load_dotenv
import logging
from utils.common_util.requests_util import Client

load_dotenv()


@attrs
class Candlestick(object):
    client = Client()
    host = attrib(type=str, default=os.getenv("HOST"))
    uri = attrib(type=str, default="/public/get-candlestick")

    def get_candlestick(self,instrument_name:str, timeframe:str):
        url = f"{self.host}{self.uri}"
        params = {"instrument_name": instrument_name, "timeframe": timeframe}
        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get(url, params)
        return response
