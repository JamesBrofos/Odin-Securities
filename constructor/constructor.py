import sys
import getopt
from odin_securities import update
from odin_securities.queries import gets


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

# Update the database.
update(symbols)
