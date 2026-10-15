# Q13. Create a function calculating shipping cost.
def calculate_shipping_cost(weight, rate_per_kg):
    return weight * rate_per_kg
print(
    "Q13 - Shipping Cost:",
    calculate_shipping_cost(12.5, 50)
)


# Q14. Return shipment category based on weight.
def shipment_category(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    else:
        return "Light"
print("Q14 - Category:", shipment_category(22))



shipments = [
    {
        "shipment_id": "S1001",
        "destination": "Hyderabad",
        "weight": 12.5,
        "status": "Delivered",
        "cost": 850
    },
    {
        "shipment_id": "S1002",
        "destination": "Mumbai",
        "weight": 8.0,
        "status": "In Transit",
        "cost": 620
    },
    {
        "shipment_id": "S1003",
        "destination": "Bangalore",
        "weight": 18.5,
        "status": "Delivered",
        "cost": 1250
    },
    {
        "shipment_id": "S1004",
        "destination": "Delhi",
        "weight": 5.5,
        "status": "Pending",
        "cost": 480}]



# Q15. Use lambda/filter to select Delivered shipments.
delivered = list(
    filter(
        lambda shipment: shipment["status"] == "Delivered",
        shipments))

print("\nQ15 - Delivered Shipments:")
for shipment in delivered:
    print(shipment)



# Q16. Use map to obtain all destinations.
destinations = list(
    map(
        lambda shipment: shipment["destination"],
        shipments))
print("\nQ16 - Destinations:")
print(destinations)


# Q17. Sort shipment dictionaries by cost.
sorted_shipments = sorted(
    shipments,
    key=lambda shipment: shipment["cost"])
print("\nQ17 - Shipments Sorted by Cost:")
for shipment in sorted_shipments:
    print(shipment)

