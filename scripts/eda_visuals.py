# scripts/eda_visuals.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Load cleaned data
df = pd.read_csv("data/cleaned_sales_data.csv")

# Create charts folder if not exists
import os
if not os.path.exists("data/plots"):
    os.makedirs("data/plots")

# 1. Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
category_sales.plot(kind='barh', title='Sales by Category', color='skyblue')
plt.xlabel('Sales')
plt.tight_layout()
plt.savefig("data/plots/category_sales.png")
plt.clf()

# 2. Profit by Region
profit_region = df.groupby('Region')['Profit'].sum().sort_values()
profit_region.plot(kind='barh', title='Profit by Region', color='lightgreen')
plt.xlabel('Profit')
plt.tight_layout()
plt.savefig("data/plots/profit_by_region.png")
plt.clf()

# 3. Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', title='Top 10 Products by Sales', color='coral')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("data/plots/top_products.png")
plt.clf()

# 4. Monthly Sales Trend
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum()
monthly_sales.unstack().T.plot(kind='line', figsize=(10,5), marker='o', title='Monthly Sales Trend')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig("data/plots/monthly_sales_trend.png")
plt.clf()

# 5. Sales by Segment
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values()
segment_sales.plot(kind='barh', title='Sales by Customer Segment', color='violet')
plt.xlabel('Sales')
plt.tight_layout()
plt.savefig("data/plots/segment_sales.png")
plt.clf()

# 6. Discount vs Quantity (Heatmap)
pivot = df.pivot_table(index='Discount', columns='Quantity', values='Sales', aggfunc='sum')
sns.heatmap(pivot, cmap='YlGnBu')
plt.title("Heatmap: Discount vs Quantity")
plt.tight_layout()
plt.savefig("data/plots/quantity_discount_heatmap.png")
plt.clf()

print("✅ All EDA plots saved in: data/plots/")
