# Binance Futures Testnet Trading Bot

## Overview

A simple Python CLI application that places MARKET and LIMIT orders on Binance USDT-M Futures Testnet with proper validation, logging, and structured code.

## Setup

### 1. Install dependencies

`pip install -r requirements.txt`

### 2. Create .env file

BINANCE_API_KEY=your_api_key

BINANCE_API_SECRET=your_api_secret

### Run Examples

#### MARKET Order

`python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002`

### LIMIT Order

`python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 84000`

### Logging

#### All API requests, responses, and errors are logged to:

logs/trading_bot.log

### Notes / Assumptions

- Binance USDT-M Futures Testnet is used.

- Minimum notional value per order is 100 USDT.

- Limit order prices must fall within Binance price protection bands.

- Order status may remain NEW due to simulated testnet liquidity.

### Project Structure

````PrimeTrade/
│
├── cli.py
├── requirements.txt
├── bot/
│ ├── client.py
│ ├── orders.py
│ └── logging_config.py
└── logs/```