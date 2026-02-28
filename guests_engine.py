import sqlite3
import streamlit as st
from datetime import datetime

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

def guest_entry_ui():
    st.header("👥 Guest Entry")

    name = st.text_input("Guest Name")
    mobile = st.text_input("Mobile Number")

    category = st.selectbox("Category",[
        "Swiggy","Zomato","Easy Dinner","Party","Walk-in","VIP","Other"
    ])

    pax = st.number_input("Number of PAX",1,50,1)

    if st.button("Save Entry"):
        cur.execute("""INSERT INTO guests 
            (name,mobile,category,pax,visit_date,visit_time,staff_id)
            VALUES (?,?,?,?,?,?,?)""",
            (name,mobile,category,pax,
             datetime.now().date(),
             datetime.now().time().strftime("%H:%M"),
             st.session_state["uid"]))

        conn.commit()
        st.success("Guest Entry Saved")
