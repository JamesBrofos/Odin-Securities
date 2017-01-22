import requests
import sys, getopt
import pandas_datareader
import datetime as dt
import urllib
import psycopg2
import yahoo_finance
from time import sleep
from odin_securities import conn
from odin_securities.vendors import quandl, yahoo_finance, construct
from odin_securities.queries import gets, deletes


# Create a vector of vendors.
vendors = [quandl, yahoo_finance]

# For testing, it may be desirable to download more assets. We accomplish
# this by providing the ticks as command line arguments.
opts, args = getopt.getopt(sys.argv[1:], "li:")

if len(sys.argv) == 1:
    # Set base symbols to download and extend with more.
    symbols = ["^GSPC", "^OEX", "SPY", "OEF"]
    symbols.extend(quandl.download_symbols())
else:
    for opt, arg in opts:
        if opt == "-l":
            symbols = gets.symbols()
        elif opt == "-i":
            symbols = arg.split(" ")

# Compute the number of symbols that we're going to acquire price and volume and
# dividend and split data for.
n_symbols = len(symbols)
# Number to download before committing changes (to keep track of progress).
n_prog = 1

for i, s in enumerate(symbols):
    # Save changes.
    if i % n_prog == 0 or i == n_symbols - 1:
        print("Progress: {} / {}\t{}".format(i+1, n_symbols, s))

    for v in vendors:
        # Get identifier for vendor.
        vid = gets.id_for_vendor(v.name)

        # Try to download the asset using this vendor.
        done, succeeded = False, True
        while not done:
            try:
                construct(v, s)
                done = True
            except (
                    pandas_datareader._utils.RemoteDataError
            ):
                done, succeeded = True, False
            except (
                    quandl.quandl.errors.quandl_error.LimitExceededError,
                    quandl.quandl.errors.quandl_error.InternalServerError,
                    quandl.quandl.errors.quandl_error.QuandlError,
                    requests.exceptions.ConnectionError,
                    urllib.error.URLError,
                    yahoo_finance.YQLResponseMalformedError
            ):
                print("Error. Sleeping.")
                # Get identifier for symbol.
                sid = gets.id_for_symbol(s)
                # Clear out the (possibly) bad and irrelevant data.
                deletes.prices_actions(sid, vid)
                deletes.symbol_vendor(sid, vid)
                sleep(60)

    # Commit changes.
    if succeeded:
        conn.commit()
