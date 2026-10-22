# Q36. Create Event class and initialize attributes.
class Event:

    def __init__(self, event_id, event_name, capacity, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price


    
  
  # Q37. Display event details.
   def display_event(self):
        print("Event ID:", self.event_id)
        print("Event Name:", self.event_name)
        print("Capacity:", self.capacity)
        print("Ticket Price:", self.ticket_price)


   
    # Q38. Calculate revenue.

    def calculate_revenue(self, tickets_sold):
        return self.ticket_price * tickets_sold


# Q39-Q42
class OnlineEvent(Event):

    def __init__(
        self,
        event_id,
        event_name,
        capacity,
        ticket_price,
        platform
    ):
        super().__init__(
            event_id,
            event_name,
            capacity,
            ticket_price
        )

        self.platform = platform


    # Q42. Override display_event().

    def display_event(self):
        super().display_event()
        print("Platform:", self.platform)


# Q43-Q44. 

class PhysicalEvent(Event):

    def __init__(
        self,
        event_id,
        event_name,
        capacity,
        ticket_price,
        venue
    ):
        super().__init__(
            event_id,
            event_name,
            capacity,
            ticket_price
        )

        self.venue = venue


    def display_event(self):
        super().display_event()
        print("Venue:", self.venue)


# Q39. Create two Event-related objects.

online_event = OnlineEvent(
    "E101",
    "AI Innovation Summit",
    500,
    2500,
    "Zoom"
)

physical_event = PhysicalEvent(
    "E102",
    "Leadership Forum",
    350,
    3500,
    "Mumbai Convention Centre"
)


# Q38. Calculate revenue.

print("Q38 - Online Event Revenue:")
print(online_event.calculate_revenue(100))


# Q45. Put OnlineEvent and PhysicalEvent objects into a list.

events = [online_event, physical_event]


# Q46. Demonstrate polymorphism.

print("\nQ46 - Polymorphism Demonstration:")

for event in events:
    event.display_event()
    print("-" * 40)
