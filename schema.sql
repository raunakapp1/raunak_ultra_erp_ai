from ai_layer.health_score_ai import business_health

st.metric("🔥 Business Health", f"{business_health()} / 100")
