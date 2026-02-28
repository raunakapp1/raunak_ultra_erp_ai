import streamlit as st
import random

def ai_dashboard():
    st.subheader("🤖 AI Insights")

    st.metric("Fraud Risk",f"{random.randint(1,15)} %")
    st.metric("Sales Growth",f"{random.randint(5,30)} %")
    st.metric("Business Health",f"{random.randint(70,95)}/100")