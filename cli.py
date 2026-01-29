import argparse
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_order

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

    client = BinanceClient().futures()

    order = place_order(
        client, args.symbol, args.side, args.type, args.quantity, args.price
    )

    print("\n========== ORDER RESULT ==========")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice"))
    print("==================================\n")


if __name__ == "__main__":
    main()
