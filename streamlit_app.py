import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# --- ASSUMING 'arts_df' IS LOADED HERE ---
# For demonstration, creating a dummy arts_df
# Replace this section with your actual data loading
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100, p=[0.40, 0.60])
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


# --- Start of Streamlit App Code ---

st.title("Gender Distribution Pie Chart")

# **Dummy DataFrame Creation**
# *Replace this entire block with your actual data loading and setup*
# *e.g., df = pd.read_csv('your_data.csv')*
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100, p=[0.60, 0.40])
}
df = pd.DataFrame(data)
# -----------------------------------

# Count the occurrences of each gender
gender_counts = df['Gender'].value_counts()

# Create a figure object (Crucial for Streamlit)
fig, ax = plt.subplots(figsize=(6, 6))

# Create the pie chart on the figure's axis
ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=140
)
ax.set_title('Distribution of Gender')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# **Display the figure in Streamlit**
st.pyplot(fig)
