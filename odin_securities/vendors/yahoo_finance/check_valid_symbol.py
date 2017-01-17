from yahoo_finance import Share


def check_valid_symbol(symbol):
    """We identify invalid shares if there is no official company name
    associated with the specified ticker.
    """
    s = Share(symbol)
    return s.get_name() is not None
