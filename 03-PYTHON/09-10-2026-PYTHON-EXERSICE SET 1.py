import csv


# 1. Read shipments.csv
shipments = []

with open("shipments.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        shipments.append(row)



# 2. Display complete list
print("Complete list:")
print(shipments)



# 3. Display shipment ID, customer and status
print("\nShipment details:")

for shipment in shipments:
    print(
        shipment["shipment_id"],
        shipment["customer"],
        shipment["status"]
    )



# 4. Convert weight and cost to numeric values
for shipment in shipments:
    shipment["weight"] = float(shipment["weight"])
    shipment["cost"] = float(shipment["cost"])



# 5. Calculate total shipping cost
total_cost = 0

for shipment in shipments:
    total_cost += shipment["cost"]

print("\nTotal shipping cost:", total_cost)



# 6. Shipments with cost greater than 700
print("\nCost greater than 700:")

for shipment in shipments:
    if shipment["cost"] > 700:
        print(shipment)



# 7. filter() + lambda Delivered shipments
delivered = list(
    filter(
        lambda shipment: shipment["status"] == "Delivered",
        shipments
    )
)

print("\nDelivered shipments:")

for shipment in delivered:
    print(shipment)



# 8. filter() + lambda Weight greater than 10
heavy_shipments = list(
    filter(
        lambda shipment: shipment["weight"] > 10,
        shipments
    )
)

print("\nShipments weighing more than 10 kg:")

for shipment in heavy_shipments:
    print(shipment)



# 9. map() to extract city names
cities = list(
    map(
        lambda shipment: shipment["city"],
        shipments
    )
)

print("\nAll cities:")
print(cities)



# 10. map() + set() for unique cities
unique_cities = set(cities)

print("\nUnique cities:")
print(unique_cities)



# 11. Sort by cost - lowest to highest
shipments_by_cost = sorted(
    shipments,
    key=lambda shipment: shipment["cost"]
)

print("\nSorted by cost:")

for shipment in shipments_by_cost:
    print(
        shipment["shipment_id"],
        shipment["cost"]
    )



# 12. Sort by weight - highest to lowest
shipments_by_weight = sorted(
    shipments,
    key=lambda shipment: shipment["weight"],
    reverse=True
)

print("\nSorted by weight:")

for shipment in shipments_by_weight:
    print(
        shipment["shipment_id"],
        shipment["weight"]
    )



# 13. Sort alphabetically by customer
shipments_by_customer = sorted(
    shipments,
    key=lambda shipment: shipment["customer"]
)

print("\nSorted by customer:")

for shipment in shipments_by_customer:
    print(
        shipment["customer"]
    )



# 14. Lambda for cost per kg
cost_per_kg = lambda shipment: shipment["cost"] / shipment["weight"]

print("\nCost per kg:")

for shipment in shipments:
    print(
        shipment["shipment_id"],
        cost_per_kg(shipment)
    )


