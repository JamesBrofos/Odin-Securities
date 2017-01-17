from ...connection_cursor import cur


def id_for_symbol(symbol):
    """Retrieves the integer identification number for the specified symbol.

    Parameters
    ----------
    symbol: String.
        The symbol whose integer identifier is requested.
    """
    cur.execute("SELECT id FROM symbols WHERE symbol='{}'".format(symbol))
    return cur.fetchone()[0]
