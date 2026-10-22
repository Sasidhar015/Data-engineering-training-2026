# Q1. Take attendee name, number of tickets and ticket price.
attendee_name = input("Enter attendee name: ")
tickets = int(input("Enter number of tickets: "))
ticket_price = float(input("Enter ticket price: "))


# Q2. Calculate total booking amount.
total_amount = tickets * ticket_price


# Q3. Apply discount.
if total_amount >= 10000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount


# Q4. Display results using f-strings.
print("\n--- Booking Details ---")
print(f"Attendee Name: {attendee_name}")
print(f"Number of Tickets: {tickets}")
print(f"Ticket Price: ₹{ticket_price:.2f}")
print(f"Original Amount: ₹{total_amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")


# Q5. Ask for event capacity and registered participants.

capacity = int(input("\nEnter event capacity: "))
participants = int(input("Enter registered participants: "))


# Q6. Check event capacity.

if capacity < 0 or participants < 0:
    print("Invalid Data")
elif participants > capacity:
    print("Invalid Data")
elif participants == capacity:
    print("Full")
else:
    print("Seats Available")


# Q7. Print numbers 1-15.

print("\nQ7 - Numbers 1 to 15:")

for number in range(1, 16):
    print(number)


# Q8. Display numbers divisible by 3.

print("\nQ8 - Numbers Divisible by 3:")

for number in range(1, 16):
    if number % 3 == 0:
        print(number)


# Q9. Countdown from 10 to 1.

print("\nQ9 - Countdown:")

number = 10

while number >= 1:
    print(number)
    number -= 1


# Q10. Demonstrate break and continue.

print("\nQ10 - Continue Example:")

for number in range(1, 11):
    if number == 5:
        continue

    print(number)


print("\nQ10 - Break Example:")

for number in range(1, 11):
    if number == 8:
        break

    print(number)
