import streamlit as st
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dashboard import admin_dashboard

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

admin_dashboard()
