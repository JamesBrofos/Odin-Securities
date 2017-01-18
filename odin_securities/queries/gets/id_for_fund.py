from ...connection_cursor import cur


def id_for_fund(fund):
    """Retrieves the integer identification number for the specified fund.

    Parameters
    ----------
    fund: String.
        The fund whose integer identifier is requested.
    """
    cur.execute("SELECT id FROM funds WHERE fund='{}'".format(fund))
    return cur.fetchone()[0]
