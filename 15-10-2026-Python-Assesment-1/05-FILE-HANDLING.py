import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# Q40 Create activity.txt
activity_file = BASE_DIR / "activity.txt"


# Q41. Write three messages.
with open(activity_file, "w", encoding="utf-8") as file:
    file.write("Started customer data processing.\n")
    file.write("Validated order records.\n")
    file.write("Loaded product data.\n")



# Q42. Append one message.
with open(activity_file, "a", encoding="utf-8") as file:
    file.write("Assessment processing completed.\n")


# Q43. Read complete file.

print("Q43 - Activity File:")

with open(activity_file, "r", encoding="utf-8") as file:
    print(file.read())




customers_file = BASE_DIR / "customers.csv"




# Q44. Read CSV using csv module.
with open(customers_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Q45. Store records in a list.
    customers = list(reader)

print("Q45 - Customer Records:", customers)


# Q46. Display active customers.

print("\nQ46 - Active Customers:")

for customer in customers:
    if customer["active"].strip().lower() == "true":
        print(customer)


# Q47. Display Hyderabad customers.

print("\nQ47 - Hyderabad Customers:")

for customer in customers:
    if customer["city"] == "Hyderabad":
        print(customer)


# Q48-Q55. Read and process products.json.

products_file = BASE_DIR / "products.json"

# Q48. Read JSON.

with open(products_file, "r", encoding="utf-8") as file:
    products = json.load(file)


# Q49. Display all product names.

print("\nQ49 - Product Names:")

for product in products:
    print(product["product_name"])


# Q50. Display products costing above 10000.

print("\nQ50 - Products Above 10000:")

for product in products:
    if product["price"] > 10000:
        print(product["product_name"], product["price"])


# Q51. Display supplier name and city.

print("\nQ51 - Supplier Details:")

for product in products:
    supplier = product["supplier"]

    print(
        product["product_name"],
        supplier["name"],
        supplier["city"]
    )


# Q52. Extract all colors.

all_colors = []

for product in products:
    all_colors.extend(product["colors"])

print("\nQ52 - All Colors:", all_colors)


# Q53. Display unique colors.

unique_colors = set(all_colors)

print("Q53 - Unique Colors:", unique_colors)


# Q54. Increase stock of product ID 202.
for product in products:
    if product["product_id"] == 202:
        product["stock"] += 5
        break
print("\nQ54 - Updated Product:")
for product in products:
    if product["product_id"] == 202:
        print(product)


# Q55. Write modified data to products_updated.json.
updated_file = BASE_DIR / "products_updated.json"

with open(updated_file, "w", encoding="utf-8") as file:
    json.dump(products, file, indent=2)

print("Q55 - Updated products saved.")
