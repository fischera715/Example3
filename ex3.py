import streamlit as st
import plotly.express as px

st.title("📊 Interactive Dashboard with Multiple Plots")

df = px.data.gapminder()

selected_year = st.sidebar.slider(
    "Select Year:",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].min()),
    step=5
)

filtered_df = df[df["year"] == selected_year]

fig1 = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="Life Expectancy vs GDP"
)

fig2 = px.bar(
    filtered_df,
    x="continent",
    y="pop",
    color="continent",
    title="Population per Continent"
)

fig3 = px.line(
    filtered_df,
    x="country",
    y="gdpPercap",
    color="continent",
    title="GDP Per Capita by Country"
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)
