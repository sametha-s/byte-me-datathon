import streamlit as st
import pandas as pd

import plotly.express as px
from pathlib import Path

DATA = Path(__file__).parent.parent

@st.cache_data
def load():
    hist = pd.read_parquet(DATA / "risk_history.parquet")
    names = pd.read_csv(DATA / "division_names.csv", dtype={"division": str})
    return hist, names

hist, names = load()

st.title("Risk heatmap")
st.caption("Each square is one sector in one month. "
        "Darker red means a higher risk of distress six months later.")

df = hist.merge(names, on="division")
grid = df.pivot(index="name", columns="date", values="prob")

# Put the riskiest sectors (in the latest month) at the top
latest_col = grid.columns[-1]
grid = grid.sort_values(latest_col, ascending=False)

# Turn the dates into readable labels like "Sep 2026"
grid.columns = grid.columns.strftime("%b %Y")

# Draw heatmap
fig = px.imshow(grid, aspect="auto", zmin=0, zmax=0.3,
                color_continuous_scale="YlOrRd", labels={"color": "Risk"})
fig.update_xaxes(side="top")
st.plotly_chart(fig, use_container_width=True)

st.caption("Up to March 2026 these scores come from the backtest "
        "(the model had not seen those months). From April 2026 they are live scores.")