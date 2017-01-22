from ...connection_cursor import cur


def symbol(symbol):
    cur.execute("""
    SELECT EXISTS(SELECT 1 FROM symbols WHERE symbol='{}' LIMIT 1)
    """.format(symbol))
    return cur.fetchone()[0]
