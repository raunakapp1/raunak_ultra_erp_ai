import streamlit as st
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)

from dashboard import admin_dashboard

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

admin_dashboard()
