from .quandl_init import quandl


def download_stock(symbol, start_date=None):
    dataset = "WIKI/{}".format(symbol)
    return quandl.get(dataset, start_date=start_date)
