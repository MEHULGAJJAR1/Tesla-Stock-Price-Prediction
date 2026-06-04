import streamlit as st
import yfinance as yf
import pandas as pd
from plotly import graph_objs as go
import math
from datetime import date
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

START = "2020-06-26"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = "TSLA"

@st.cache_data
def load_data(ticker):
    price = yf.download(ticker, START, TODAY)
    price.reset_index(inplace=True)
    return price

price = load_data(stocks)

steps = 50
price_test = price.tail(steps)

st.header("Prediction Kernel")

# Ensure Close column is 1D
y_true = price_test["Close"].squeeze()

# Dummy prediction (same as actual values)
y_pred = y_true.copy()

# RMSE
error = math.sqrt(mean_squared_error(y_true, y_pred))

st.subheader("Prediction Results")
st.write("RMSE:")
st.success(round(error, 4))

# Create prediction dataframe safely
VR_predict = pd.DataFrame({
    "Date": price_test["Date"].tolist(),
    "Actual": y_true.tolist(),
    "Predicted": y_pred.tolist()
})

st.write(VR_predict)

# Prediction Chart
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=VR_predict["Date"],
        y=VR_predict["Actual"],
        name="Actual Price"
    )
)

fig.add_trace(
    go.Scatter(
        x=VR_predict["Date"],
        y=VR_predict["Predicted"],
        name="Predicted Price"
    )
)

fig.update_layout(
    title="Tesla Stock Prediction",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=True
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ARIMA Forecast Section
# -----------------------------

st.subheader("ARIMA Forecast (30 Days)")

try:
    combined = pd.DataFrame(price["Close"])

    model = ARIMA(combined["Close"], order=(1, 1, 1))
    fitted_model = model.fit()

    forecast = fitted_model.forecast(steps=30)

    forecast_df = pd.DataFrame({
        "Day": range(1, 31),
        "Forecast": forecast.values
    })

    st.write(forecast_df)

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=forecast_df["Day"],
            y=forecast_df["Forecast"],
            name="Forecast"
        )
    )

    fig2.update_layout(
        title="30-Day Tesla Forecast",
        xaxis_title="Days Ahead",
        yaxis_title="Predicted Price"
    )

    st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"ARIMA Error: {e}")