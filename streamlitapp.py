import streamlit as st
import seaborn as sns
import plotly.express as px

# --- Custom Styling (Background, Fonts, etc.) ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #FF7E5F, #feb47b);  /* Gradient background */
            color: #fff;  /* White text */
            font-family: 'Helvetica', sans-serif;  /* Clean font */
        }
        .main {
            padding-top: 5rem;  /* Padding to push the content down */
            padding-bottom: 5rem;
        }
        .stTitle {
            font-size: 2.5rem;  /* Larger title */
            font-weight: 600;
        }
        .stSubheader {
            font-size: 1.5rem;  /* Larger subheader */
            color: #ffffff;
        }
        .stMarkdown {
            font-size: 1.1rem;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #FF7E5F;  /* Button color */
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .plotly-graph-div {
            border-radius: 15px;  /* Rounded corners for plots */
            padding: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("✨ Interactive Visualizations with Plotly ✨")

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
fig1.update_layout(
    title_x=0.5,  # Center the title
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
)
st.plotly_chart(fig1)

# --- Task 2: Scatter Plot ---
st.subheader("Total Bill vs Tip (by Gender)")
fig2 = px.scatter(
    tips, x='total_bill', y='tip', color='sex',
    title='Total Bill vs Tip (by Gender)',
    labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark',  # Dark background for contrast
    size='size',  # Points sized by party size
)
fig2.update_layout(
    title_x=0.5,  # Center the title
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
)
st.plotly_chart(fig2)

# --- Button for Interactivity ---
if st.button("Show More Information"):
    st.markdown("### More Fun Visualizations Coming Soon!")
    st.markdown("""
        This app demonstrates the power of **Plotly** and **Streamlit**. With more visualizations and customization, you'll be able to explore data in an exciting way!
    """)
