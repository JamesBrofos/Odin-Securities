from ...connection_cursor import cur


def id_for_vendor(vendor):
    """Retrieves the integer identification number for the specified vendor.

    Parameters
    ----------
    vendor: String.
        The vendor whose integer identifier is requested.
    """
    cur.execute("SELECT id FROM vendors WHERE vendor='{}'".format(vendor))
    return cur.fetchone()[0]
