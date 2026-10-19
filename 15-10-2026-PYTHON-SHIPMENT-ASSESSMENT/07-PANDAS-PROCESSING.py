import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent



# Q36. Read shipments.csv.
shipments = pd.read_csv(BASE_DIR / "shipments.csv")

print("Q36 - Shipment Data:")
print(shipments)


# Q37. Filter Delivered shipments.
delivered = shipments.query("status == 'Delivered'")

print("\nQ37 - Delivered Shipments:")
print(delivered)


# Q38. Count records by status.
print("\nQ38 - Count By Status:")
print(shipments["status"].value_counts())


# Q39. Convert shipment_date to datetime.
shipments["shipment_date"] = pd.to_datetime(
    shipments["shipment_date"]
)

print("\nQ39 - Date Data Type:")
print(shipments["shipment_date"].dtype)


# Create month column for Q40.
shipments["month"] = (
    shipments["shipment_date"]
    .dt.to_period("M")
    .astype(str)
)


# Q40. Count shipments by month and status.
print("\nQ40 - Shipments By Month and Status:")

monthly_status = (
    shipments.groupby(["month", "status"])
    .size()
    .reset_index(name="shipment_count")
)

print(monthly_status)


# Q41. Calculate average cost by destination.
print("\nQ41 - Average Cost By Destination:")

average_cost = (
    shipments.groupby("destination")["cost"]
    .mean()
)

print(average_cost)



# Q42. Calculate total weight by destination.
print("\nQ42 - Total Weight By Destination:")

total_weight = (
    shipments.groupby("destination")["weight"]
    .sum()
)

print(total_weight)



# Q43. Read selected columns using a dynamic usecols list.
selected_columns = [
    "shipment_id",
    "destination",
    "weight",
    "cost"
]

selected_data = pd.read_csv(
    BASE_DIR / "shipments.csv",
    usecols=selected_columns
)

print("\nQ43 - Selected Columns:")
print(selected_data)

