from ...connection_cursor import cur


def id_for_portfolio(portfolio):
    """Retrieves the integer identification number for the specified portfolio.

    Parameters
    ----------
    portfolio: String.
        The portfolio whose integer identifier is requested.
    """
    cur.execute(
        "SELECT id FROM portfolios WHERE portfolio='{}'".format(portfolio)
    )
    return cur.fetchone()[0]
