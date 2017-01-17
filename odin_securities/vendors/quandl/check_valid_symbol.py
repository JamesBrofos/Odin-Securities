from .quandl_init import quandl
from .download_metadata import download_metadata


def check_valid_symbol(symbol):
    """Quandl symbols are identified as valid if there exists a dataset
    associated with the specified symbol. Otherwise, they are assumed invalid.
    """
    try:
        dataset = "WIKI/{}".format(symbol)
        download_metadata(dataset)
    except quandl.errors.quandl_error.NotFoundError:
        return False
    else:
        return True
