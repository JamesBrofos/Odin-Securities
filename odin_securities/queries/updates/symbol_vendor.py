from ...connection_cursor import cur


def symbol_vendor(sid, vid, updated):
        cur.execute("""UPDATE symbol_vendor SET updated='{}' WHERE symbol_id={}
        AND vendor_id={}""".format(
            updated.strftime("%Y-%m-%d %H:%M:%S.%f"), sid, vid
        ))
