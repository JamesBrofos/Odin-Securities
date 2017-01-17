import pandas as pd
from ...connection_cursor import conn


def standard_sessions(start_date, end_date):
    """Return the datetimes corresponding to the trading sessions in a specified
    time period during which the stock market was officially open.

    Parameters
    ----------
    start_date: Datetime object.
        The datetime indicating the beginning of the trading time period.
    end_date (optional): Datetime object.
        The datetime indicating the ending of the trading time period.
    """
    qry = """
    SELECT p.datetime FROM prices AS p JOIN symbols as s ON p.symbol_id = s.id
    WHERE s.symbol='^GSPC' AND p.datetime >= '{}' AND p.datetime <= '{}'
    """.format(start_date, end_date)
    return pd.read_sql(qry, conn)
