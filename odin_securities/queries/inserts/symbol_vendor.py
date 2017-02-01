from ...connection_cursor import cur
from ...io_params import IOFiles


def symbol_vendor(sid, vid, updated):
    cur.execute("""
    INSERT INTO symbol_vendor (symbol_id, vendor_id, updated) VALUES {}
    """.format((sid, vid, updated.strftime(IOFiles.date_format.value))))
