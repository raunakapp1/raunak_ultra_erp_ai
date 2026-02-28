import sqlite3

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

def business_health():
    cur.execute("SELECT SUM(amount) FROM bills")
    revenue = cur.fetchone()[0] or 0

    cur.execute("SELECT COUNT(*) FROM guests")
    guests = cur.fetchone()[0]

    score = min(100, (revenue/1000)+(guests*2))

    return round(score,2)
