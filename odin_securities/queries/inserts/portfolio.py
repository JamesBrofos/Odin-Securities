import datetime as dt
from ...connection_cursor import cur
from ...io_params import IOFiles


def portfolio(portfolio, fid):
    cur.execute("""INSERT INTO portfolios
    (portfolio, fund_id, maximum_capacity, capital, updated)
    VALUES {}
    """.format((
        portfolio.portfolio_id,
        fid,
        portfolio.maximum_capacity,
        portfolio.capital,
        dt.datetime.now().strftime(IOFiles.date_format.value)
    )))
