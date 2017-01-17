# Odin Securities Database Constructor

This module implements the capability to initialize and update price data obtained from Odin's data vendors. This approach has the advantage of not requiring price data to be streamed over a network connection.

The Odin securities database is responsible for over 3,000 different assets. As such, redownloading the entire dataset is costly and unnecessary. Instead, at the end of each day, the database is updated with the latest bar data. Entire stocks are redownloaded whenever a stock split or a dividend is received.


## Initializing and Updating the Database

To initialize or update the database with the latest price data, execute the command:

```
python3 constructor.py
```

To download a particular asset in addition to the defaults, you may append command line arguments corresponding to tickers. For instance, to download Amazon's latest price and volume data, simply execute `python3 constructor.py AMZN`


