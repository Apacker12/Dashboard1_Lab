#import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
# Sample Data
data = {
    'Order ID': range(1, 21),
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Headphones'] * 4,
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'] * 4,
    'Price': np.random.randint(50, 1000, 20),
    'Quantity': np.random.randint(1, 5, 20)
}
df = pd.DataFrame(data)
df['Total'] = df['Price'] * df['Quantity']

# Sidebar Filter
st.sidebar.header("Filters")
category_filter = st.sidebar.selectbox("Select Category", ['All'] + list(df['Category'].unique()))
if category_filter != 'All':
    df = df[df['Category'] == category_filter]

# KPIs
st.title("E-commerce Sales Dashboard")

# Create columns for metrics
col1,col2=st.columns(2)
with col1:
    st.metric("Total Revenue", f"${df['Total'].sum():,.2f}")
with col2:
    st.metric("Total Orders", len(df))

# Create columns for metrics
col1, col2=st.columns(2)
with col1:
    # Data Table
    st.subheader("Sales Data")
    st.dataframe(df)
with col2:
    # Chart
    st.subheader("Sales by Category")
    category_sales = df.groupby('Category')['Total'].sum().reset_index()
    st.bar_chart(category_sales.set_index('Category'))
