from ...connection_cursor import cur


def fund(fund):
    cur.execute("""
    INSERT INTO funds (fund, rebalance_period, manage_period, entry_date)
    VALUES {}
    """.format((
        fund.fund_id, fund.rebalance_period, fund.manage_period,
        fund.date_entered.strftime("%Y-%m-%d %H:%M:%S")
    )))
