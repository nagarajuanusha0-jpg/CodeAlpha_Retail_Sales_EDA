
import pandas as pd
import matplotlib.pyplot as plt

# Business Questions for Exploratory Data Analysis

print("\n========== BUSINESS QUESTIONS ==========")

print("1. Which product category generates the highest sales?")
print("2. Which product category generates the highest profit?")
print("3. Which region contributes the highest sales?")
print("4. Which sub-category generates the highest sales?")
print("5. Which sub-category generates the highest profit?")
print("6. Which sub-categories are operating at a loss?")

# Load the dataset
df = pd.read_csv("superstore.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

# Statistical Analysis

print("\n========== STATISTICAL ANALYSIS ==========")

print("\nTotal Sales:")
print(df['Sales'].sum())

print("\nAverage Sales:")
print(df['Sales'].mean())

print("\nMedian Sales:")
print(df['Sales'].median())

print("\nMaximum Sales:")
print(df['Sales'].max())

print("\nMinimum Sales:")
print(df['Sales'].min())

print("\nTotal Profit:")
print(df['Profit'].sum())

print("\nAverage Profit:")
print(df['Profit'].mean())

# Category-wise Sales Analysis

category_sales = df.groupby('Category')['Sales'].sum()

print("\n========== CATEGORY ANALYSIS ==========")

print("\nCategory-wise Sales:")
print(category_sales)

# Category-wise Profit Analysis
category_profit = df.groupby('Category')['Profit'].sum()

print("\nCategory-wise Profit:")
print(category_profit)

# Region-wise Sales Analysis
region_sales = df.groupby('Region')['Sales'].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Highest category and region
print("\nHighest Sales Category:")
print(category_sales.idxmax())

print("\nHighest Profit Category:")
print(category_profit.idxmax())

print("\nHighest Sales Region:")
print(region_sales.idxmax())

# Sub-category Analysis

subcategory_sales = df.groupby('Sub-Category')['Sales'].sum()
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum()

print("\n========== SUB-CATEGORY ANALYSIS ==========")

print("\nSub-category-wise Sales:")
print(subcategory_sales.sort_values(ascending=False))

print("\nSub-category-wise Profit:")
print(subcategory_profit.sort_values(ascending=False))

print("\nHighest Sales Sub-category:")
print(subcategory_sales.idxmax())

print("\nHighest Profit Sub-category:")
print(subcategory_profit.idxmax())

# Identify Loss-making Sub-categories

loss_making = subcategory_profit[subcategory_profit < 0]

print("\n========== LOSS-MAKING SUB-CATEGORIES ==========")

print("\nLoss-making Sub-categories:")
print(loss_making)

print("\nNumber of Loss-making Sub-categories:")
print(len(loss_making))

# Data Visualization

print("\n========== DATA VISUALIZATION ==========")

# 1. Category-wise Sales Bar Chart

plt.figure(figsize=(8, 5))

category_sales.plot(kind='bar')

plt.title('Category-wise Sales Analysis')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 2. Region-wise Sales Bar Chart

plt.figure(figsize=(8, 5))

region_sales.plot(kind='bar')

plt.title('Region-wise Sales Analysis')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

# 3. Category-wise Profit Bar Chart

plt.figure(figsize=(8, 5))

category_profit.plot(kind='bar')

plt.title('Category-wise Profit Analysis')
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_profit.png")
plt.show()

# 4. Sales Distribution Histogram

plt.figure(figsize=(8, 5))

plt.hist(df['Sales'], bins=30, edgecolor='black')

plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

print("\n========== ANALYSIS COMPLETED SUCCESSFULLY ==========")
