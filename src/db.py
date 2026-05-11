import os
from contextlib import contextmanager

import psycopg2


def get_conn():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        dbname=os.getenv("PGDATABASE", "demo_one_form"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "0990"),
    )


@contextmanager
def get_cursor():
    conn = get_conn()
    try:
        cur = conn.cursor()
        yield conn, cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
