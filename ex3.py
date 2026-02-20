import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Example 3")

# Create dataframe
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
})

# Make sure Category is treated as categorical in correct order
df["Category"] = pd.Categorical(
    df["Category"],
    categories=["A", "B", "C", "D"],
    ordered=True
)

# Create bar chart
fig = px.bar(
    df,
    x="Category",
    y="Values",
    category_orders={"Category": ["A", "B", "C", "D"]}
)

st.plotly_chart(fig)
