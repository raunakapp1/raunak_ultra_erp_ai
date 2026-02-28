import streamlit as st
from local_db import create_tables
from staff_engine import staff_page
from guests_engine import guests_page
from attendance_engine import attendance_page
from ai_engine import ai_dashboard
from dashboard import admin_dashboard
from auth import login_page

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Raunak Ultra ERP AI",
    page_icon="🚀",
    layout="wide"
)

# ---------- INIT DATABASE ----------
create_tables()

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "staff_id" not in st.session_state:
    st.session_state.staff_id = 1

# ---------- LOGIN ----------
if not st.session_state.logged_in:
    login_page()
    st.stop()

# ---------- SIDEBAR ----------
st.sidebar.title("🚀 Raunak Ultra ERP AI")

if st.sidebar.button("🔓 Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

st.sidebar.success(f"Role: {st.session_state.role}")

st.session_state.staff_id = st.sidebar.number_input(
    "Staff ID", min_value=1, value=st.session_state.staff_id
)

menu = st.sidebar.radio(
    "📂 Navigation",
    ["Dashboard", "Guests", "Attendance", "Staff", "AI Insights"]
)

# ---------- ROUTING ----------
if menu == "Dashboard":
    if st.session_state.role == "Admin":
        admin_dashboard()
    else:
        st.subheader("📊 Dashboard")
        st.info("Limited access")

elif menu == "Guests":
    guests_page(st.session_state.staff_id)

elif menu == "Attendance":
    attendance_page(st.session_state.role)

elif menu == "Staff":
    if st.session_state.role == "Admin":
        staff_page(st.session_state.role)
    else:
        st.warning("Access Denied")

elif menu == "AI Insights":
    if st.session_state.role in ["Admin", "Manager"]:
        ai_dashboard()
    else:
        st.warning("Access Denied")

st.markdown("---")
st.caption("⚡ Powered by Raunak Ultra ERP AI")
