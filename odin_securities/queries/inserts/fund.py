from ...connection_cursor import cur


def fund(fund):
    # Note that we do not use literate strings here to allow psycopg2 to
    # properly handle none elements (such and rebalance and manage period).
    cur.execute("""
    INSERT INTO funds (fund, rebalance_period, manage_period, entry_date)
    VALUES %s
    """, (
        fund.fund_id, fund.rebalance_period, fund.manage_period,
        fund.date_entered.strftime("%Y-%m-%d %H:%M:%S")
    ))
