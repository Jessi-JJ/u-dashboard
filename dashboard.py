import streamlit as st
import plotly.express as px
import pandas as pd

udash = pd.read_csv('university_student_dashboard_data.csv')

# Title
st.title("University Student Admissions Dashboard")

# Sidebar Filter
st.sidebar.header("Filters")
year_filter = st.sidebar.selectbox("Select Year", ['All'] + list(udash['Year'].unique()))
if year_filter != 'All':
    filtered_udash = udash[udash['Year'] == year_filter]
else:
    filtered_udash = udash

# KPIs
st.header("Key Performance Indicators")

# Group by Term
for term, group in filtered_udash.groupby("Term"):
    st.header(f"Term: {term}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", f"{group['Applications'].sum():,}")
    col2.metric("Total Admitted", f"{group['Admitted'].sum():,}")
    col3.metric("Total Enrolled", f"{group['Enrolled'].sum():,}")
