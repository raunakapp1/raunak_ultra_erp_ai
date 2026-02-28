import streamlit as st
from local_db import get_conn
from datetime import date

def attendance_page(role):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id,name FROM staff")
    staff = cur.fetchall()

    if staff:
        names=[s["name"] for s in staff]
        ids=[s["id"] for s in staff]

        sel = st.selectbox("Staff",names)
        status = st.selectbox("Status",["Present","Absent","Leave"])

        if st.button("Mark"):
            sid = ids[names.index(sel)]
            cur.execute("INSERT INTO attendance VALUES(NULL,?,?,?)",
                        (sid,str(date.today()),status))
            conn.commit()
            st.success("Marked")

    cur.execute("""
    SELECT a.date,s.name,a.status
    FROM attendance a JOIN staff s ON s.id=a.staff_id
    ORDER BY a.date DESC""")

    st.table(cur.fetchall())
    conn.close()