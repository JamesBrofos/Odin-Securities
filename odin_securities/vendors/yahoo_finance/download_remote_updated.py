from pandas_datareader.data import DataReader
from ...queries import gets
from .download_stock import download_stock


def download_remote_updated(symbol):
    sid = gets.id_for_symbol(symbol)
    vid = gets.id_for_vendor("Yahoo! Finance")
    try:
        update_local_date = gets.updated_for_symbol_vendor(sid, vid)
        stock = DataReader(symbol, "yahoo", update_local_date)
    except TypeError:
        stock = DataReader(symbol, "yahoo")

    return stock.index[-1].to_pydatetime()
