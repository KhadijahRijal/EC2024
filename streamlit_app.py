import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Genetic Algorithm", divider="gray")


# --- ASSUMING 'arts_df' IS LOADED HERE ---
# For demonstration, creating a dummy arts_df
# Replace this section with your actual data loading
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100, p=[0.45, 0.55])
}
arts_df = pd.DataFrame(data)
# --- END OF DUMMY DATA ---

# Count the occurrences of each gender in the arts_df
arts_gender_counts = arts_df['Gender'].value_counts().reset_index()
arts_gender_counts.columns = ['Gender', 'Count']

# Create a bar chart using Plotly Express
fig = px.bar(
    arts_gender_counts,
    x='Gender',
    y='Count',
    title='Gender Distribution in Arts Faculty',
    color='Gender', # Optional: to color bars by gender
    labels={'Count': 'Number of Students'} # Optional: custom axis label
)

# Display the Plotly figure in Streamlit
st.title("Arts Faculty Data Visualization")
st.plotly_chart(fig, use_container_width=True)
