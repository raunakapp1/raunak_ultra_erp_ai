import pandas as pd
from local_db import get_conn
from datetime import date

def generate_excel_report():
    conn = get_conn()

    df = pd.read_sql("""
        SELECT g.name, g.phone, g.pax, g.category, g.entry_date, s.name as staff
        FROM guests g
        JOIN staff s ON g.added_by_staff_id = s.id
    """, conn)

    filename = f"reports/guest_report_{date.today()}.xlsx"
    df.to_excel(filename, index=False)

    conn.close()
    return filename