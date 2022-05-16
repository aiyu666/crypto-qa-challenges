import json
import logging
from websocket import create_connection
from time import sleep


class WebsocketClient:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.ws_client = create_connection(self.ws_url)
        sleep(2)

    def send_message(self, params):
        logging.info("Sending message....")
        self.ws_client.send(params)
        logging.info(f"Sent message.... params: {params}")

    def on_message(self, heartbeat: bool = False):
        logging.info("Receiving message....")
        if heartbeat:
            result = self.ws_client.recv()
            logging.info(f"Received message.... result: {result}")
            return result

        for _ in range(3):
            result = self.ws_client.recv()
            logging.info(f"Received message.... result: {result}")
            if "heartbeat" not in result:
                return result
            logging.info(f"Get the heartbeat message waiting for the next message...")
            sleep(3)
        logging.error("Timeout for receiving websocket message for three times.")
        raise

    def __delete__(self):
        self.ws_client.close()
