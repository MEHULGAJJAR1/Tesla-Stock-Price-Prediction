import streamlit as st
import pandas as pd
from plotly import graph_objs as go

st.set_page_config(
    page_title="TSLA Price Prediction",
    page_icon="🚗"
)

st.title("TSLA Price Prediction 🚗⚡🔋")

# Load Local CSV
@st.cache_data
def load_data():
    price = pd.read_csv("TSLA.csv")

    price["Date"] = pd.to_datetime(price["Date"])
    price = price.sort_values("Date")

    return price

price = load_data()

st.subheader("Tesla Stock Data")
st.write(price.tail())

if st.checkbox("Data Description"):
    st.write(price.describe())

# Tesla Open vs Close
fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Open"],
        name="Open Price"
    )
)

fig1.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Close"],
        name="Close Price"
    )
)

fig1.update_layout(
    title="Tesla Stock Movement",
    xaxis_rangeslider_visible=True
)

st.plotly_chart(fig1, use_container_width=True)

# Moving Average
fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Close"],
        name="Close Price"
    )
)

fig2.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Close"].rolling(30).mean(),
        name="30 Day MA"
    )
)

fig2.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Close"].rolling(60).mean(),
        name="60 Day MA"
    )
)

fig2.update_layout(
    title="Tesla Moving Averages",
    xaxis_rangeslider_visible=True
)

st.plotly_chart(fig2, use_container_width=True)

# High vs Low
fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["High"],
        name="High Price"
    )
)

fig3.add_trace(
    go.Scatter(
        x=price["Date"],
        y=price["Low"],
        name="Low Price"
    )
)

fig3.update_layout(
    title="Tesla High vs Low Price",
    xaxis_rangeslider_visible=True
)

st.plotly_chart(fig3, use_container_width=True)

# Metrics
st.subheader("Tesla Stock Metrics")

latest_close = round(float(price["Close"].iloc[-1]), 2)
highest_price = round(float(price["High"].max()), 2)
lowest_price = round(float(price["Low"].min()), 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Latest Close", latest_close)

with col2:
    st.metric("Highest Price", highest_price)

with col3:
    st.metric("Lowest Price", lowest_price)

# Volume Chart
st.subheader("Trading Volume")

fig4 = go.Figure()

fig4.add_trace(
    go.Bar(
        x=price["Date"],
        y=price["Volume"],
        name="Volume"
    )
)

fig4.update_layout(
    title="Tesla Trading Volume"
)

st.plotly_chart(fig4, use_container_width=True)

st.success("Tesla Dashboard Loaded Successfully ✅")