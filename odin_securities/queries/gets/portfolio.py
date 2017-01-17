import pandas as pd
from ...connection_cursor import conn


def portfolio(portfolio):
    qry = "SELECT * FROM portfolios WHERE portfolio='{}'".format(portfolio)
    return pd.read_sql(qry, conn, index_col=["id"]).iloc[0]
