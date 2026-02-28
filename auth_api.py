import streamlit as st
from local_db import get_conn

def login_page():
    st.header("🔐 Login")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users")
    users = [x[0] for x in cur.fetchall()]

    user = st.selectbox("Select User", users)
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        cur.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (user, pwd)
        )
        row = cur.fetchone()

        if row:
            st.session_state.logged_in = True
            st.session_state.role = row["role"]
            st.success("Login Successful")
            st.experimental_rerun()
        else:
            st.error("Wrong Password")

    conn.close()
