from ...connection_cursor import cur


def symbol_vendor(sid, vid):
    cur.execute("""
    SELECT NOT EXISTS(SELECT 1 FROM symbol_vendor WHERE symbol_id={} AND
    vendor_id={} LIMIT 1)
    """.format(sid, vid))
    return cur.fetchone()[0]
