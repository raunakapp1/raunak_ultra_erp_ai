import streamlit as st
from local_db import get_conn
from datetime import date, datetime

def guests_page(staff_id):
    st.subheader("👥 Guest Entry")

    conn = get_conn()
    cur = conn.cursor()

    name = st.text_input("Name")
    phone = st.text_input("Mobile")
    pax = st.number_input("Pax",1,100,1)
    category = st.selectbox("Category",[
        "Swiggy","Zomato","EasyDinner","Party",
        "W/I","VIP","Buffet","Holi","Other"
    ])
    entry_date = st.date_input("Date",date.today())
    entry_time = st.time_input("Time",datetime.now().time())

    if st.button("Save"):
        cur.execute("""INSERT INTO guests 
        (name,phone,pax,category,entry_date,entry_time,added_by_staff_id)
        VALUES(?,?,?,?,?,?,?)""",
        (name,phone,pax,category,str(entry_date),str(entry_time),staff_id))
        conn.commit()
        st.success("Guest Saved")

    cur.execute("SELECT * FROM guests ORDER BY id DESC")
    st.table(cur.fetchall())

    conn.close()