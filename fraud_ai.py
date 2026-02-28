import sqlite3
import numpy as np

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

def fraud_scan():
    cur.execute("""
    SELECT staff_id, COUNT(*) FROM bills 
    WHERE amount < 50 GROUP BY staff_id
    """)

    suspicious = cur.fetchall()

    for staff, count in suspicious:
        score = min(95, count * 12)

        if score > 60:
            cur.execute("""INSERT INTO fraud_logs 
                (staff_id, issue, score, created_at)
                VALUES (?,?,?,datetime('now'))""",
                (staff,"High low-value bills",score))

    conn.commit()
