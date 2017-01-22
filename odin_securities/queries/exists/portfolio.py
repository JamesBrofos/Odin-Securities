from ...connection_cursor import cur


def portfolio(portfolio):
    cur.execute("""
    SELECT EXISTS (SELECT 1 FROM portfolios WHERE portfolio='{}')
    """.format(portfolio))
    return cur.fetchone()[0]
