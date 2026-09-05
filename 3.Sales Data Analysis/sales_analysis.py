import pandas as pd

# Load the sales dataset
df = pd.read_csv("Sales_data.csv")

# Display the data
print("Sales Data:")
print(df)

# Calculate total sales for each row
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nSales Data with Total Sales:")
print(df)

# Total revenue
total_revenue = df["Total_Sales"].sum()

print("\nTotal Revenue:", total_revenue)
# Sales by category
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nSales by Category:")
print(category_sales)
# Best-selling product
product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()
best_quantity = product_sales.max()

print("\nBest-Selling Product:")
print(best_product, "-", best_quantity, "units sold")
# Product with highest revenue
product_revenue = df.groupby("Product")["Total_Sales"].sum()

highest_revenue_product = product_revenue.idxmax()
highest_revenue = product_revenue.max()

print("\nHighest Revenue Product:")
print(highest_revenue_product, "-", highest_revenue)
import matplotlib.pyplot as plt

# Sales by category chart
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()