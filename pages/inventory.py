import streamlit as st
import os
import numpy as np

from services.inventory_service import add_product, get_all
from services.ml_service import predict_price
from services.vision_service import get_embedding


def app():

    st.title("📦 Smart Inventory System")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Product Name")
        buy = st.number_input("Buy Price", min_value=0.0)
        qty = st.number_input("Quantity", min_value=1)

    with col2:
        branch = st.selectbox(
            "Branch",
            ["Nagpur", "Wardha", "Amravati"]
        )

        branch_map = {
            "Nagpur": 0,
            "Wardha": 1,
            "Amravati": 2
        }

        ai_price = predict_price(
            buy,
            qty,
            branch_map[branch]
        )

        st.info(
            f"🤖 AI Suggested Price: ₹{round(ai_price, 2)}"
        )

        sell = st.number_input(
            "Selling Price",
            value=float(ai_price)
        )

    image = st.file_uploader(
        "Product Image",
        type=["jpg", "jpeg", "png"]
    )

    # ---------------- ADD PRODUCT ---------------- #

    if st.button("Add Product"):

        path = None

        # Save image and create embedding
        if image:

            os.makedirs("uploads", exist_ok=True)
            os.makedirs("embeddings", exist_ok=True)

            path = f"uploads/{image.name}"

            # Save image
            with open(path, "wb") as f:
                f.write(image.getbuffer())

            # Create AI embedding for image recognition
            try:
                embedding = get_embedding(path)

                np.save(
                    f"embeddings/{name}.npy",
                    embedding
                )

            except Exception as e:
                st.warning(
                    f"Embedding creation failed: {e}"
                )

        # Save product in database
        add_product(
            name,
            buy,
            sell,
            qty,
            branch,
            path
        )

        st.success("✅ Product Added Successfully")

    st.divider()

    # ---------------- SHOW INVENTORY ---------------- #

    st.subheader("📋 Inventory Data")

    data = get_all()

    if data:
        for row in data:
            st.write(row)
    else:
        st.info("No products added yet.")