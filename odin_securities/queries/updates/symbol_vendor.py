from ...connection_cursor import cur
from ...io_params import IOFiles


def symbol_vendor(sid, vid, updated):
        cur.execute("""UPDATE symbol_vendor SET updated='{}' WHERE symbol_id={}
        AND vendor_id={}""".format(
            updated.strftime(IOFiles.date_format.value), sid, vid
        ))
