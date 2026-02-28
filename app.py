import streamlit as st
from local_db import create_tables
from staff_engine import staff_page
from guests_engine import guests_page
from attendance_engine import attendance_page
from ai_engine import ai_dashboard

create_tables()

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

st.sidebar.title("🚀 Navigation")

role = st.sidebar.selectbox("Role", ["Admin","Manager","Staff","Viewer"])
staff_id = st.sidebar.number_input("Staff ID", 1, value=1)

menu = st.sidebar.radio("Go To", ["Dashboard","Guests","Attendance","Staff","AI Insights"])

if menu == "Dashboard":
    st.title("Raunak Ultra ERP AI 🚀")

elif menu == "Guests":
    guests_page(staff_id)

elif menu == "Attendance":
    attendance_page(role)

elif menu == "Staff":
    staff_page(role)

elif menu == "AI Insights":
    ai_dashboard()