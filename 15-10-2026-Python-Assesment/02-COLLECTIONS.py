
booking_amounts = [
    5000, 3500, 7500, 6000,
    4000, 7000, 3000, 10000]



# Q11. Find total booking amount.
print("Q11 - Total Booking Amount:", sum(booking_amounts))



# Q12. Find average booking amount.
average = sum(booking_amounts) / len(booking_amounts)

print("Q12 - Average Booking Amount:", average)


# Q13. Find highest and lowest amounts.

print("Q13 - Highest Amount:", max(booking_amounts))
print("Q13 - Lowest Amount:", min(booking_amounts))


# Q14. Display values greater than 5000.

print("\nQ14 - Amounts Greater Than 5000:")

for amount in booking_amounts:
    if amount > 5000:
        print(amount)


# Q15. Sort amounts descending.

sorted_amounts = sorted(booking_amounts, reverse=True)

print("\nQ15 - Descending Amounts:")
print(sorted_amounts)


# Given cities.

cities = [
    "Hyderabad",
    "Mumbai",
    "Pune",
    "Hyderabad",
    "Delhi",
    "Mumbai"
]


# Q16. Find unique cities using a set.

unique_cities = set(cities)

print("\nQ16 - Unique Cities:")
print(sorted(unique_cities))


# Q17. Add another city to the set.

unique_cities.add("Chennai")

print("Q17 - Cities After Adding Chennai:")
print(sorted(unique_cities))


# Q18. Find number of unique cities.

print("Q18 - Number of Unique Cities:", len(unique_cities))


# Q19. Create a tuple containing event details.

event = (
    "E101",
    "AI Innovation Summit",
    "Hyderabad",
    500
)

print("\nQ19 - Event Tuple:")
print(event)


# Q20. Unpack tuple into variables.

event_id, event_name, venue, capacity = event

print("Q20 - Event ID:", event_id)
print("Event Name:", event_name)
print("Venue:", venue)
print("Capacity:", capacity)


# Q21. Create registration dictionary.

registration = {
    "registration_id": "R1001",
    "attendee_name": "Aarav Shah",
    "city": "Hyderabad",
    "tickets": 2,
    "status": "Confirmed",
    "amount": 5000
}

print("\nQ21 - Registration:")
print(registration)


# Q22. Change registration status.

registration["status"] = "Pending"

print("Q22 - Updated Status:", registration["status"])


# Q23. Increase ticket count.

registration["tickets"] += 1

print("Q23 - Updated Tickets:", registration["tickets"])


# Q24. Add an email field.

registration["email"] = "aarav@example.com"

print("Q24 - Updated Registration:")
print(registration)


# Q25. Loop through dictionary items.

print("\nQ25 - Registration Details:")

for key, value in registration.items():
    print(f"{key}: {value}")
