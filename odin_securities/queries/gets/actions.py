import pandas as pd
from ...connection_cursor import conn
from .standard_sessions import standard_sessions


def actions(
        start_date, end_date=None, symbols=None, standard=True
):
    """Return the stock split and dividend data for the specified symbol for the
    specified time period. This is used to augment unadjusted price data used in
    Odin's data handler object used in algorithmic trading.

    Parameters
    ----------
    start_date: Datetime object.
        The datetime indicating the beginning of the trading time period.
    end_date (optional): Datetime object.
        The datetime indicating the ending of the trading time period.
    symbols (optional): List of strings.
        A list of ticker symbols for which price data will be requested.
    standard (optional): Boolean.
        An indicator of whether or not to return only price data during
        "standard" trading sessions. These are trading sessions when the stock
        market is officially open.
    """
    # If no ending date is provided, then we take the start date and end date to
    # be the same.
    if end_date is None:
        end_date = start_date

    # If symbols are provided, then restrict the query to only the identified
    # securities. Otherwise, this query fetches data for all securities.
    if symbols is not None:
        symbol_cond = "s.symbol IN ({}) AND ".format(
            ", ".join(map(repr, tuple(symbols)))
        )
    else:
        symbol_cond = ""

    qry = """
    SELECT DISTINCT ON (a.datetime, s.symbol) s.symbol, a.datetime,
    a.split_ratio, a.dividend FROM symbols as s JOIN actions AS a ON
    a.symbol_id=s.id WHERE {} a.datetime >= '{}' AND a.datetime <= '{}' ORDER BY
    a.datetime, s.symbol, a.vendor_id
    """.format(symbol_cond, start_date, end_date)
    actions = pd.read_sql(qry, conn, index_col=["datetime", "symbol"]).to_panel()

    # Determine whether or not we should restrict the query to the standard
    # trading sessions.
    if standard:
        sess = standard_sessions(start_date, end_date)
        return actions.ix[:, sess["datetime"], :]
    else:
        return actions
