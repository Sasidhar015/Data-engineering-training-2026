# Q30 Initialize the values using __init__().
class Product:

    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

# Q31. Display product details.
 def display_product(self):
    print("Product ID:", self.product_id)
    print("Product Name:", self.product_name)
    print("Price:", self.price)
    print("Stock:", self.stock)

# Q32. Calculate inventory value.
def calculate_value(self):
    return self.price * self.stock


# Q33. Create two Product objects.
product1 = Product(201, "Laptop", 65000, 12)
product2 = Product(204, "Keyboard", 3000, 30)

print("Q33 - Product 1:")
product1.display_product()
print("Inventory Value:", product1.calculate_value())
print("\nProduct 2:")
product2.display_product()


# Q34-Q36
class DiscountedProduct(Product):

    def __init__(self, product_id, product_name, price, stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)
        self.discount_percent = discount_percent

# Q37. Override display_product().
def display_product(self):
      super().display_product()
      print("Discount:", self.discount_percent, "%")


discounted_product = DiscountedProduct(
    202, "Monitor", 18000, 8, 10
)

print("\nQ37 - Discounted Product:")
discounted_product.display_product()


# Q38. Create PremiumProduct.
class PremiumProduct(Product):

    def __init__(self, product_id, product_name, price, stock):
        super().__init__(product_id, product_name, price, stock)

    def display_product(self):
        print("Premium Product Details:")
        super().display_product()

premium_product = PremiumProduct(205, "Premium Headphones", 12000, 5)



# Q39. Demonstrate polymorphism.
products = [
    product1,
    product2,
    discounted_product,
    premium_product
]

print("\nQ39 - Polymorphism:")

for product in products:
    product.display_product()
    print("-------------------------")

