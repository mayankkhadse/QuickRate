import streamlit as st
import sqlite3

def app():
    st.title("Sales Intelligence")

    conn = sqlite3.connect("database/inventory.db")
    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM products").fetchall()
    total_value = sum([r[3] * r[4] for r in rows]) if rows else 0

    st.metric("Total Inventory Value", f"₹{total_value:,.2f}")

    if rows:
        st.subheader("Sales Data")
        st.write(rows)
    else:
        st.warning("No products found.")
