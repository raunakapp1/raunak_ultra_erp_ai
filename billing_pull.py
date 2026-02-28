import time
import random
import sqlite3

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

def fetch_external_bills():
    for _ in range(5):
        cur.execute("""INSERT INTO bills
            (guest_id,amount,platform,bill_time)
            VALUES (?,?,?,datetime('now'))""",
            (random.randint(1,5),
             random.randint(120,900),
             random.choice(["Swiggy","Zomato","POS"]),
             ))
    conn.commit()
