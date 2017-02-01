from ...connection_cursor import cur
from ...io_params import IOFiles


def position(position, sid, pid):
    props = "{}".format((
        sid, pid, position.direction.value, position.trade_type.value,
        position.date_entered.strftime(IOFiles.date_format.value),
        position.avg_price, position.buys, position.sells,
        position.avg_buys_price, position.avg_sells_price,
        position.tot_buys_price, position.tot_sells_price,
        position.tot_commission,
    ))
    cur.execute("""
    INSERT INTO positions (
        symbol_id,
        portfolio_id,
        direction,
        trade_type,
        date_entered,
        avg_price,
        buys,
        sells,
        avg_buys_price,
        avg_sells_price,
        tot_buys_price,
        tot_sells_price,
        tot_commission
    ) VALUES {}
    """.format(props))
