import datetime as dt
from ...connection_cursor import cur


def portfolio(portfolio):
    cur.execute("""INSERT INTO portfolios
    (portfolio, maximum_capacity, capital, updated) VALUES {}""".format((
            portfolio.portfolio_id, portfolio.maximum_capacity,
            portfolio.capital, dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )))
