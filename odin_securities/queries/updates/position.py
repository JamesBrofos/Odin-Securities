from ...connection_cursor import cur


def position(position, sid, pid):
    props = "{}".format((
        position.quantity, position.avg_price,
        position.buys, position.sells,
        position.avg_buys_price, position.avg_sells_price,
        position.tot_buys_price, position.tot_sells_price,
        position.tot_commission
    ))
    cur.execute("""
    UPDATE positions SET (
    quantity, avg_price, buys, sells, avg_buys_price, avg_sells_price,
    tot_buys_price, tot_sells_price, tot_commission
    ) = {} WHERE symbol_id={} AND portfolio_id={}
    """.format(props, sid, pid))
