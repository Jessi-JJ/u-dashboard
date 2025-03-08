import streamlit as st
import plotly.express as px
import pandas as pd

udash = pd.read_csv('university_student_dashboard_data.csv')

# Title
st.title("University Student Admissions Dashboard")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(udash["Year"].min()), int(udash["Year"].max()), int(udash["Year"].min()))

# Filter data based on the selected year
filtered_udash = udash[udash.Year == selected_year]

# KPIs
st.header("Key Performance Indicators")

# Group by Term
for term, group in filtered_udash.groupby("Term"):
    st.header(f"Term: {term}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", f"{group['Applications'].sum():,}")
    col2.metric("Total Admitted", f"{group['Admitted'].sum():,}")
    col3.metric("Total Enrolled", f"{group['Enrolled'].sum():,}")
