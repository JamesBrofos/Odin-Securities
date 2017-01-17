import psycopg2 as pg


conn = pg.connect(
    "dbname='securities_master' user='securities' password='odin'"
)
cur = conn.cursor()
