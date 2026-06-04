import streamlit as st
import pandas as pd

st.title("📊 CSV Data Analyzer")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    option = st.sidebar.selectbox(
        "Choose Option",
        [
            "Preview Data",
            "Dataset Summary",
            "Missing Values",
            "Statistics",
            "Columns",
            "Correlation Matrix"
        ]
    )

    if option == "Preview Data":
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

    elif option == "Dataset Summary":
        st.subheader("Dataset Summary")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

    elif option == "Missing Values":
        st.subheader("Missing Values")
        st.write(df.isnull().sum())

    elif option == "Statistics":
        st.subheader("Statistics")
        st.write(df.describe())

    elif option == "Columns":
        st.subheader("Columns")
        st.write(df.columns.tolist())

    elif option == "Correlation Matrix":
        st.subheader("Correlation Matrix")
        st.write(df.corr(numeric_only=True))
else:
    st.info("Upload a CSV file from the sidebar.")