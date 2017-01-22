from ...connection_cursor import cur


def symbols():
    cur.execute("SELECT symbol FROM symbols")
    return [x[0] for x in cur.fetchall()]
