import streamlit as st
from local_db import get_conn

def staff_page(role):
    conn = get_conn()
    cur = conn.cursor()

    if role=="Admin":
        name = st.text_input("Staff Name")
        phone = st.text_input("Phone")
        role = st.selectbox("Role",["Admin","Manager","Staff","Viewer"])

        if st.button("Add Staff"):
            cur.execute("INSERT INTO staff(name,phone,role) VALUES(?,?,?)",
                        (name,phone,role))
            conn.commit()
            st.success("Staff Added")

    cur.execute("SELECT * FROM staff")
    st.table(cur.fetchall())

    conn.close()