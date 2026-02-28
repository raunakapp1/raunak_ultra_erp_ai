from fpdf import FPDF
from local_db import get_conn
from datetime import date

def generate_pdf_report():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT category, COUNT(*), SUM(pax)
        FROM guests GROUP BY category
    """)

    data = cur.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Raunak Ultra ERP - Daily Report", ln=True, align="C")

    for row in data:
        pdf.cell(200, 10, f"{row[0]} - Guests: {row[1]}  Pax: {row[2]}", ln=True)

    filename = f"reports/daily_report_{date.today()}.pdf"
    pdf.output(filename)

    conn.close()
    return filename