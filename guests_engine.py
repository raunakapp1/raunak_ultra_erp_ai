import streamlit as st
from local_db import get_conn
from datetime import date

def guests_page(current_staff_id):

    st.subheader("👥 Guest Entry Panel")

    conn = get_conn()
    cursor = conn.cursor()

    with st.expander("➕ Add Guest"):
        name = st.text_input("Guest Name")
        phone = st.text_input("Mobile Number")
        pax = st.number_input("Number of Guests (PAX)", min_value=1, max_value=100, value=1)

        category = st.selectbox(
            "Category",
            ["Swiggy", "Zomato", "Walk-in", "Dinner", "Party", "W/I", "VIP", "Other"]
        )

        entry_date = st.date_input("Visit Date", date.today())

        if st.button("✅ Save Guest Entry"):
            cursor.execute("""
                INSERT INTO guests (name, phone, pax, category, entry_date, added_by_staff_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, phone, pax, category, str(entry_date), current_staff_id))

            conn.commit()
            st.success("Guest Entry Saved Successfully 🎉")

    st.divider()

    st.subheader("📋 Today's Guest List")

    cursor.execute("""
        SELECT g.name, g.phone, g.pax, g.category, s.name
        FROM guests g
        JOIN staff s ON g.added_by_staff_id = s.id
        WHERE g.entry_date = ?
    """, (str(date.today()),))

    rows = cursor.fetchall()

    if rows:
        st.table(rows)
    else:
        st.info("No guest entries for today")

    conn.close()
