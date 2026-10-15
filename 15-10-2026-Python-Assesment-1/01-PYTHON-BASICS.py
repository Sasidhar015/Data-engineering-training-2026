# Q1. Take product name, unit price and quantity from user.
product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))



# Q2. Calculate total amount.
total_amount = unit_price * quantity



# Q3. Apply discount based on total amount.
if total_amount >= 50000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05
final_amount = total_amount - discount



# Q4. Display amounts using f-strings.
print(f"Product Name: {product_name}")
print(f"Original Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Amount: {final_amount:.2f}")


# Q5. Check stock quantity.
stock = int(input("Enter stock quantity: "))

if stock > 20:
    print("High Stock")
elif stock >= 1:
    print("Low Stock")
elif stock == 0:
    print("Out of Stock")
else:
    print("Invalid stock quantity")


# Q6. Display numbers from 1 to 10.
print("\nNumbers from 1 to 10:")

for number in range(1, 11):
    print(number)


# Q7. Reduce stock from 5 to 0 using while loop.
print("\nStock countdown:")

stock = 5

while stock >= 0:
    print(stock)
    stock -= 1


# Q8. Skip number 5 using continue.
print("\nSkipping number 5:")

for number in range(1, 11):
    if number == 5:
        continue

    print(number)


# Q9. Stop the loop when the value reaches 8.
print("\nStopping at 8:")

for number in range(1, 11):
    if number == 8:
        break

    print(number)
