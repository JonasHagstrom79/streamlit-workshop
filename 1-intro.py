import streamlit as st
import pandas as pd

df = pd.read_csv("state_data.csv")

st.dataframe(df)
