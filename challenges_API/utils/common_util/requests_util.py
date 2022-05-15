import requests
import logging
import curlify


class Client:
    def get(self, url, params):
        response = requests.get(url, params)
        logging.info(curlify.to_curl(response.request))
        return response
