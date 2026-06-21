import streamlit as st
from services.ml_service import predict_price

def app():
    st.title("AI Pricing Engine")

    buy = st.number_input("Buy Price", min_value=0.0)
    qty = st.number_input("Quantity", min_value=0)

    branch = st.selectbox("Branch", ["Nagpur", "Wardha", "Amravati"])
    branch_map = {"Nagpur": 0, "Wardha": 1, "Amravati": 2}

    if st.button("Predict"):
        price = predict_price(buy, qty, branch_map[branch])
        st.success(f"Suggested Price: ₹{round(price, 2)}")
