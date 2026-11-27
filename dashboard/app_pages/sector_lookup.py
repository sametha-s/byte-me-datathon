import streamlit as st
import pandas as pd

from pathlib import Path


DATA = Path(__file__).parent.parent   # the folder that app.py lives in

@st.cache_data
def load():
    hist = pd.read_parquet(DATA / "risk_history.parquet")
    feats = pd.read_parquet(DATA / "features.parquet")
    names = pd.read_csv(DATA / "division_names.csv", dtype={"division": str})
    return hist, feats, names

hist, feats, names = load()

# ----- Page ------
st.title("Data Lookup by Sector")

st.caption("View the year-on-year growth, 6-month average growth and if the sector is in distress of all months of a specified sector.")
st.caption("Data from January 2015 to September 2026")

choice = st.selectbox("Select Sector", options = [
  "Food products",
  "Beverages",
  "Tobacco products",
  "Textiles",
  "Wearing apparel",
  "Leather and related products",
  "Wood, products of wood and cork, except furniture",
  "Paper and paper products",
  "Printing and reproduction of recorded media",
  "Coke and refined petroleum products",
  "Chemicals and chemical products",
  "Pharmaceutical products and preparations",
  "Rubber and plastic products",
  "Non-metallic mineral products",
  "Basic metals",
  "Fabricated metal products, except machinery and equipment",
  "Computer, electronic and optical products",
  "Electrical equipment",
  "Machinery and equipment",
  "Motor vehicles, trailers and semi-trailers",
  "Other transport equipment",
  "Furniture",
  "Other manufacturing",
  "Repair and installation of machinery and equipment"
])

rm_na = st.checkbox("Remove Missing Values?", value = False)

if rm_na:
  feats_copy = feats.dropna().copy()
else:
  feats_copy = feats.copy()

feats_copy["date"] = feats_copy["date"].dt.strftime("%B %Y")
feats_copy["distress"] = feats_copy["distress"].map({0: "No", 1: "Yes"})

sec_choice_df = feats_copy.merge(
  names,
  on = "division",
  how = "left",
  validate = "m:1"
)

filtered_df = sec_choice_df[sec_choice_df["name"] == choice]
display_df = filtered_df[["date", "name", "growth_yoy", "yoy_roll_6", "distress"]].rename(columns = {
  "date": "Month",
  "name": "Sector",
  "growth_yoy": "YoY Growth (%)",
  "yoy_roll_6": "6-month Average YoY (%)",
  "distress": "Is the sector in distress?"})

st.dataframe(display_df)

st.caption("Some rows have missing values due to limited information. "
            "Year-on-year growth (YoY Growth (%)) requires the same month in the previous year, " 
            "so it is undefined for the first 12 months of each sector (January – December 2015).")