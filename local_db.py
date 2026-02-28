import sqlite3

DB_FILE = "raunak_erp.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_conn()
    cur = conn.cursor()

    # STAFF
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            role TEXT
        )
    """)

    # USERS LOGIN
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    # GUESTS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            pax INTEGER,
            category TEXT,
            entry_date TEXT,
            added_by_staff_id INTEGER
        )
    """)

    # ATTENDANCE
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            staff_id INTEGER,
            date TEXT,
            status TEXT
        )
    """)

    # FRAUD LOG
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fraud_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()
