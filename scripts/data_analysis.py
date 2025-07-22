# scripts/data_analysis.py

import pandas as pd

# Load dataset
df = pd.read_csv("data/superstore_sales.csv", encoding='latin1')
print("✅ Data Loaded")
print(df.head())

# Basic Info
print("\n📊 Dataset Info:")
print(df.info())

# Check for null values
print("\n🧼 Missing Values:")
print(df.isnull().sum())

# Rename columns (strip spaces if needed)
df.columns = df.columns.str.strip()

# Convert Order Date and Ship Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract useful columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Weekday'] = df['Order Date'].dt.day_name()

# Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)
print("\n✅ Cleaned data saved to: data/cleaned_sales_data.csv")
