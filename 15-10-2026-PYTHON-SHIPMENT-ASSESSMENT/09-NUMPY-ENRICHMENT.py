import numpy as np
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


shipments = pd.read_csv(BASE_DIR / "shipments.csv")



# Q51. Add cost_per_kg = cost / weight.
shipments["cost_per_kg"] = np.where(
    shipments["weight"] > 0,
    shipments["cost"] / shipments["weight"],
    0)



# Q52. Classify cost using NumPy.
shipments["cost_category"] = np.where(
    shipments["cost"] >= 1200,
    "Expensive",
    "Normal")


# Q53. Add shipment performance category
conditions = [
    (
        (shipments["status"] == "Delivered")
        & (shipments["cost"] >= 1000)
    ),
    (
        (shipments["status"] == "Delivered")
        & (shipments["cost"] < 1000)
    ),
    (
        shipments["status"] == "In Transit"
    ),
    (
        shipments["status"] == "Pending"
    )
]

categories = [
    "High Performance",
    "Standard Performance",
    "In Progress",
    "Awaiting Processing"
]

shipments["shipment_performance"] = np.select(
    conditions,
    categories,
    default="Other"
)


# Q54. Save enriched dataset as shipment_analysis.csv.

shipments.to_csv(
    BASE_DIR / "shipment_analysis.csv",
    index=False
)
