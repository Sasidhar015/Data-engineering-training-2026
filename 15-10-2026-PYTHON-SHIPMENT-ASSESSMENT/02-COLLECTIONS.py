# Q7. Create a list of shipment costs.
shipment_costs = [
    850, 620, 1250, 480,
    1600, 740, 590, 1100,
    920, 1750, 520, 1050]

print("Q7 - Shipment Costs:")
print(shipment_costs)


# Q8. Calculate total, average, minimum and maximum.
total_cost = sum(shipment_costs)
average_cost = total_cost / len(shipment_costs)
minimum_cost = min(shipment_costs)
maximum_cost = max(shipment_costs)

print("\nQ8 - Total Cost:", total_cost)
print("Average Cost:", round(average_cost, 2))
print("Minimum Cost:", minimum_cost)
print("Maximum Cost:", maximum_cost)


# Q9. Remove duplicate destination cities using a set.
destinations = [
    "Hyderabad",
    "Mumbai",
    "Bangalore",
    "Delhi",
    "Pune",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Pune",
    "Hyderabad",
    "Mumbai"]

unique_destinations = set(destinations)
print("\nQ9 - Unique Destinations:")
print(sorted(unique_destinations))


# Q10. Store one shipment using a dictionary.
shipment = {
    "shipment_id": "S1001",
    "hub_id": "H01",
    "destination": "Hyderabad",
    "weight": 12.5,
    "status": "Delivered",
    "cost": 850}
print("\nQ10 - One Shipment:")
print(shipment)


# Q11. Store multiple shipments using a list of dictionaries.
shipments = [{
        "shipment_id": "S1001",
        "destination": "Hyderabad",
        "status": "Delivered",
        "cost": 850
    },
    {
        "shipment_id": "S1002",
        "destination": "Mumbai",
        "status": "In Transit",
        "cost": 620
    },
    {
        "shipment_id": "S1003",
        "destination": "Bangalore",
        "status": "Delivered",
        "cost": 1250
    },
    {
        "shipment_id": "S1004",
        "destination": "Delhi",
        "status": "Pending",
        "cost": 480
    }]

print("\nQ11 - Multiple Shipments:")
for item in shipments:
    print(item)


# Q12. Filter shipment records by status.
delivered_shipments = [
    item for item in shipments
    if item["status"] == "Delivered"
]

print("\nQ12 - Delivered Shipments:")

for item in delivered_shipments:
    print(item)

