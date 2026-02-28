import streamlit as st
import sys
import os

# Force root path add
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dashboard import admin_dashboard

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

admin_dashboard()
