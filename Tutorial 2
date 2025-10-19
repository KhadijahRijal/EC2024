import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt # Needed for creating interactive charts

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# URL of the CSV file
file_url = 'https://raw.githubusercontent.com/KhadijahRijal/EC2024/refs/heads/main/student_survey_exported.csv'

# Use st.cache_data to cache the function's output.
# This prevents Streamlit from re-downloading and re-loading the data 
# every time the app re-runs, making it much faster.
@st.cache_data
def load_data(url):
    """Loads the CSV file from the URL into a pandas DataFrame."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        # Streamlit will display this error message in the app
        st.error(f"An error occurred while loading the data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

# Load the data
df_url = load_data(file_url)

# --- Streamlit App Layout ---

st.title("Student Survey Data Viewer 📊")

# Check if the DataFrame is not empty before attempting to display
if not df_url.empty:
    st.success("CSV file loaded successfully from URL!")

    # Use Streamlit's st.header for a section title
    st.header("First 5 Rows of the DataFrame")
    
    # Use st.dataframe to display the entire DataFrame
    st.dataframe(df_url.head())
    
    st.header("DataFrame Information")
    
    # Display the shape and some info (optional but useful)
    st.write(f"The DataFrame has **{df_url.shape[0]}** rows and **{df_url.shape[1]}** columns.")
    
else:
    st.warning("Could not load data. Please check the URL and your connection.")

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


# --- Streamlit App Code ---

st.title("Academic Year Distribution Violin Plot")

# --- Dummy Data Setup (Replace with your actual data loading) ---
# Create a dummy DataFrame arts_df for demonstration
np.random.seed(42)
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4']
data = {
    'Bachelor  Academic Year in EU': np.random.choice(years, size=300, p=[0.3, 0.25, 0.2, 0.25]),
    # Adding a dummy numerical variable that might be used in a real-world violin plot
    'Numerical_Score': np.random.normal(loc=75, scale=10, size=300)
}
arts_df = pd.DataFrame(data)
# -----------------------------------------------------------------

# 1. Create the figure and axes objects explicitly
fig, ax = plt.subplots(figsize=(10, 6))

# 2. Use Seaborn to create the violin plot, passing the axis object
sns.violinplot(
    data=arts_df,
    x='Bachelor  Academic Year in EU',
    ax=ax # <--- Crucial step: Directs the plot to the figure's axis
)

# 3. Set the title and labels using the axis object
ax.set_title('Distribution of Bachelor Academic Year in Arts Faculty')
ax.set_xlabel('Bachelor Academic Year in EU')
ax.set_ylabel('Density')

# Adjust layout to prevent clipping
fig.tight_layout()

# 4. Display the figure using Streamlit
st.pyplot(fig)


# --- 1. Data Loading and Caching ---
file_url = 'https://raw.githubusercontent.com/KhadijahRijal/EC2024/refs/heads/main/student_survey_exported.csv'

@st.cache_data
def load_data(url):
    """Loads the CSV file from the URL into a pandas DataFrame."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()

df_raw = load_data(file_url)

# --- 2. Data Preparation and Sanitization ---
# Define the expected columns based on your analysis
EXPECTED_ACADEMIC_YEAR_COL = 'Bachelor Academic Year in EU'
EXPECTED_GENDER_COL = 'Gender'

df = df_raw.copy()

# Define custom year order for all academic year charts
YEAR_ORDER = ['Year 1', 'Year 2', 'Year 3', 'Year 4+']

# Ensure data structure is robust for analysis steps (Handles potential missing/renamed columns)
if EXPECTED_ACADEMIC_YEAR_COL not in df.columns:
    st.warning(f"Column '{EXPECTED_ACADEMIC_YEAR_COL}' not found. Using dummy data for structure.")
    df[EXPECTED_ACADEMIC_YEAR_COL] = np.random.choice(YEAR_ORDER, size=len(df))
if EXPECTED_GENDER_COL not in df.columns:
    st.warning(f"Column '{EXPECTED_GENDER_COL}' not found. Using dummy data for structure.")
    df[EXPECTED_GENDER_COL] = np.random.choice(['Female', 'Male', 'Other'], size=len(df))

# Clean up whitespace in column data
for col_name in [EXPECTED_ACADEMIC_YEAR_COL, EXPECTED_GENDER_COL]:
    if col_name in df.columns:
        df[col_name] = df[col_name].astype(str).str.strip()


# --- 3. Key Insight Text Definitions ---
INSIGHT_TEXTS = {
    1: "This analysis shows the distribution of students across academic years, segmented by gender. This is vital for understanding demographic balance throughout the program's lifecycle and ensuring equitable engagement.",
    2: "The overall gender balance in the survey population provides crucial context for all other analyses, highlighting the primary gender representation within the sample group.",
    3: "Identifying which academic years have the highest representation in the survey can indicate potential sampling bias or confirm an intentional focus on specific undergraduate phases (e.g., higher response rates from first-year students).",
    4: "This analysis visualizes the concentration of respondents across the academic years. The height of the bar (or the density peak in a violin plot) confirms where the majority of survey responses are concentrated, which is essential for assessing sample representativeness."
}


# --- 4. Streamlit Application Layout ---

st.set_page_config(layout="wide")

st.title("Student Survey Demographic Insights")
st.markdown("---")

if df.empty:
    st.error("Cannot display insights because the data could not be loaded or is empty.")
else:
    st.header("Key Findings: Gender and Academic Year Distribution")

    # -----------------------------------------------------
    # INSIGHT 1: Academic Year Breakdown by Gender (Grouped Bar Chart)
    # -----------------------------------------------------
    st.subheader("1. Academic Year Breakdown by Gender 👫")
    st.info(f"Insight: {INSIGHT_TEXTS[1]}") 
    
    # Analysis and Chart Generation for Insight 1
    academic_year_gender_counts = df.groupby([EXPECTED_ACADEMIC_YEAR_COL, EXPECTED_GENDER_COL]).size().reset_index(name='Count')
    academic_year_gender_counts.columns = ['AcademicYear', 'Gender', 'Count']
    
    chart1 = alt.Chart(academic_year_gender_counts).mark_bar().encode(
        # Use the custom order for the X-axis
        x=alt.X('AcademicYear', sort=YEAR_ORDER, title='Academic Year in EU'),
        y=alt.Y('Count', title='Number of Students'),
        # Hue encodes the gender
        color='Gender',
        tooltip=['AcademicYear', 'Gender', 'Count']
    ).properties(
        title="Distribution of Academic Year by Gender"
    ).interactive()
    
    st.altair_chart(chart1, use_container_width=True)
    st.markdown("---")

    # -----------------------------------------------------
    # INSIGHT 2: Overall Gender Split (Donut Chart)
    # -----------------------------------------------------
    st.subheader("2. Overall Gender Split 🚻")
    st.info(f"Insight: {INSIGHT_TEXTS[2]}") 
    
    # Analysis and Chart Generation for Insight 2
    gender_counts = df[EXPECTED_GENDER_COL].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    
    chart2 = alt.Chart(gender_counts).mark_arc(innerRadius=80, outerRadius=120).encode(
        theta=alt.Theta(field="Count", type="quantitative"),
        color=alt.Color(field="Gender", type="nominal"),
        order=alt.Order(field="Count", sort="descending"),
        tooltip=["Gender", "Count"]
    ).properties(
        title="Overall Gender Distribution"
    )
    
    st.altair_chart(chart2, use_container_width=False)
    st.markdown("---")

    # -----------------------------------------------------
    # INSIGHT 3 & 4 (Setup): Academic Year Enrollment Focus / Response Density (Simple Bar Chart)
    # -----------------------------------------------------
    # Analysis and Chart Generation for Insights 3 & 4 (reuse the same data/chart)
    year_counts = df[EXPECTED_ACADEMIC_YEAR_COL].value_counts().reset_index()
    year_counts.columns = ['AcademicYear', 'Count']

    chart3 = alt.Chart(year_counts).mark_bar().encode(
        # Use the custom order for the X-axis
        x=alt.X('AcademicYear', sort=YEAR_ORDER, title='Academic Year in EU'),
        y=alt.Y('Count', title='Number of Students'),
        tooltip=['AcademicYear', 'Count'],
        color=alt.Color('AcademicYear', legend=None)
    ).properties(
        title="Count of Students by Academic Year"
    ).interactive()
    
    # -----------------------------------------------------
    # INSIGHT 3: Academic Year Enrollment Focus
    # -----------------------------------------------------
    st.subheader("3. Academic Year Enrollment Focus 📅")
    st.info(f"Insight: {INSIGHT_TEXTS[3]}") 
    
    st.altair_chart(chart3, use_container_width=True)
    st.markdown("---")
    
    # -----------------------------------------------------
    # INSIGHT 4: Analysis of Response Density by Academic Year
    # -----------------------------------------------------
    st.subheader("4. Analysis of Response Density 📉")
    st.info(f"Insight: {INSIGHT_TEXTS[4]}") 
    
    # Reusing chart3 as it visualizes the frequency density for this categorical data
    st.altair_chart(chart3, use_container_width=True)
    st.markdown("---")
