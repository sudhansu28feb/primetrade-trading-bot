import os
from binance.client import Client


class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True,
        )

        # Futures Testnet base URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def futures(self):
        return self.client
