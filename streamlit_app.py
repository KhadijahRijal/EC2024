import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# --- ASSUMING 'arts_df' IS LOADED HERE ---
# For demonstration, creating a dummy arts_df
# Replace this section with your actual data loading
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100, p=[0.32, 0.68])
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
    'Gender': np.random.choice(['Male', 'Female'], size=100, p=[0.61, 0.39])
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


# --- Start of Streamlit App Code ---

st.title("S.S.C (GPA) Distribution Histogram")

# **Dummy DataFrame Creation**
# *Replace this entire block with your actual data loading and setup*
# *e.g., arts_df = pd.read_csv('arts_data.csv')*
np.random.seed(42)
data = {
    'S.S.C (GPA)': np.random.normal(loc=4.5, scale=0.8, size=200)
}
arts_df = pd.DataFrame(data)
# -----------------------------------

# 1. Create the figure and axes objects explicitly
fig, ax = plt.subplots(figsize=(8, 6))

# 2. Use Seaborn to create the histogram on the specific axis (ax)
sns.histplot(
    data=arts_df,
    x='S.S.C (GPA)',
    kde=True,
    ax=ax # IMPORTANT: Pass the axis object to the seaborn function
)

# 3. Set the title and labels using the axis object
ax.set_title('Distribution of S.S.C (GPA) in Arts Faculty')
ax.set_xlabel('S.S.C (GPA)')
ax.set_ylabel('Frequency')

# 4. Display the figure using Streamlit
st.pyplot(fig)


# --- Start of Streamlit App Code ---

st.title("Academic Year Distribution by Gender")

# **Dummy DataFrame Creation**
# *Replace this entire block with your actual data loading and setup*
# *e.g., arts_df = pd.read_csv('arts_data.csv')*
np.random.seed(42)
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4']
genders = ['Male', 'Female']
data = {
    'Bachelor  Academic Year in EU': np.random.choice(years, size=300, p=[0.3, 0.25, 0.2, 0.25]),
    'Gender': np.random.choice(genders, size=300, p=[0.48, 0.52])
}
arts_df = pd.DataFrame(data)
# -----------------------------------

# Group the data by 'Bachelor Academic Year in EU' and 'Gender' and count occurrences
# Note: The column name has spaces, which is handled correctly by the groupby and plotting functions.
academic_year_gender_counts = arts_df.groupby(['Bachelor  Academic Year in EU', 'Gender']).size().reset_index(name='Count')

# 1. Create the figure and axes objects explicitly
fig, ax = plt.subplots(figsize=(12, 6))

# 2. Use Seaborn to create the bar plot on the specific axis (ax)
sns.barplot(
    data=academic_year_gender_counts,
    x='Bachelor  Academic Year in EU',
    y='Count',
    hue='Gender',
    ax=ax # IMPORTANT: Pass the axis object to the seaborn function
)

# 3. Set the title, labels, and rotations using the axis object
ax.set_title('Distribution of Bachelor Academic Year in Arts Faculty by Gender')
ax.set_xlabel('Bachelor Academic Year in EU')
ax.set_ylabel('Count')

# Rotate x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Adjust layout to prevent labels from being cut off
fig.tight_layout()

# 4. Display the figure using Streamlit
st.pyplot(fig)
