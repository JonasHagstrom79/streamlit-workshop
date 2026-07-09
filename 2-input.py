import streamlit as st
import pandas as pd

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

# Widget 1: pick a state
option = st.selectbox("Select a state:", df["State"].unique())

# Widget 2: pick a single year
year = st.slider("Select a year:", 2005, 2023, 2020)

st.write("You selected:", option, "in", year)

# Filter on both state and year
df = df[df["State"] == option]
df = df[df["Year"] == year]

st.dataframe(df)
