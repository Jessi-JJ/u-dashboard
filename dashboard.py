import streamlit as st
import plotly.express as px
import pandas as pd

# Data Load and Cleanup
udash = pd.read_csv('university_student_dashboard_data.csv')
udash.columns = (udash.columns.str.replace(r'[^\w\s]', '', regex=True)
                         .str.strip()
                         .str.replace(r' ', '_', regex=True))
udash['Retention_Rate'] = udash['Retention_Rate']/100
udash['Student_Satisfaction'] = udash['Student_Satisfaction']/100

#Logo
st.set_page_config(page_icon="SUNY-Poly-seal-logo.png")
st.image("SUNY-Poly-horizontal-logo.png", width=250)

# Title
st.title("Student Admissions Dashboard")

# Sidebar Filter
st.sidebar.header("Filters")
year_filter = st.sidebar.selectbox("Select Year", ['All'] + sorted(udash['Year'].unique().tolist()))
if year_filter != 'All':
    filtered_udash = udash[udash['Year'] == year_filter]
else:
    filtered_udash = udash.copy()

term_filter = st.sidebar.selectbox("Select Term", ['All'] + sorted(filtered_udash['Term'].unique().tolist()))
if term_filter != 'All':
    filtered_udash = filtered_udash[filtered_udash['Term'] == term_filter]

# Create a combined column
filtered_udash['Year_Term'] = filtered_udash['Year'].astype(str) + " " + filtered_udash['Term']

# Sort filtered data
filtered_udash = filtered_udash.sort_values(by=["Year", "Term"])

# KPIs
st.header("Key Performance Indicators")

# Group by Term
for term, group in filtered_udash.groupby("Term"):
    st.header(f"Term: {term}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", f"{group['Applications'].sum():,}")
    col2.metric("Total Admitted", f"{group['Admitted'].sum():,}")
    col3.metric("Total Enrolled", f"{group['Enrolled'].sum():,}")


# Create a line chart for Retention Rate and Student Satisfaction
fig1 = px.line(filtered_udash, 
            x="Year_Term", 
            y="Retention_Rate",
            title="Retention Rate Trends", 
            labels={
            "Year_Term": "Term by Year",
            "Retention_Rate": "Retention Rate (%)"
    })

fig2 = px.line(filtered_udash,
            x="Year_Term", 
            y="Student_Satisfaction", 
            title="Student Satisfaction",
            labels={
            "Year_Term": "Term by Year",
            "Student_Satisfaction": "Student Satisfaction (%)"
    })

# Arrange the plots in a grid layout
col1, col2 = st.columns(2)  # Create 2 columns

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column
