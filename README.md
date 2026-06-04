# 🚗 TSLA Stock Price Prediction Dashboard

An interactive Streamlit-based dashboard for Tesla (TSLA) stock analysis, visualization, sentiment analysis, and price prediction using Machine Learning models.

## Features

### 📊 Home Dashboard

* Tesla historical stock data visualization
* Open vs Close Price analysis
* High vs Low Price comparison
* Moving Average trends (30-Day & 60-Day)
* Trading Volume analysis
* Key stock metrics dashboard

### 📈 Data Analyzer

* CSV file upload support
* Automatic dataset summary
* Statistical analysis
* Missing value detection
* Correlation analysis
* Interactive visualizations

### 🤖 Price Prediction

* Machine Learning based stock price prediction
* Supports trained Pickle models
* OLS Regression Model
* Advanced Prediction Model (Model V2)
* User input based future price estimation

### 💬 Sentiment Analysis

* Tesla-related sentiment analysis
* News sentiment evaluation
* Positive, Negative and Neutral classification

## Dataset

The application uses a local Tesla stock dataset:

* TSLA.csv
* Historical Tesla stock prices
* Date, Open, High, Low, Close, Volume columns

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-Learn
* Pickle
* SNScrape
* TextBlob

## Project Structure

TSLA-STREAMLIT/

├── Home.py

├── Prediction.py

├── Sentiment.py

├── Data_Analyzer.py

├── TSLA.csv

├── model_OLS.pkl

├── modelv2.pkl

├── requirements.txt

└── README.md

## Installation

```bash
git clone <repository-url>
cd TSLA-STREAMLIT
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run Home.py
```

## Models Used

### Model 1

* model_OLS.pkl
* Ordinary Least Squares Regression

### Model 2

* modelv2.pkl
* Enhanced Prediction Model

## Future Improvements

* LSTM Deep Learning Prediction
* Real-Time Stock Updates
* Portfolio Tracking
* Advanced Technical Indicators
* News API Integration

## Author

Mehul Gajjar

Tesla Stock Price Prediction Dashboard using Streamlit and Machine Learning.
