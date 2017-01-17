from ...connection_cursor import cur


def closed_position(sid, pid):
    cur.execute("""INSERT INTO closed_positions SELECT * FROM positions WHERE
    symbol_id={} AND portfolio_id={}""".format(sid, pid))
