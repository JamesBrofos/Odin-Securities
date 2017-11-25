import datetime as dt
from collections import Sequence
from pandas_datareader.data import DataReader
from .download_splits_dividends import download_splits_dividends


def download_stock(symbol, start_date=dt.datetime(1990, 1, 1)):
    # Because Yahoo! Finance has recently took down their API, I will instead
    # try to download the stock ten times before giving up.
    for i in range(10):
        try:
            return __download_stock(symbol, start_date)
        except:
            print(
                "Attempt {} to download {} from Yahoo! Finance failed.".format(
                    i, symbol
                )
            )
            continue
    else:
        raise ValueError(
            "Could not download {} from Yahoo! Finance despite it being a valid"
            "ticker.".format(symbol)
        )

def __download_stock(symbol, start_date):
    # Download assets.
    stock = DataReader(symbol, "yahoo", start_date)
    stock.rename(columns={"Adj Close": "Adj. Close"}, inplace=True)
    # Compute the adjusted prices.
    ratio = stock["Adj. Close"] / stock["Close"]
    stock["Adj. Open"] = stock["Open"] * ratio
    stock["Adj. High"] = stock["High"] * ratio
    stock["Adj. Low"] = stock["Low"] * ratio
    stock["Adj. Volume"] = stock["Volume"] * ratio
    stock["Split Ratio"] = 1.0
    stock["Ex-Dividend"] = 0.0
    return stock
