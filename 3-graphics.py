import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

# Widget 1: pick a state
state = st.selectbox("Select a State:", df["State"].unique())

# Widget 2: pick what to graph
demographic = st.selectbox(
    "Select a demographic:",
    ["Total Population", "Median Household Income"],
)

# Filter to the selected state (keep ALL years for the trend line)
mask = df["State"] == state
df_state = df[mask]

# Build the line graph
fig = px.line(
    df_state,
    x="Year",
    y=demographic,
    title=f"{demographic} of {state} over Time",
)

st.plotly_chart(fig)
