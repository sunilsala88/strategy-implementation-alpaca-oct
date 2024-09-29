import random
import time
import datetime
import pendulum as pdt
import pandas as pd
import pandas_ta as ta
#getting all active orders
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
import pandas as pd
api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'
trading_client = TradingClient(api_key, secret_key, paper=True)


from alpaca.data.historical import CryptoHistoricalDataClient
# setup crypto historical data client
crypto_historical_data_client = CryptoHistoricalDataClient()
from zoneinfo import ZoneInfo
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

def get_level(hist_df):
    # ct=datetime.datetime.now()
    # start_range=datetime.datetime(ct.year, ct.month, ct.day, 19, 0)
    # end_range=datetime.datetime(ct.year, ct.month, ct.day, 20, 0)
    ct = pdt.now('UTC')
    start_range=pdt.datetime(ct.year, ct.month, ct.day, 0, 0,tz='UTC')
    end_range=pdt.datetime(ct.year, ct.month, ct.day, 2, 0,tz='UTC')
    print(start_range, end_range)
    hist_df.reset_index(inplace=True)
    print(hist_df)
    # hist_df['date']=hist_df['date'].dt.tz_localize(None)
    hist_df.set_index('timestamp',inplace=True)
    print(hist_df.index)
    print(start_range, end_range)


    hist_df=hist_df[start_range:end_range]
    print(hist_df)
    high_level=hist_df.high.max()
    low_level=hist_df.low.min()
    return high_level,low_level

def get_historical_crypto_data(ticker_name,time_frame,days):

    now = datetime.datetime.now(ZoneInfo("America/New_York"))
    req = CryptoBarsRequest(
        symbol_or_symbols = ticker_name,
        timeframe=TimeFrame(amount = time_frame, unit = TimeFrameUnit.Hour), # specify timeframe
        start = now - datetime.timedelta(days = days),                          # specify start datetime, default=the beginning of the current day.
        # end_date=None,                                        # specify end datetime, default=now
        # limit = 2,                                               # specify limit
    )
    data=crypto_historical_data_client.get_crypto_bars(req).df
    # data['sma_10']=ta.sma(data['close'],10)
    # data['sma_30']=ta.sma(data['close'],30)
    return data


tickers=["BTC/USD","ETH/USD"]
hist_df=get_historical_crypto_data(tickers[0],1,5)
print(hist_df.tail(12))

h,l=get_level(hist_df)
print(h,l)