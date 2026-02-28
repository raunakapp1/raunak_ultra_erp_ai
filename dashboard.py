import streamlit as st
import sys
import os

# Force root path add
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_layer.forecast_ai import predict_tomorrow_revenue

def admin_dashboard():
    st.title("📊 Raunak Ultra ERP AI Dashboard")

    today_sales = st.number_input("Today's Total Revenue", min_value=0)

    if st.button("Predict Tomorrow Revenue"):
        prediction = predict_tomorrow_revenue(today_sales)
        st.success(f"Tomorrow Expected Revenue: ₹ {prediction}")
