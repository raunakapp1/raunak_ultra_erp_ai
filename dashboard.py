import streamlit as st
import pandas as pd
from local_db import get_conn
from ai_layer.forecast_ai import predict_tomorrow_revenue
from ai_layer.offer_ai import generate_offer

def admin_dashboard():

    conn = get_conn()
    cur = conn.cursor()

    st.header("📊 Admin Control Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    cur.execute("SELECT COUNT(*) FROM guests")
    total_guests = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(pax) FROM guests")
    total_pax = cur.fetchone()[0] or 0

    cur.execute("SELECT COUNT(*) FROM attendance WHERE status='Absent'")
    total_absent = cur.fetchone()[0] or 0

    forecast = predict_tomorrow_revenue()

    col1.metric("👥 Total Guests", total_guests)
    col2.metric("🧍 Total PAX", total_pax)
    col3.metric("🚫 Absents", total_absent)
    col4.metric("🤖 Tomorrow Prediction", f"₹ {forecast}")

    st.divider()

    st.subheader("📌 Category Wise Report")
    cur.execute("""
        SELECT category, COUNT(*), SUM(pax)
        FROM guests
        GROUP BY category
    """)
    cat_data = cur.fetchall()

    if cat_data:
        df = pd.DataFrame(cat_data, columns=["Category", "Guests", "Total PAX"])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index("Category")["Guests"])

    st.subheader("📅 Date Wise Report")
    cur.execute("""
        SELECT entry_date, COUNT(*), SUM(pax)
        FROM guests
        GROUP BY entry_date
        ORDER BY entry_date DESC
    """)
    date_data = cur.fetchall()

    if date_data:
        df2 = pd.DataFrame(date_data, columns=["Date", "Guests", "PAX"])
        st.dataframe(df2, use_container_width=True)
        st.line_chart(df2.set_index("Date")["Guests"])

    st.subheader("👨‍💼 Staff Performance")
    cur.execute("""
        SELECT s.name, COUNT(g.id)
        FROM guests g
        JOIN staff s ON g.added_by_staff_id = s.id
        GROUP BY s.name
    """)

    staff_data = cur.fetchall()
    if staff_data:
        df3 = pd.DataFrame(staff_data, columns=["Staff", "Guest Entries"])
        st.dataframe(df3, use_container_width=True)
        st.bar_chart(df3.set_index("Staff")["Guest Entries"])

    offer = generate_offer(total_guests)
    st.success(f"🎯 AI Suggested Offer: {offer}")

    conn.close()