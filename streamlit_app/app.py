
# streamlit_app/app.py

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📈 Sales Insights Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/cleaned_sales_data.csv")

# Sidebar filters
st.sidebar.title("🔍 Filters")
region = st.sidebar.multiselect("Region", df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Category", df['Category'].unique(), default=df['Category'].unique())
segment = st.sidebar.multiselect("Segment", df['Segment'].unique(), default=df['Segment'].unique())

# Apply filters
filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Segment'].isin(segment))
]

# KPIs
total_sales = int(filtered_df['Sales'].sum())
total_profit = int(filtered_df['Profit'].sum())
total_orders = filtered_df['Order ID'].nunique()

st.title("📊 Sales Insights Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,}")
col2.metric("📦 Total Orders", f"{total_orders}")
col3.metric("💹 Total Profit", f"${total_profit:,}")

st.markdown("---")

# Display plots
plot_paths = {
    "Sales by Category": "data/plots/category_sales.png",
    "Profit by Region": "data/plots/profit_by_region.png",
    "Top 10 Products by Sales": "data/plots/top_products.png",
    "Monthly Sales Trend": "data/plots/monthly_sales_trend.png",
    "Sales by Customer Segment": "data/plots/segment_sales.png",
    "Discount vs Quantity Heatmap": "data/plots/quantity_discount_heatmap.png"
}

for title, path in plot_paths.items():
    st.subheader(f"📌 {title}")
    st.image(path, use_container_width=True)
    st.markdown("---")

# Display raw data
with st.expander("📂 View Raw Data"):
    st.dataframe(filtered_df)
