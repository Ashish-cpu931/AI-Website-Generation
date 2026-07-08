# Create a Data Visualization Tool

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Interactive Data Visualization Tool",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Data Visualization Tool")
st.markdown("Upload any dataset and generate interactive visualizations.")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Missing Values")

    missing = df.isnull().sum()

    st.dataframe(missing)

    if st.checkbox("Remove Missing Values"):
        df = df.dropna()
        st.success("Missing values removed.")

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    all_columns = df.columns.tolist()

    chart = st.selectbox(
        "Choose Visualization",
        [
            "Scatter Plot",
            "Line Chart",
            "Bar Chart",
            "Histogram",
            "Box Plot",
            "Pie Chart",
            "Heatmap"
        ]
    )

    if chart != "Heatmap":

        x = st.selectbox("Select X-axis", all_columns)

    if chart in ["Scatter Plot", "Line Chart", "Bar Chart", "Box Plot"]:

        y = st.selectbox("Select Y-axis", numeric_columns)

    if chart == "Scatter Plot":

        fig = px.scatter(
            df,
            x=x,
            y=y,
            color=x,
            title="Scatter Plot"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Line Chart":

        fig = px.line(
            df,
            x=x,
            y=y,
            markers=True,
            title="Line Chart"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Bar Chart":

        fig = px.bar(
            df,
            x=x,
            y=y,
            color=x,
            title="Bar Chart"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Histogram":

        fig = px.histogram(
            df,
            x=x,
            title="Histogram"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Box Plot":

        fig = px.box(
            df,
            x=x,
            y=y,
            color=x,
            title="Box Plot"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Pie Chart":

        values = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        fig = px.pie(
            df,
            names=x,
            values=values,
            title="Pie Chart"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Heatmap":

        st.subheader("Correlation Heatmap")

        corr = df[numeric_columns].corr()

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)

    st.subheader("Download Clean Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="processed_dataset.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a dataset to begin.")