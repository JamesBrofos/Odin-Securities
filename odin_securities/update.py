import requests
import urllib
from time import sleep
from .connection_cursor import conn
from .vendors import quandl, yahoo_finance, construct, supported_vendors
from .queries import gets, deletes


def update(symbols, n_prog=1):
    """Update the Odin Securities with the latest price and volume data for the
    specified assets.

    Parameters
    ----------
    symbols: List.
        A list of symbols whose price and volume data should be retrieved.
    n_prog (optional): Integer.
        Number of symbols to download before displaying progress to the console.
    """
    # Compute the number of symbols that we're going to acquire price and volume
    # and dividend and split data for.
    n_symbols = len(symbols)

    for s_ind, s in enumerate(symbols):
        # Display progress.
        if s_ind % n_prog == 0:
            print("Progress: {} / {}\t{}".format(s_ind+1, n_symbols, s))

        for v_ind, v in enumerate(supported_vendors):
            # Get identifier for vendor.
            vid = gets.id_for_vendor(v.name)
            # Try to download the asset using this vendor.
            done = False

            while not done:
                # TODO: We should have failure errors and delay errors for each
                #       of the data vendors to make some of this logic more
                #       elegant. We can revisit this as we encounter errors.
                construct(v, s)
                done = True

        # Commit changes.
        conn.commit()
