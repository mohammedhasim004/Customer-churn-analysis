import streamlit as st

st.title("📊 Customer Churn Predictor")

tenure = st.slider("Tenure (Months)", 1, 72, 12)
monthly_charges = st.number_input("Monthly Charges (₹)", 100.0, 15000.0, 5000.0)

if st.button("Predict"):
    if tenure < 12 and monthly_charges > 5000:
        st.error("⚠️ Customer will Churn (Leave) - New customer with high charges")
    elif tenure >= 12 and monthly_charges > 9000:
        st.error("⚠️ Customer will Churn (Leave) - Old customer with excessive charges")
    else:
        st.success("✅ Customer will Stay")