from ...connection_cursor import cur


def position(sid, pid):
    cur.execute("""DELETE FROM positions WHERE symbol_id={} AND portfolio_id={}
    """.format(sid, pid))
