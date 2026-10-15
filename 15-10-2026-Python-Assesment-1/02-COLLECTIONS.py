# Given sales 
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]



# Q10. Find total sales.
print("Q10 - Total Sales:", sum(sales))


# Q11. Find highest and lowest sale.
print("Q11 - Highest Sale:", max(sales))
print("Q11 - Lowest Sale:", min(sales))


# Q12. Display sales greater than 20000.
print("Q12 - Sales above 20000:")
for sale in sales:
    if sale > 20000:
        print(sale)


# Q13. Sort sales from highest to lowest.
sales.sort(reverse=True)
print("Q13 - Descending Sales:", sales)


# Q14. Create a set of unique cities.
cities = [
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Mumbai"
]

unique_cities = set(cities)
print("Q14 - Unique Cities:", unique_cities)



# Q15. Create and unpack a tuple.
product = (201, "Laptop", "Electronics", 65000)
product_id, product_name, category, price = product
print("Q15 - Product ID:", product_id)
print("Q15 - Product Name:", product_name)
print("Q15 - Category:", category)
print("Q15 - Price:", price)


# Q16. Create a customer dictionary.
customer = {
    "id": "C101",
    "name": "North Star Retail",
    "city": "Hyderabad",
    "orders": 3,
    "active": True
}

print("Q16 - Customer:", customer)


# Q17. Update customer's city.
customer["city"] = "Chennai"
print("Q17 - Updated Customer City:", customer["city"])


# Q18. Increase order count by 1.
customer["orders"] += 1
print("Q18 - Updated Order Count:", customer["orders"])


# Q19. Add email field.
customer["email"] = "northstar@example.com"

print("Q19 - Customer with Email:", customer)


# Q20. Display all dictionary keys and values.
print("Q20 - Customer Details:")

for key, value in customer.items():
    print(key, ":", value)
