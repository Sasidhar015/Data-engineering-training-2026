import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent



# Q44. Read hubs.csv.
hubs = pd.read_csv(BASE_DIR / "hubs.csv")

print("Q44 - Hub Data:")
print(hubs)


# Read shipments for Q45.
shipments = pd.read_csv(BASE_DIR / "shipments.csv")



# Q45. Inner join using hub_id.
joined = pd.merge(
    shipments,
    hubs,
    on="hub_id",
    how="inner")

print("\nQ45 - Joined Shipment and Hub Data:")
print(joined)


# Q46. Calculate total shipment cost by hub.
print("\nQ46 - Total Shipment Cost By Hub:")

hub_cost = (
    joined.groupby(["hub_id", "hub_name"])["cost"]
    .sum()
    .reset_index(name="total_shipment_cost"))

print(hub_cost)



# Q47. Calculate total shipment count by hub.
print("\nQ47 - Shipment Count By Hub:")

hub_count = (
    joined.groupby(["hub_id", "hub_name"])
    .size()
    .reset_index(name="total_shipments"))

print(hub_count)



# Combine hub cost and count summaries.
hub_summary = pd.merge(
    hub_cost,
    hub_count,
    on=["hub_id", "hub_name"],
    how="inner")


# Q48. Sort hubs by total shipment cost.
hub_summary = hub_summary.sort_values(
    by="total_shipment_cost",
    ascending=False)

print("\nQ48 - Sorted Hub Summary:")
print(hub_summary)


# Q49. Save results to CSV.
hub_summary.to_csv(
    BASE_DIR / "hub_shipment_summary.csv",
    index=False)

print("\nQ49 - CSV summary saved.")


# Q50. Save results to JSON.
hub_summary.to_json(
    BASE_DIR / "hub_shipment_summary.json",
    orient="records",
    indent=2)

print("Q50 - JSON summary saved.")
