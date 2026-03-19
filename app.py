import streamlit as st
import pandas as pd
from query import search_query

st.set_page_config(page_title="Endee AI Ads Assistant", layout="wide")

st.title("Endee AI Ads Assistant")
st.write("Semantic search over Social Network Ads data stored in Endee.")

try:
    df = pd.read_csv("Social_Network_Ads.csv")
except Exception as e:
    st.error(f"Could not load Social_Network_Ads.csv: {e}")
    st.stop()

st.sidebar.header("Analytics")
chart_option = st.sidebar.selectbox(
    "Choose a graph",
    [
        "Gender Distribution",
        "Purchase Distribution",
        "Age Distribution",
        "Estimated Salary Distribution",
        "Average Age by Purchase",
        "Average Salary by Purchase",
    ],
)

st.subheader("Data Visualization")

if chart_option == "Gender Distribution":
    chart_data = df["Gender"].value_counts()
    st.bar_chart(chart_data)

elif chart_option == "Purchase Distribution":
    chart_data = df["Purchased"].value_counts()
    chart_data.index = ["Not Purchased", "Purchased"]
    st.bar_chart(chart_data)

elif chart_option == "Age Distribution":
    chart_data = df["Age"].value_counts().sort_index()
    st.bar_chart(chart_data)

elif chart_option == "Estimated Salary Distribution":
    chart_data = df["EstimatedSalary"]
    st.line_chart(chart_data)

elif chart_option == "Average Age by Purchase":
    chart_data = df.groupby("Purchased")["Age"].mean()
    chart_data.index = ["Not Purchased", "Purchased"]
    st.bar_chart(chart_data)

elif chart_option == "Average Salary by Purchase":
    chart_data = df.groupby("Purchased")["EstimatedSalary"].mean()
    chart_data.index = ["Not Purchased", "Purchased"]
    st.bar_chart(chart_data)

st.divider()

st.subheader("Ask a Question")
user_query = st.text_input("Type your query here")

if user_query:
    try:
        results = search_query(user_query)
        st.subheader("Results")
        if results:
            for r in results:
                st.write("-", r)
        else:
            st.info("No matching results found.")
    except Exception as e:
        st.error(f"Query failed: {e}")