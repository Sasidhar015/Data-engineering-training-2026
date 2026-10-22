import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
staff_file = BASE_DIR / "staff.json"



# Q61. Read JSON into Python.
with open(staff_file, "r", encoding="utf-8") as file:
    staff = json.load(file)


# Q62. Check the datatype.
print("Q62 - Datatype:", type(staff))


# Q63. Display all staff names.
print("\nQ63 - Staff Names:")

for employee in staff:
    print(employee["name"])


# Q64. Display employees from Operations.
print("\nQ64 - Operations Employees:")

for employee in staff:
    if employee["department"] == "Operations":
        print(employee["name"])


# Q65. Display employees earning above 75000.

print("\nQ65 - Salary Above 75000:")

for employee in staff:
    if employee["salary"] > 75000:
        print(employee["name"], employee["salary"])


# Q66. Find employees having Python in their skills.

print("\nQ66 - Employees Knowing Python:")

for employee in staff:
    if "Python" in employee["skills"]:
        print(employee["name"])


# Q67. Display name, rating and events handled.

print("\nQ67 - Staff Performance:")

for employee in staff:
    print(
        "Name:", employee["name"],
        "| Rating:", employee["performance"]["rating"],
        "| Events Handled:", employee["performance"]["events_handled"]
    )


# Q68. Find employees whose rating exceeds 4.5.

print("\nQ68 - Rating Above 4.5:")

for employee in staff:
    if employee["performance"]["rating"] > 4.5:
        print(employee["name"])


# Q69. Extract all skills into one list.

all_skills = []

for employee in staff:
    all_skills.extend(employee["skills"])

print("\nQ69 - All Skills:")
print(all_skills)


# Q70. Find unique skills.

unique_skills = set(all_skills)

print("\nQ70 - Unique Skills:")
print(sorted(unique_skills))


# Q71. Sort employees by salary descending.

salary_sorted = sorted(
    staff,
    key=lambda employee: employee["salary"],
    reverse=True
)

print("\nQ71 - Employees Sorted by Salary:")

for employee in salary_sorted:
    print(employee["name"], employee["salary"])


# Q72. Sort employees by performance rating descending.

rating_sorted = sorted(
    staff,
    key=lambda employee: employee["performance"]["rating"],
    reverse=True
)

print("\nQ72 - Employees Sorted by Rating:")

for employee in rating_sorted:
    print(
        employee["name"],
        employee["performance"]["rating"]
    )


# Q73. Add Pandas to staff ID 503.

for employee in staff:
    if employee["staff_id"] == 503:
        if "Pandas" not in employee["skills"]:
            employee["skills"].append("Pandas")

        break


print("\nQ73 - Updated Staff 503:")

for employee in staff:
    if employee["staff_id"] == 503:
        print(employee)


# Q74. Save modified JSON as staff_updated.json.

updated_file = BASE_DIR / "staff_updated.json"

with open(updated_file, "w", encoding="utf-8") as file:
    json.dump(staff, file, indent=2)

print("\nQ74 - Updated JSON saved successfully.")
