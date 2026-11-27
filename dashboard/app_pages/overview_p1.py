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

# ------------------ This month vs last month -------------------
dates = sorted(hist["date"].unique())
latest_d, prev_d = dates[-1], dates[-2] # last date and second to last

cur = hist[hist["date"] == latest_d].set_index("division")
prv = hist[hist["date"] == prev_d].set_index("division")

# Build table
table = cur[["prob", "tier"]].copy()
table["chg"] = cur["prob"] - prv["prob"] # this month's prob vs last months
table["prev_tier"] = prv["tier"]

table = (table.join(names.set_index("division")) # adds sector name
            .join(feats[feats["date"] == latest_d].set_index("division")[["growth_yoy", "yoy_roll_6"]]) # adds this months YOY growth and 6-month average
            .sort_values("prob", ascending=False) # puts the riskiest sector first
            .reset_index()) # turns division from the index back into an ordinary column

# ---- Page ------
st.title("Early-Warning for Manufacturing Sectors")
st.caption(f"As of {pd.Timestamp(latest_d): %B %Y}. "
            "Risk of distress six months ahead, by manufacturing sector.")

n_high = (table["tier"] == "High").sum()
n_watch = (table["tier"] == "Watch").sum()
n_low = (table["tier"] == "Low").sum()
new_high = ((table["tier"] == "High") & (table["prev_tier"] != "High")).sum()
left_high = ((table["prev_tier"] == "High") & (table["tier"] != "High")).sum()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("High", n_high, border = True)
c2.metric("Watch", n_watch, border = True)
c3.metric("Low", n_low, border = True)
c4.metric("New High this month", new_high, border = True)
c5.metric("Dropped out of High", left_high, border = True)

st.subheader("Sector watchlist")

def colour(v):
    return {"High": "background-color: #8B0000",
            "Watch": "background-color: #BA8E23",
            "Low": "background-color: #06402B"}.get(v, "")

show = table[["name", "tier", "prob", "chg", "growth_yoy", "yoy_roll_6"]].rename(columns={
    "name": "Sector", 
    "tier": "Tier", 
    "prob": "Risk",
    "chg": "Change vs last month", 
    "growth_yoy": "YoY growth (%)",
    "yoy_roll_6": "6-month average YoY (%)"})

st.dataframe(
    show.style.map(colour, subset=["Tier"]) 
        .format({"Risk": "{:.3f}", "Change vs last month": "{:+.3f}",
                "YoY growth (%)": "{:.1f}", "6-month avg YoY (%)": "{:.1f}"}),
    hide_index=True, use_container_width=True)

st.caption("In the backtest, about 1 in 5 High flags was followed by distress, "
        "compared with about 1 in 11 by chance. Treat it as a screening tool, "
        "not a forecast.")