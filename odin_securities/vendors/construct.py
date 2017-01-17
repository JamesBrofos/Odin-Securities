from ..queries import exists, gets, inserts, deletes, updates


def construct(vendor, symbol):
    # If this symbol is new to the Odin securities database, then insert it into
    # the symbols table.
    if exists.symbol(symbol):
        inserts.symbol(symbol)

    # Extract the identifier for this symbol as well as the identifier for the
    # (potential) vendor.
    sid = gets.id_for_symbol(symbol)
    vid = gets.id_for_vendor(vendor.name)

    # Detect if the symbol can be downloaded from the vendor.
    if vendor.check_valid_symbol(symbol):
        # Check if the symbol is already being served by the vendor. Recall that
        # this first boolean returns true if the symbol is not servicing the
        # symbol.
        if exists.symbol_vendor(sid, vid):
            # If the symbol is not being served by the vendor, then initialize
            # new price data from the asset's entire history.
            stock = vendor.download_stock(symbol)
            inserts.prices_actions(stock, sid, vid)

            # Get the current datetime for updating the asset.
            update_remote = vendor.download_remote_updated(symbol)
            inserts.symbol_vendor(sid, vid, update_remote)
        else:
            # Check if the most recent remote update of price information is
            # more current than what is available from the vendor locally.
            update_local = gets.updated_for_symbol_vendor(sid, vid)
            update_remote = vendor.download_remote_updated(symbol)

            if update_local < update_remote:
                # Update or redownload the stock price depending on whether or
                # not a split or dividend occurred.
                stock = vendor.download_stock(
                    symbol, start_date=update_local
                ).ix[1:]
                # Detect stock splits and dividends.
                if (
                        (stock["Split Ratio"] != 1.).any() or
                        (stock["Ex-Dividend"] != 0.).any()
                ):
                    stock = vendor.download_stock(symbol)
                    deletes.prices_actions(sid, vid)

                # Send the new data to the database.
                inserts.prices_actions(stock, sid, vid)
                updates.symbol_vendor(sid, vid, update_remote)
