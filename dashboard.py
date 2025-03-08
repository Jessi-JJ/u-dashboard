import streamlit as st
import plotly.express as px
import pandas as pd

udash = pd.read_csv('university_student_dashboard_data.csv')

col1, col2 = st.columns([1, 4])  # Adjust column widths as needed

with col1: #Logo
    st.image("SUNY-Poly-vertical-logo.png", width=250)

with col2: # Title
    st.title("Student Admissions Dashboard")

# Sidebar Filter
st.sidebar.header("Filters")
year_filter = st.sidebar.selectbox("Select Year", ['All'] + list(udash['Year'].unique()))
if year_filter != 'All':
    filtered_udash = udash[udash['Year'] == year_filter]
else:
    filtered_udash = udash

term_filter = st.sidebar.selectbox("Select Term", ['All'] + list(filtered_udash['Term'].unique()))
if term_filter != 'All':
    filtered_udash = filtered_udash[filtered_udash['Term'] == term_filter]
else:
    filtered_udash = filtered_udash

# KPIs
st.header("Key Performance Indicators")

# Group by Term
for term, group in filtered_udash.groupby("Term"):
    st.header(f"Term: {term}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", f"{group['Applications'].sum():,}")
    col2.metric("Total Admitted", f"{group['Admitted'].sum():,}")
    col3.metric("Total Enrolled", f"{group['Enrolled'].sum():,}")
