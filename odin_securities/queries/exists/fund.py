from ...connection_cursor import cur


def fund(fund):
    cur.execute("""
    SELECT EXISTS (SELECT 1 FROM funds WHERE fund='{}')
    """.format(fund))
    return cur.fetchone()[0]
