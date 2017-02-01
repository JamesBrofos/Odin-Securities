import datetime as dt
from ...connection_cursor import cur
from ...io_params import IOFiles


def portfolio(portfolio, pid):
    cur.execute("""
    UPDATE portfolios SET (maximum_capacity, capital, updated) = {} WHERE id={}
    """.format(
        (portfolio.maximum_capacity, portfolio.capital,
         dt.datetime.now().strftime(IOFiles.date_format.value)), pid)
    )
