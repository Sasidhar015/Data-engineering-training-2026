import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

customers = pd.read_csv(BASE_DIR / "customers.csv")
orders = pd.read_csv(BASE_DIR / "orders.csv")
orders.rename(columns={"stat": "status"}, inplace=True)



# Q75. Perform inner join using customer_id.
joined = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner")
joined["order_value"] = joined["quantity"] * joined["unit_price"]



# Q76. Display selected columns.
print("Q76 - Joined Data:")

print( joined[[
            "order_id",
            "customer_name",
            "city",
            "product",
            "status",
            "order_value"
        ]])


# Q77. Delivered orders from Hyderabad.
hyderabad_delivered = joined.query(
    "status == 'Delivered' and city == 'Hyderabad'"
)

print("\nQ77 - Hyderabad Delivered Orders:")
print(hyderabad_delivered)


# Q78. Calculate total orders, total sales and average order value.
city_summary = (
    joined.groupby("city")
    .agg(
        total_orders=("order_id", "count"),
        total_sales=("order_value", "sum"),
        average_order_value=("order_value", "mean")
    )
    .reset_index()
)


# Q79. Sort total sales in descending order.
city_summary = city_summary.sort_values(
    by="total_sales",
    ascending=False
)

print("\nQ78-Q79 - City Sales Summary:")
print(city_summary)


# Q80. Write summary to CSV.
city_summary.to_csv(
    BASE_DIR / "city_sales_summary.csv",
    index=False
)

print("\nQ80 - CSV file created.")


# Q81. Write record-oriented JSON.
city_summary.to_json(
    BASE_DIR / "city_sales_summary.json",
    orient="records",
    indent=2
)
print("Q81 - JSON file created.")

