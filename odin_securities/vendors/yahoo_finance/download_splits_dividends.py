import pandas as pd


def download_splits_dividends(symbol):
    """Downloads the stock split and dividend information for assets coming from
    Yahoo! Finance. Both stock splits and dividends are included in a single
    column of a dataframe that can be processed further downstream.

    Parameters
    ----------
    symbol: String.
        The string identifier for the stock whose split and dividend data should
        be retrieved.
    """
    url = "http://ichart.finance.yahoo.com/x?s={}&g=v&a=1&b=1&c=2001".format(
        symbol
    )
    # The last four rows of the returned dataframe are the start date and end
    # date of the time series, the total size (whatever that is), and the status
    # (whatever that is).
    X = pd.read_csv(url).ix[:-4]
    X.columns = ("datetime", "adjustment")
    X["datetime"] = [
        pd.to_datetime(x, format="%Y%m%d") for x in X["datetime"]
    ]
    return X
