from ...connection_cursor import cur


def symbol_vendor(sid, vid):
    cur.execute("""
    DELETE FROM symbol_vendor WHERE symbol_id={} AND vendor_id={}
    """.format(sid, vid))
