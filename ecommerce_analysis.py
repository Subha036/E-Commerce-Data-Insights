import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("ecommerce_data.csv")

# Calculate revenue
data['revenue'] = data['quantity'] * data['price']

# Top-selling products
top_products = data.groupby('product')['revenue'].sum()

# Orders per hour
orders_by_hour = data.groupby('hour')['order_id'].count()

# Top users by revenue
top_users = data.groupby('user_id')['revenue'].sum()

# Bar chart: Top-selling products
plt.figure(figsize=(7,5))
top_products.plot(kind='bar', title='Top-Selling Products')
plt.ylabel("Revenue")
plt.show()

# Line chart: Orders by hour
plt.figure(figsize=(7,5))
orders_by_hour.plot(kind='line', marker='o', title='Orders by Hour')
plt.xlabel("Hour of Day")
plt.ylabel("Number of Orders")
plt.show()

# Pie chart: Revenue share by users
plt.figure(figsize=(6,6))
top_users.plot(kind='pie', autopct='%1.1f%%', title='Revenue Contribution by Users')
plt.ylabel("")
plt.show()

print("Top Products:\n", top_products)
print("\nTop Users:\n", top_users)
