from ...connection_cursor import cur


def symbol_vendor(sid, vid, updated):
    cur.execute("""
    INSERT INTO symbol_vendor (symbol_id, vendor_id, updated) VALUES {}
    """.format((sid, vid, updated.strftime("%Y-%m-%d %H:%M:%S.%f"))))
