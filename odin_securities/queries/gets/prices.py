import pandas as pd
from ...connection_cursor import conn
from .standard_sessions import standard_sessions


def prices(
        start_date, end_date=None, symbols=None, adjusted=True, standard=True
):
    """Return the price data for the specified symbol for the specified time
    period. This is used to supply historical bar data and price data to Odin's
    data handler object used in algorithmic trading.

    Parameters
    ----------
    start_date: Datetime object.
        The datetime indicating the beginning of the trading time period.
    end_date (optional): Datetime object.
        The datetime indicating the ending of the trading time period.
    symbols (optional): List of strings.
        A list of ticker symbols for which price data will be requested.
    adjusted (optional): Boolean.
        An indicator variable for whether or not to return the split and
        dividend adjusted prices or the raw prices.
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

    # Format the query appropriately when adjusted or unadjusted prices are
    # requested.
    fields = ["price_open", "price_high", "price_low", "price_close", "volume"]
    fields = ["p.adj_" + f if adjusted else "p." + f for f in fields]
    qry = """
    SELECT DISTINCT ON (p.datetime, s.symbol) s.symbol, p.datetime, {}
    FROM prices AS p
    JOIN symbols AS s ON
    p.symbol_id=s.id WHERE {}
    p.datetime >= '{}' AND p.datetime <= '{}'
    ORDER BY p.datetime, s.symbol, p.vendor_id
    """.format(", ".join(fields), symbol_cond, start_date, end_date)
    prices = pd.read_sql(qry, conn, index_col=["datetime", "symbol"]).to_panel()

    # Determine whether or not we should restrict the query to the standard
    # trading sessions.
    if standard:
        sess = standard_sessions(start_date, end_date)
        return prices.ix[:, sess["datetime"], :]
    else:
        return prices
