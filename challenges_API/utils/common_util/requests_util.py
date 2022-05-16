import requests
import logging
import curlify


class RestClient:
    def get(self, url, params):
        response = requests.get(url, params)
        logging.info(curlify.to_curl(response.request))
        return response
