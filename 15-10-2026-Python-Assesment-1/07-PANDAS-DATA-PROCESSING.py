import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent



# Q61. Read orders.csv into a DataFrame.
orders = pd.read_csv(BASE_DIR / "orders.csv")

orders.rename(columns={"stat": "status"}, inplace=True)



# Q62. Display first five rows.
print("Q62 - First Five Rows:")
print(orders.head())



# Q63. Display columns and datatypes.
print("\nQ63 - Columns:")
print(orders.columns)

print("\nQ63 - Data Types:")
print(orders.dtypes)



# Q64. Display DataFrame shape.
print("\nQ64 - Shape:")
print(orders.shape)



# Q65. Filter Delivered orders using query().
delivered = orders.query("status == 'Delivered'")
print("\nQ65 - Delivered Orders:")
print(delivered)



# Q66. Filter quantity greater than 2.
high_quantity = orders[orders["quantity"] > 2]
print("\nQ66 - Quantity Greater Than 2:")
print(high_quantity)



# Q67. Calculate order_value.
orders["order_value"] = orders["quantity"] * orders["unit_price"]
print("\nQ67 - Order Values:")
print(orders[["order_id", "order_value"]])



# Q68. Count orders by status.
print("\nQ68 - Orders By Status:")
print(orders["status"].value_counts())


# Q69. Convert order_date to datetime.
orders["order_date"] = pd.to_datetime(orders["order_date"])



# Q70. Create month column.
orders["month"] = orders["order_date"].dt.to_period("M").astype(str)

print("\nQ70 - Month:")
print(orders[["order_date", "month"]])


# Q71. Order count by month and status.
print("\nQ71 - Monthly Order Count:")
print(orders.groupby(["month", "status"])
    .size()
    .reset_index(name="order_count"))



# Q72. Total order value by category.
print("\nQ72 - Total Value By Category:")

print(orders.groupby("category")["order_value"].sum())



# Q73. Average order value by category.
print("\nQ73 - Average Value By Category:")
print(orders.groupby("category")["order_value"].mean())



# Q74. Sort by order value descending.
sorted_orders = orders.sort_values(
    by="order_value",
    ascending=False)

print("\nQ74 - Sorted Orders:")
print(sorted_orders)


