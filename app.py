import streamlit as st

st.set_page_config(
    page_title="QuickRate AI",
    page_icon="📦",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f1117;
    color: white;
}
section[data-testid="stSidebar"] {
    background-color: #11131a;
}
.stButton button {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("📦 QuickRate AI SaaS")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Inventory",
        "Scan Product",
        "AI Pricing Engine",
        "Analytics"
    ]
)

if page == "Dashboard":
    from pages.dashboard import app
    app()

elif page == "Inventory":
    from pages.inventory import app
    app()

elif page == "Scan Product":
    from pages.scan import app
    app()

elif page == "AI Pricing Engine":
    from pages.pricing_ai import app
    app()

elif page == "Analytics":
    from pages.analytics import app
    app()