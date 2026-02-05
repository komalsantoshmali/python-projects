# analysis.py
# Project: CSV Data Analysis with Pandas & Visualization
# Author: Komal
# Date: 2026

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# 1. Load CSV file
# ------------------------------
df = pd.read_csv('sales.csv')
print("Data Loaded Successfully!\n")
print(df.head())

# ------------------------------
# 2. Basic Data Analysis
# ------------------------------

# Average of numeric columns
average_units = df['Units_Sold'].mean()
average_revenue = df['Revenue'].mean()
print(f"\nAverage Units Sold: {average_units}")
print(f"Average Revenue: {average_revenue}")

# Total revenue per region
revenue_region = df.groupby('Region')['Revenue'].sum()
print("\nTotal Revenue by Region:\n", revenue_region)

# Max / Min units sold
print("\nMax Units Sold:", df['Units_Sold'].max())
print("Min Units Sold:", df['Units_Sold'].min())

# ------------------------------
# 3. Create Visualizations
# ------------------------------

# Create visualizations folder if not exists
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# a) Bar Chart: Revenue per Region
revenue_region.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('visualizations/bar_chart.png')
plt.show()

# b) Scatter Plot: Units Sold vs Revenue
plt.scatter(df['Units_Sold'], df['Revenue'], color='red')
plt.title('Units Sold vs Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('visualizations/scatter_plot.png')
plt.show()

# c) Heatmap: Correlation (numeric columns only)
numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('visualizations/heatmap.png')
plt.show()

# ------------------------------
# 4. Additional Insights (Optional)
# ------------------------------

# Revenue per Product
revenue_product = df.groupby('Product')['Revenue'].sum()
print("\nTotal Revenue by Product:\n", revenue_product)

revenue_product.plot(kind='bar', color='orange')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('visualizations/revenue_by_product.png')
plt.show()
