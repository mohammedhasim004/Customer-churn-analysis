import streamlit as st

st.title("📊 Customer Churn Predictor")

tenure = st.slider("Tenure (Months)", 1, 72, 1)
monthly_charges = st.number_input("Monthly Charges (₹)", 10.0, 2000.0, 150.0)

if st.button("Predict"):
    # முதல் 1 மாதத்தில் ₹150க்கு மேல் இருந்தால் Churn
    if tenure == 1 and monthly_charges > 150:
        st.error("⚠️ Customer will Churn (Leave) - 1st month charges exceeded ₹150")
    # 2வது மாதம் முதல் ₹300க்கு மேல் இருந்தால் Churn
    elif tenure >= 2 and monthly_charges > 300:
        st.error("⚠️ Customer will Churn (Leave) - Monthly charges exceeded ₹300")
    else:
        st.success("✅ Customer will Stay")