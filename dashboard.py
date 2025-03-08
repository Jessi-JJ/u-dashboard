import streamlit as st
import plotly.express as px
import pandas as pd

udash = pd.read_csv('university_student_dashboard_data.csv')

# KPIs
st.title("University Student Admissions Dashboard")

# Group by Term
for term, group in udash.groupby("Term"):
    st.header(f"Term: {term}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Applications", f"${group['Applications'].sum():,}")
    col2.metric("Total Accepted", f"${group['Accepted'].sum():,}")
    col3.metric("Total Enrolled", f"${group['Enrolled'].sum():,}")
    col4.metric("Acceptance Rate", f"{group['Acceptance_Rate'].mean():.2%}")
