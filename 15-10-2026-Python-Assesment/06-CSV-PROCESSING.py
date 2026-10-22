import csv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

csv_file = BASE_DIR / "registrations.csv"



# Q53. Read the file using the csv module.
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)


# Q54. Store records in a Python list.
registrations = list(reader)
print("Q54 - Total Records:", len(registrations))



# Q55. Display only Confirmed registrations.
print("\nQ55 - Confirmed Registrations:")

for registration in registrations:
    if registration["status"] == "Confirmed":
        print(registration)



# Q56. Display registrations from Hyderabad.

print("\nQ56 - Hyderabad Registrations:")

for registration in registrations:
    if registration["city"] == "Hyderabad":
        print(registration)


# Q57. Convert amount into a numeric datatype.

for registration in registrations:
    registration["amount"] = float(registration["amount"])

print("\nQ57 - Numeric Amount Example:")
print(registrations[0]["amount"])
print(type(registrations[0]["amount"]))


# Q58. Find registrations where amount exceeds 7000.

print("\nQ58 - Amounts Above 7000:")

for registration in registrations:
    if registration["amount"] > 7000:
        print(registration["registration_id"], registration["amount"])


# Q59. Calculate total registration amount.

total_amount = sum(
    registration["amount"]
    for registration in registrations
)

print("\nQ59 - Total Registration Amount:", total_amount)


# Q60. Extract all cities and display unique cities.

all_cities = [
    registration["city"]
    for registration in registrations
]

unique_cities = set(all_cities)

print("\nQ60 - All Cities:")
print(all_cities)

print("Q60 - Unique Cities:")
print(sorted(unique_cities))
