#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 1: Interactive Bar Chart ---
st.subheader("Task 1: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='average tip by day',
    labels={'tip': 'Average tip(s)', 'day': 'Day of the Week'},
    template='plotly_white', #clean white backrground
)


st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 2: Interactive Scatter Chart
fig4 = px.scatter(
    tips, x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip(colored by Gender)',
    labels={'total_bill': 'total bill($)', 'tip': 'Tip($)'},
    template='plotly_dark', #cool dark backrground
    size='size' #the size of points based on the group
)

st.plotly_chart(fig4)  # Display the chart in Streamlit
