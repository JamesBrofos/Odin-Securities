from ...connection_cursor import cur


def position(sid, pid):
    cur.execute("""
    SELECT NOT EXISTS(SELECT 1 FROM positions WHERE symbol_id={} AND
    portfolio_id={})""".format(sid, pid))
    return cur.fetchone()[0]
