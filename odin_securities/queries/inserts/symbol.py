from ...connection_cursor import cur


def symbol(symbol):
    cur.execute("INSERT INTO symbols (symbol) VALUES ('{}')".format(symbol))
