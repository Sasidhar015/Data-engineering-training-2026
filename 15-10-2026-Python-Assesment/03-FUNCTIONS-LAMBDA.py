# Q26. Calculate booking amount.
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets

print("Q26 - Booking Amount:", calculate_booking(2500, 3))



# Q27. Return discount amount.
def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    else:
        return amount * 0.05
print("Q27 - Discount:", calculate_discount(12000))




# Q28. Check whether registration is active.
def check_registration(status):
    if status == "Confirmed":
        return "Active"
    else:
        return "Inactive"

print("Q28 - Registration:", check_registration("Confirmed"))



# Q29. Return total of booking amounts.
def total_booking_amount(amounts):
    return sum(amounts)


booking_amounts = [
    5000, 3500, 7500, 6000,
    4000, 7000, 3000, 10000]

print("Q29 - Total:", total_booking_amount(booking_amounts))



# Q30. Lambda increases amount by 10%.
increase_amount = lambda amount: amount * 1.10

print("Q30 - Increased Amount:", increase_amount(5000))


# Q31. Filter amounts greater than 6000.

high_amounts = list(
    filter(lambda amount: amount > 6000, booking_amounts)
)

print("Q31 - Amounts Above 6000:", high_amounts)



registrations = [
    {
        "registration_id": "R1001",
        "attendee_name": "Aarav Shah",
        "city": "Hyderabad",
        "status": "Confirmed",
        "amount": 5000
    },
    {
        "registration_id": "R1002",
        "attendee_name": "Simran Kaur",
        "city": "Mumbai",
        "status": "Confirmed",
        "amount": 3500
    },
    {
        "registration_id": "R1003",
        "attendee_name": "Faiz Ahmed",
        "city": "Pune",
        "status": "Pending",
        "amount": 7500
    },
    {
        "registration_id": "R1004",
        "attendee_name": "Keerthi Rao",
        "city": "Bangalore",
        "status": "Cancelled",
        "amount": 6000
    }
]


# Q32. Filter Confirmed registrations.

confirmed = list(
    filter(
        lambda item: item["status"] == "Confirmed",
        registrations
    )
)

print("\nQ32 - Confirmed Registrations:")

for item in confirmed:
    print(item)


# Q33. Extract attendee cities using map().

attendee_cities = list(
    map(lambda item: item["city"], registrations)
)

print("\nQ33 - Attendee Cities:")
print(attendee_cities)


# Q34. Use map() and set() to obtain unique cities.

unique_attendee_cities = set(
    map(lambda item: item["city"], registrations)
)

print("Q34 - Unique Cities:")
print(sorted(unique_attendee_cities))


# Q35. Sort registrations by amount.

sorted_registrations = sorted(
    registrations,
    key=lambda item: item["amount"]
)

print("\nQ35 - Registrations Sorted by Amount:")

for item in sorted_registrations:
    print(item)
