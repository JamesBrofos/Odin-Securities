import datetime as dt
import pandas_datareader
from pandas_datareader.data import DataReader


def check_valid_symbol(symbol):
    """We identify invalid shares if there is no official company name
    associated with the specified ticker.
    """
    for i in range(10):
        try:
            DataReader(symbol, "yahoo")
            return True
        except pandas_datareader._utils.RemoteDataError:
            print(
                "Attempt {} to validate {} from Yahoo! Finance failed.".format(
                    i, symbol
                )
            )
            continue
    else:
        return False
