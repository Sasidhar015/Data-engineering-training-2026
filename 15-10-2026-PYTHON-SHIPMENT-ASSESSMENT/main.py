# Q34. Import the complete module.
import shipment_utils

cost = shipment_utils.calculate_shipping_cost(12.5, 50)

print("Q34 - Shipping Cost:", cost)

print("Q34 - Shipment Category:",shipment_utils.shipment_category(22))




# Q35. Import a specific function.
from shipment_utils import calculate_cost_per_kg

print("Q35 - Cost Per Kg:",calculate_cost_per_kg(850, 12.5))
