from ...connection_cursor import cur


def prices_actions(sid, vid):
    cur.execute(
        "DELETE FROM prices WHERE symbol_id={} AND vendor_id={}".format(
            sid, vid
        )
    )
    cur.execute(
        "DELETE FROM actions WHERE symbol_id={} AND vendor_id={}".format(
            sid, vid
        )
    )
