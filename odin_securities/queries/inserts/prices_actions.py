from ...connection_cursor import cur


def prices_actions(stock, symbol_id, vendor_id):
    """Insert the price and corporate actions data for a given stock into the
    database.
    """
    # Prune not-a-numbers.
    stock.dropna(inplace=True)
    # Set the columns for extracting information into the price database. Set
    # similar columns for corporate actions.
    price_cols = [
        "Open", "High", "Low", "Close", "Volume", "Adj. Open", "Adj. High",
        "Adj. Low", "Adj. Close", "Adj. Volume"
    ]
    action_cols = ["Split Ratio", "Ex-Dividend"]
    # Create a execution query string.
    price_values = ""
    action_values = ""
    # Iterate through all the dates in the stock price dataset and update the
    # database with the newly acquired data.
    for date_idx in stock.index:
        string_date = str(date_idx)
        price_v = list(stock[price_cols].ix[date_idx])
        a = stock[action_cols].ix[date_idx]
        action_v = list(a)
        price_v.insert(0, string_date)
        price_v.insert(0, vendor_id)
        price_v.insert(0, symbol_id)
        action_v.insert(0, string_date)
        action_v.insert(0, vendor_id)
        action_v.insert(0, symbol_id)
        price_values += "{},".format(tuple(price_v))
        if a["Split Ratio"] != 1.0 or a["Ex-Dividend"] > 0.0:
            action_values += "{},".format(tuple(action_v))

    # Remove the trailing comma.
    price_values = price_values[:-1]
    action_values = action_values[:-1]
    # Send the data for this stock to the database.
    if price_values != "":
        cur.execute("""
        INSERT INTO prices (
        symbol_id, vendor_id, datetime, price_open, price_high, price_low,
        price_close, volume, adj_price_open, adj_price_high, adj_price_low,
        adj_price_close, adj_volume
        ) VALUES {}
        """.format(price_values))

    if action_values != "":
        cur.execute("""
        INSERT INTO actions (
        symbol_id, vendor_id, datetime, split_ratio, dividend
        ) VALUES {}
        """.format(action_values))
