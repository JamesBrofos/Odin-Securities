from ...connection_cursor import cur


def updated_for_symbol_vendor(sid, vid):
    cur.execute("""
    SELECT updated FROM symbol_vendor WHERE symbol_id={} AND vendor_id={}
    """.format(sid, vid))
    return cur.fetchone()[0]
