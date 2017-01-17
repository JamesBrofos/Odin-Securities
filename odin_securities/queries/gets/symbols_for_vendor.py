import pandas as pd
from ...connection_cursor import conn


def symbols_for_vendor(vid):
    return pd.read_sql("""
    SELECT * FROM symbols AS s JOIN symbol_vendor AS sv ON s.id=sv.symbol_id
    WHERE sv.vendor_id={}""".format(vid), conn, index_col="symbol")
