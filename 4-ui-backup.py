import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

# --- UI Options: 3 select boxes side by side in columns ---
col1, col2, col3 = st.columns(3)
with col1:
    state = st.selectbox("Select a State:", df["State"].unique())
with col2:
    demographic = st.selectbox(
        "Select a Demographic:", ["Total Population", "Median Household Income"]
    )
with col3:
    year = st.selectbox("Select a Year:", df["Year"].unique())

# --- Prepare the data ---
df_state = df[df["State"] == state]
df_year = df[df["Year"] == year]

# --- 3 visualizations in 3 tabs ---
graph_tab, map_tab, table_tab = st.tabs(["📈 Graph", "🗺️ Map", "📋 Table"])

with graph_tab:
    fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
    st.plotly_chart(fig)

with map_tab:
    fig = px.choropleth(
        df_year,
        locations="State Abbrev",
        locationmode="USA-states",
        color=demographic,
        scope="usa",
        title=f"{demographic} for {year}",
        color_continuous_scale="viridis",
    )
    st.plotly_chart(fig)

with table_tab:
    st.dataframe(df)
