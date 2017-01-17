import datetime as dt
from ...connection_cursor import cur


def portfolio(portfolio, pid):
    cur.execute("""
    UPDATE portfolios SET (maximum_capacity, capital, updated) = {} WHERE id={}
    """.format(
        (portfolio.maximum_capacity, portfolio.capital,
         dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), pid)
    )
