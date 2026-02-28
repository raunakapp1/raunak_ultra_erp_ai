import streamlit as st
import os
import sys

# 🔧 Hard fix for Streamlit Cloud import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AI_DIR = os.path.join(BASE_DIR, "ai_layer")

if AI_DIR not in sys.path:
    sys.path.insert(0, AI_DIR)

from forecast_ai import predict_tomorrow_revenue


def admin_dashboard():
    st.title("📊 Raunak Ultra ERP AI Dashboard")

    today_sales = st.number_input("Today's Total Revenue", min_value=0)

    if st.button("Predict Tomorrow Revenue"):
        prediction = predict_tomorrow_revenue(today_sales)
        st.success(f"Tomorrow Expected Revenue: ₹ {prediction}")
