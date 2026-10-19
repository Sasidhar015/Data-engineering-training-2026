# Q33. Function to calculate shipping cost.
def calculate_shipping_cost(weight, rate_per_kg):
    return weight * rate_per_kg



# Q33. Function to classify shipment weight.
def shipment_category(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    else:
        return "Light"



# Q33. Function to calculate cost per kg.
def calculate_cost_per_kg(cost, weight):
    if weight <= 0:
        return 0

    return cost / weight


