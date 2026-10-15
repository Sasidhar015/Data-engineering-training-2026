# Q18-Q20. 
class Shipment:

    def __init__(self, shipment_id, destination, weight, cost):
        self.shipment_id = shipment_id
        self.destination = destination
        self.weight = weight
        self.cost = cost

    def display_shipment(self):
        print("Shipment ID:", self.shipment_id)
        print("Destination:", self.destination)
        print("Weight:", self.weight)
        print("Cost:", self.cost)

    def calculate_cost(self):
        return self.cost


# Q21. Create ExpressShipment inheriting from Shipment.
class ExpressShipment(Shipment):

    def __init__(
        self,
        shipment_id,
        destination,
        weight,
        cost,
        surcharge
    ):
        super().__init__(
            shipment_id,
            destination,
            weight,
            cost
        )

        self.surcharge = surcharge

  
  
  # Q22. Override method to add express surcharge.

    def calculate_cost(self):
        return self.cost + self.surcharge

    def display_shipment(self):
        super().display_shipment()

        print("Express Surcharge:", self.surcharge)
        print("Final Express Cost:", self.calculate_cost())


# Q23. Demonstrate polymorphism.
normal_shipment = Shipment(
    "S1001",
    "Hyderabad",
    12.5,
    850
)

express_shipment = ExpressShipment(
    "S1002",
    "Mumbai",
    8.0,
    620,
    200
)

shipments = [
    normal_shipment,
    express_shipment
]

print("Q23 - Polymorphism Demonstration:")

for shipment in shipments:
    shipment.display_shipment()
    print("Calculated Cost:", shipment.calculate_cost())
    print("-" * 30)
