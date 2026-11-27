import streamlit as st

st.set_page_config(
    layout="wide"
)


page = st.navigation(
  [
    st.Page("app_pages/overview_p1.py", title = "Overview", icon = "ℹ️"),
    st.Page("app_pages/risk_heatmap_p2.py", title = "Risk Heatmap", icon = "📈"),
    st.Page("app_pages/sector_lookup.py", title = "Data Lookup by Sector", icon = "🔎")

  ]
)

page.run()