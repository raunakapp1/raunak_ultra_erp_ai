import sqlite3

DB_FILE = "raunak_erp.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
