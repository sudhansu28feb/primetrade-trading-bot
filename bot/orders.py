from bot.logging_config import setup_logger

logger = setup_logger()


def place_order(client, symbol, side, order_type, quantity, price=None):

    try:
        logger.info(
            f"ORDER REQUEST | "
            f"symbol={symbol} side={side} type={order_type} "
            f"qty={quantity} price={price}"
        )

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol, side=side, type="MARKET", quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

        logger.info(f"ORDER RESPONSE | {order}")
        return order

    except Exception as e:
        logger.exception("ORDER FAILED")
        raise
