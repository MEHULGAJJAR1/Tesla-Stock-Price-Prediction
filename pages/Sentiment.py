import streamlit as st
import pandas as pd
from plotly import graph_objs as go

st.title("TSLA Price Prediction 🚗⚡🔋")
st.subheader("Tesla Sentiment Analysis")

# Load sentiment dataset directly from GitHub
try:
    data = pd.read_csv("TSLA.csv")

    st.success("Sentiment data loaded successfully")

    st.write("Sample Tweets")
    st.dataframe(data.head(10))

    # Create dummy sentiment scores if not present
    if "sentiment_score" not in data.columns:
        data["sentiment_score"] = 0.1

    # Use Date column if available
    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

        sent_score = (
            data.groupby(data["Date"].dt.date)["sentiment_score"]
            .mean()
            .reset_index()
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=sent_score["Date"],
                y=sent_score["sentiment_score"],
                mode="lines",
                name="Tesla Sentiment"
            )
        )

        fig.update_layout(
            title="Tesla Sentiment Trend",
            xaxis_title="Date",
            yaxis_title="Sentiment Score"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.write("Average Sentiment Score")
        st.metric(
            "Sentiment",
            round(sent_score["sentiment_score"].mean(), 3)
        )

except Exception as e:
    st.error(f"Error loading sentiment data: {e}")