import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Load sample data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

# Define the different chart types
candlestick = go.Candlestick(x=df['Date'], open=df['AAPL.Open'], high=df['AAPL.High'], low=df['AAPL.Low'], close=df['AAPL.Close'])
line = go.Scatter(x=df['Date'], y=df['AAPL.Close'], mode='lines', name='Close')

# Add a sidebar with a checkbox to select chart type
chart_type = st.sidebar.checkbox("Select chart type", True, key="chart_type")
if chart_type:
    fig = go.Figure(candlestick)
else:
    fig = go.Figure(line)

# Plot the figure
st.plotly_chart(fig)
