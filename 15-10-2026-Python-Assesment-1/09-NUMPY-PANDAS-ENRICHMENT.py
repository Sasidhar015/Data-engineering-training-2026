import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

customers = pd.read_csv(BASE_DIR / "customers.csv")
orders = pd.read_csv(BASE_DIR / "orders.csv")

orders.rename(columns={"stat": "status"}, inplace=True)

joined = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner")

joined["order_value"] = joined["quantity"] * joined["unit_price"]



# Q82. Create order_size using NumPy.
joined["order_size"] = np.select([joined["order_value"] >= 50000,joined["order_value"] >= 15000],["High","Medium"],default="Low")


# Q83. Create priority_customer.
joined["priority_customer"] = np.where(joined["segment"] == "Corporate","Priority","Normal")


# Q84. Save enriched dataset.
joined.to_csv(BASE_DIR / "enriched_orders.csv",index=False)
print("Q82-Q84 - Enriched Dataset:")
print(joined[[ "order_id", "customer_name", "order_value", "order_size","priority_customer"]])
print("\nEnriched dataset saved successfully.")
