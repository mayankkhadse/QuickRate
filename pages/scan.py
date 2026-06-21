import streamlit as st
import os
import numpy as np
import sqlite3

from services.vision_service import get_embedding


def app():

    st.title("📸 Scan Product")

    uploaded = st.file_uploader(
        "Upload Product Photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:

        temp_path = "temp_scan.jpg"

        with open(temp_path, "wb") as f:
            f.write(uploaded.getbuffer())

        query_embedding = get_embedding(temp_path)

        best_score = -1
        best_product = None

        for file in os.listdir("embeddings"):

            saved_embedding = np.load(
                os.path.join("embeddings", file)
            )

            score = np.dot(
                query_embedding,
                saved_embedding.T
            )[0][0]

            if score > best_score:
                best_score = score
                best_product = file.replace(".npy", "")

        if best_product is None:
            st.error("No matching product found")
            return

        conn = sqlite3.connect(
            "database/inventory.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM products
            WHERE product_name=?
            """,
            (best_product,)
        )

        row = cursor.fetchone()

        if row:

            st.success("Product Identified")

            st.write("### Product Details")

            st.write("**Product Name:**", row[1])
            st.write("**Selling Price:** ₹", row[3])
            st.write("**Quantity:**", row[4])
            st.write("**Branch:**", row[5])

        else:
            st.error("Product not found in database")