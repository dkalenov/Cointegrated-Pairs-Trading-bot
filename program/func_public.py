from constants import RESOLUTION
from func_utils import get_ISO_times
import pandas as pd
import numpy as np
import time

from pprint import pprint


# Get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_times()

pprint(ISO_TIMES)


# Construct market prices
def construct_market_prices(client):
  pass

  # # Declare variables
  # tradeable_markets = []
  # markets = client.public.get_markets()
  #
  # # Find tradeable pairs
  # for market in markets.data["markets"].keys():
  #   market_info = markets.data["markets"][market]
  #   if market_info["status"] == "ONLINE" and market_info["type"] == "PERPETUAL":
  #     tradeable_markets.append(market)
  #
  # # Set initial DateFrame
  # close_prices = get_candles_historical(client, tradeable_markets[0])
  # df = pd.DataFrame(close_prices)
  # df.set_index("datetime", inplace=True)