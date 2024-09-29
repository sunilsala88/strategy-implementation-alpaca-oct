import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import alpaca
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.crypto import CryptoHistoricalDataClient
from alpaca.trading.stream import TradingStream
from alpaca.data.live.crypto import CryptoDataStream

from alpaca.data.requests import (
    CryptoBarsRequest,
    CryptoQuoteRequest,
    CryptoTradesRequest,
    CryptoLatestQuoteRequest
    )
from alpaca.trading.requests import (
    GetAssetsRequest,
    MarketOrderRequest,
    LimitOrderRequest,
    StopLimitOrderRequest,
    GetOrdersRequest,
    ClosePositionRequest
)
from alpaca.trading.enums import (
    AssetClass,
    AssetStatus,
    OrderSide,
    OrderType,
    TimeInForce,
    QueryOrderStatus
)
from alpaca.common.exceptions import APIError


# setup crypto historical data client


symbol="ETH/USD"
crypto_historical_data_client = CryptoHistoricalDataClient()


# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/cryptobars-1
now = datetime.now(ZoneInfo("America/New_York"))
req = CryptoBarsRequest(
    symbol_or_symbols = [symbol],
    timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Hour), # specify timeframe
    start = now - timedelta(days = 1),                          # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                        # specify end datetime, default=now
    limit = 2,                                               # specify limit
)
d=crypto_historical_data_client.get_crypto_bars(req).df
print(d)




def get_current_price_crypto(symbol):
    crypto_historical_data_client = CryptoHistoricalDataClient()
    req = CryptoLatestQuoteRequest(
        symbol_or_symbols = [symbol],
    )
    res = crypto_historical_data_client.get_crypto_latest_quote(req)
    cp=(res[symbol].ask_price+res[symbol].bid_price)/2
    print(cp)
    return cp