import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./vehicles_us.csv')

st.header("Car Advertisement Dashboard")

fig_hist = px.histogram(df, x='type')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(df, x='model_year', y='condition')  # Adjust column names
st.plotly_chart(fig_scatter)

show_histogram = st.checkbox("Show Histogram")
if show_histogram:
    st.plotly_chart(fig_hist)


