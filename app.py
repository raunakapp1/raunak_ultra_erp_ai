import streamlit as st
import sqlite3
import os

# ---------- BASIC CONFIG ----------
st.set_page_config(
    page_title="Raunak Ultra ERP AI",
    page_icon="🚀",
    layout="wide"
)

# ---------- DATABASE SETUP ----------
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/erp.db", check_same_thread=False)
cur = conn.cursor()

# ---------- INIT DATABASE ----------
def init_db():
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        password TEXT
    );

    CREATE TABLE IF NOT EXISTS guests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        category TEXT,
        pax INTEGER,
        visit_date TEXT,
        visit_time TEXT,
        staff_id INTEGER
    );

    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guest_id INTEGER,
        amount REAL,
        platform TEXT,
        bill_time TEXT
    );

    CREATE TABLE IF NOT EXISTS fraud_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        staff_id INTEGER,
        issue TEXT,
        score REAL,
        created_at TEXT
    );
    """)

    # Insert default users only if empty
    cur.execute("SELECT COUNT(*) FROM staff")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO staff (name,role,password) VALUES ('Admin','admin','1234')")
        cur.execute("INSERT INTO staff (name,role,password) VALUES ('Staff1','staff','1111')")
        conn.commit()

init_db()

# ---------- LOGIN ----------
def login_page():
    st.title("🔐 Login - Raunak Ultra ERP AI")

    role = st.selectbox("Select Role", ["admin", "staff"])

    cur.execute("SELECT name FROM staff WHERE role=?", (role,))
    names = [x[0] for x in cur.fetchall()]

    if not names:
        st.warning("No users found")
        return

    name = st.selectbox("Select Name", names)
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        cur.execute("SELECT id FROM staff WHERE name=? AND password=?", (name, password))
        user = cur.fetchone()

        if user:
            st.session_state["login"] = True
            st.session_state["user"] = name
            st.session_state["role"] = role
            st.session_state["uid"] = user[0]
            st.experimental_rerun()
        else:
            st.error("❌ Wrong Password")

# ---------- LOGOUT ----------
def logout_btn():
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.experimental_rerun()

# ---------- DASHBOARD ----------
def dashboard():
    st.header("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    cur.execute("SELECT COUNT(*) FROM guests")
    guests = cur.fetchone()[0]

    cur.execute("SELECT SUM(amount) FROM bills")
    revenue = cur.fetchone()[0] or 0

    cur.execute("SELECT COUNT(*) FROM fraud_logs")
    frauds = cur.fetchone()[0]

    col1.metric("👥 Guests", guests)
    col2.metric("💰 Revenue", f"₹ {revenue}")
    col3.metric("🚨 Fraud Alerts", frauds)

# ---------- GUEST ENTRY ----------
def guest_entry():
    st.header("👥 Guest Entry")

    name = st.text_input("Guest Name")
    mobile = st.text_input("Mobile")
    category = st.selectbox("Category", [
        "Swiggy","Zomato","Easy Dinner","Party","Walk-in","VIP","Other"
    ])
    pax = st.number_input("Number of Pax", 1, 50, 1)

    if st.button("Save Guest"):
        cur.execute("""
        INSERT INTO guests 
        (name,mobile,category,pax,visit_date,visit_time,staff_id)
        VALUES (?,?,?,?,DATE('now'),TIME('now'),?)
        """, (name,mobile,category,pax,st.session_state["uid"]))

        conn.commit()
        st.success("✅ Guest Added Successfully")

# ---------- AI INSIGHTS ----------
def ai_insights():
    st.header("🤖 AI Insights")

    cur.execute("SELECT COUNT(*) FROM fraud_logs")
    fraud = cur.fetchone()[0]

    cur.execute("SELECT SUM(amount) FROM bills")
    revenue = cur.fetchone()[0] or 0

    score = min(100, int((revenue/1000) + (fraud * -5) + 60))

    st.metric("🧠 Business Health Score", f"{score} / 100")

# ---------- MAIN APP ----------
if "login" not in st.session_state:
    login_page()
    st.stop()

logout_btn()

st.sidebar.title("🚀 Navigation")
menu = st.sidebar.radio("Go To", ["Dashboard", "Guests", "AI Insights"])

if menu == "Dashboard":
    dashboard()

elif menu == "Guests":
    guest_entry()

elif menu == "AI Insights":
    ai_insights()
