import datetime as dt
from collections import Sequence
from pandas_datareader.data import DataReader
from .download_splits_dividends import download_splits_dividends


def download_stock(symbol, start_date=dt.datetime(2001, 1, 1)):
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

    # Fetch the dividends and splits for this stock. Notice that we restrict the
    # dates to lie in the appropriate range.
    ds = download_splits_dividends(symbol)

    # Store dividend data.
    if "DIVIDEND" in ds.index:
        divs = ds.ix[["DIVIDEND"]].set_index("datetime")
        idx = divs.index.intersection(stock.index)
        stock.ix[idx, "Ex-Dividend"] = [
            float(x) for x in divs.ix[idx, "adjustment"]
        ]

    # Store stock split data.
    if "SPLIT" in ds.index:
        splits = ds.ix[["SPLIT"]].set_index("datetime")
        splits["adjustment"] = [
            float(x.split(":")[0]) / float(x.split(":")[1])
            for x in splits["adjustment"]
        ]
        idx = splits.index.intersection(stock.index)
        stock.ix[idx, "Split Ratio"] = splits.ix[idx, "adjustment"]

    return stock
