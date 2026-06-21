import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import os

from services.vision_service import get_embedding


def app():

    st.title("📊 Business Intelligence Dashboard")

    # =====================================================
    # LOAD DATA FIRST
    # =====================================================

    conn = sqlite3.connect("database/inventory.db")
    df = pd.read_sql_query("SELECT * FROM products", conn)

    if df.empty:
        st.warning("No data available yet")
        return

    # =====================================================
    # 📸 SCANNER SECTION
    # =====================================================

    st.markdown("## 📸 Smart Product Scanner")

    upload = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])

    matched_product = None
    best_score = None

    if upload:

        os.makedirs("temp", exist_ok=True)
        os.makedirs("embeddings", exist_ok=True)

        temp_path = f"temp/{upload.name}"

        with open(temp_path, "wb") as f:
            f.write(upload.getbuffer())

        st.image(temp_path, caption="Uploaded Image", use_container_width=True)

        st.info("Matching product...")

        query_embedding = np.array(get_embedding(temp_path)).flatten()

        best_match = None
        best_score = -1

        for file in os.listdir("embeddings"):

            if file.endswith(".npy"):

                emb = np.load(os.path.join("embeddings", file)).flatten()

                score = np.dot(query_embedding, emb) / (
                    np.linalg.norm(query_embedding) *
                    np.linalg.norm(emb)
                )

                if score > best_score:
                    best_score = score
                    best_match = file.replace(".npy", "")

        if best_match:
            matched_product = best_match
            st.success(f"🎯 Product Found: {best_match}")
            st.info(f"Confidence: {round(best_score, 3)}")

    st.divider()

    # =====================================================
    # SCANNED PRODUCT DETAILS
    # =====================================================

    if matched_product:

        st.subheader("🎯 Product Details")

        found = False

        for _, row in df.iterrows():

            if row["product_name"] == matched_product:

                found = True

                st.success(f"📦 {row['product_name']}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Buy Price", f"₹{row['buy_price']}")

                with col2:
                    st.metric("Sell Price", f"₹{row['sell_price']}")

                with col3:
                    st.metric("Stock", row["quantity"])

                st.write(f"🏬 Branch: {row['branch']}")
                st.info(f"Profit per unit: ₹{row['sell_price'] - row['buy_price']}")

        if not found:
            st.error("Product not found in database")

    st.divider()

    # =====================================================
    # BUSINESS DASHBOARD
    # =====================================================

    st.markdown("## 📊 Business Overview")

    total_products = len(df)
    total_stock = df["quantity"].sum()
    revenue = (df["sell_price"] * df["quantity"]).sum()
    cost = (df["buy_price"] * df["quantity"]).sum()
    profit = revenue - cost
    margin = (profit / revenue) * 100 if revenue > 0 else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products", total_products)
    col2.metric("Stock", total_stock)
    col3.metric("Revenue", f"₹{revenue:,.0f}")
    col4.metric("Margin", f"{margin:.2f}%")

    st.divider()

    # =====================================================
    # PROFIT GRAPH
    # =====================================================

    st.markdown("## 📈 Profit Analytics")

    df["profit"] = (df["sell_price"] - df["buy_price"]) * df["quantity"]

    st.bar_chart(df.set_index("product_name")["profit"])