import pandas as pd
from ...connection_cursor import conn


def positions_for_portfolio_id(pid):
    qry = """
    SELECT s.symbol FROM positions AS p JOIN symbols AS s ON
    p.symbol_id=s.id WHERE p.portfolio_id={}
    """.format(pid)
    return list(pd.read_sql(qry, conn)["symbol"])
