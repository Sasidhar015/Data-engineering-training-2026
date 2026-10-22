# Q76. Import the entire module.
import event_utils

booking = event_utils.calculate_booking(2500, 4)
discount = event_utils.calculate_discount(booking)
capacity_status = event_utils.check_event_capacity(500, 450)

print("Q76-Q77 - Booking Amount:", booking)
print("Q77 - Discount:", discount)
print("Q77 - Capacity Status:", capacity_status)


# Q78. Import one function directly.
from event_utils import calculate_booking

print(
    "Q78 - Direct Function Import:",
    calculate_booking(3500, 2))


# Q79. Import module using an alias.

import event_utils as eu

print(
    "Q79 - Alias Import:",
    eu.check_event_capacity(100, 100)
)
