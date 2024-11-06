import streamlit as st
import seaborn as sns
import plotly.express as px

# --- Title ---
st.title("Interactive Visualizations with Plotly")

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset

# Display the first few rows of the dataset
st.write("### Dataset Overview")
st.write(tips.head())

# --- Task 1: Bar Chart ---
st.subheader("Average Tip by Day")
fig1 = px.bar(
    tips, 
    x='day', y='tip', color='day',
    title='Average Tip by Day', 
    labels={'tip': 'Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'  # Clean white background
)
st.plotly_chart(fig1)

# --- Task 2: Scatter Plot ---
st.subheader("Total Bill vs Tip (by Gender)")
fig2 = px.scatter(
    tips, x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip (by Gender)',
    labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark',  # Dark background for contrast
    size='size'  # Points sized by party size
)
st.plotly_chart(fig2)
