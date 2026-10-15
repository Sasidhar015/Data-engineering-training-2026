
# Q21. Calculate total.
def calculate_total(price, quantity):
    return price * quantity

print("Q21:", calculate_total(1500, 3))


# Q22. Calculate discount.
def calculate_discount(amount):
    if amount >= 50000:
        return amount * 0.10
    else:
        return amount * 0.05

print("Q22:", calculate_discount(60000))


# Q23. Return total sales from a list.
def total_sales(sales):
    return sum(sales)


sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
print("Q23:", total_sales(sales)


      
# Q24. Check product availability.
def check_product(product):
    if product["stock"] > 0:
        return "Available"
    else:
        return "Out of Stock"

product = {
    "product_name": "Laptop",
    "stock": 12
}
print("Q24:", check_product(product))


# Q25. Square using lambda.
square = lambda number: number ** 2

print("Q25:", square(5))


# Q26. Filter sales greater than 20000.
high_sales = list(filter(lambda sale: sale > 20000, sales))
print("Q26:", high_sales)


# Q27. Extract customer cities using map().
customers = [
    {"name": "Asha", "city": "Hyderabad"},
    {"name": "Ravi", "city": "Mumbai"},
    {"name": "Mina", "city": "Hyderabad"}
]

customer_cities = list(map(lambda customer: customer["city"], customers))
print("Q27:", customer_cities)


# Q28. Find unique cities.
unique_cities = set(customer_cities)
print("Q28:", unique_cities)


# Q29. Sort product dictionaries by price.
products = [
    {"product_name": "Laptop", "price": 65000},
    {"product_name": "Keyboard", "price": 3000},
    {"product_name": "Monitor", "price": 18000}
]

sorted_products = sorted(products, key=lambda product: product["price"])
print("Q29:")
for product in sorted_products:
     print(product) 
