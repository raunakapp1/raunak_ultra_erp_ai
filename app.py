import streamlit as st
import sqlite3

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

def login_ui():
    st.title("🔐 ERP Login")

    role = st.selectbox("Select Role", ["admin", "staff"])

    cur.execute("SELECT name FROM staff WHERE role=?", (role,))
    names = [x[0] for x in cur.fetchall()]

    username = st.selectbox("Select Name", names)
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cur.execute("SELECT id FROM staff WHERE name=? AND password=?", (username,password))
        user = cur.fetchone()
        if user:
            st.session_state["user"] = username
            st.session_state["role"] = role
            st.session_state["uid"] = user[0]
            st.experimental_rerun()
        else:
            st.error("Wrong Password")

def logout():
    if st.sidebar.button("🚪 Logout"):
        for k in st.session_state.keys():
            del st.session_state[k]
        st.experimental_rerun()
