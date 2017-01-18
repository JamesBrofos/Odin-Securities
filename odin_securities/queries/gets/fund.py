import pandas as pd
from ...connection_cursor import conn


def fund(fund):
    qry = "SELECT * FROM funds WHERE fund='{}'".format(fund)
    retval = pd.read_sql(qry, conn, index_col=["id"])
    return retval

def fund_for_fund_id(fid):
    qry = "SELECT * FROM funds WHERE id={}".format(fid)
    return pd.read_sql(qry, conn, index_col=["id"])
