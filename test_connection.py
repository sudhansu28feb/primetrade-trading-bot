from dotenv import load_dotenv
import os
from binance.client import Client

load_dotenv()

client = Client(
    api_key=os.getenv("BINANCE_API_KEY"),
    api_secret=os.getenv("BINANCE_API_SECRET"),
    testnet=True,
)

client.FUTURES_URL = "https://testnet.binancefuture.com"

balance = client.futures_account_balance()
print(balance)
