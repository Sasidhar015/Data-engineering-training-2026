# Q75. Calculate booking amount.
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets


# Q75. Calculate discount.
def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    else:
        return amount * 0.05


# Q75. Check event capacity.
def check_event_capacity(capacity, participants):
    if capacity < 0 or participants < 0:
        return "Invalid Data"

    if participants > capacity:
        return "Invalid Data"

    if participants == capacity:
        return "Full"

    return "Seats Available"

