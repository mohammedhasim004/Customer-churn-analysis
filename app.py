import streamlit as st

st.title("📊 Customer Churn Predictor")

tenure = st.slider("Tenure (Months)", 1, 72, 12)
monthly_charges = st.number_input("Monthly Charges ($)", 10.0, 150.0, 65.0)

if st.button("Predict"):
    if monthly_charges > 70 and tenure < 12:
        st.error("⚠️ Customer will Churn (Leave)")
    else:
        st.success("✅ Customer will Stay")
