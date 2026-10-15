# Q1. Accept shipment weight and cost from the user.
weight = float(input("Enter shipment weight in kg: "))
cost = float(input("Enter shipping cost: "))


# Q2. Calculate cost per kg.
cost_per_kg = cost / weight if weight > 0 else 0
print("Cost per kg:", round(cost_per_kg, 2))


# Q3. Classify shipment based on weight.
if weight > 20:
    category = "Heavy"
elif weight >= 10:
    category = "Medium"
else:
    category = "Light"

print("Shipment Category:", category)


# Q4. Display shipment numbers from 1 to 20.
print("\nQ4 - Shipment Numbers:")
for number in range(1, 21):
    print(number)


# Q5. Display only even shipment numbers.
print("\nQ5 - Even Shipment Numbers:")
for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# Q6. Simulate five processing attempts using while loop.
print("\nQ6 - Processing Attempts:")
attempt = 1
while attempt <= 5:
    print(f"Processing attempt {attempt}")
    attempt += 1
