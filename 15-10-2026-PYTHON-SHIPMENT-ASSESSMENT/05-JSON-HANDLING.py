import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
employees_file = BASE_DIR / "employees.json"


# Q24. Read employees.json.
with open(employees_file, "r", encoding="utf-8") as file:
    employees = json.load(file)


# Q25. Display all employee names.
print("Q25 - Employee Names:")
for employee in employees:
    print(employee["name"])


# Q26. Find employees earning above 75000.
print("\nQ26 - Employees Earning Above 75000:")
for employee in employees:
    if employee["salary"] > 75000:
        print(employee["name"], employee["salary"])


# Q27. Display employees knowing Python.
print("\nQ27 - Employees Knowing Python:")
for employee in employees:
    if "Python" in employee["skills"]:
        print(employee["name"])


# Q28. Display employee name and performance rating.
print("\nQ28 - Employee Ratings:")
for employee in employees:
    print(
        employee["name"],
        employee["performance"]["rating"]
    )


# Q29. Find employees whose rating exceeds 4.5.
print("\nQ29 - Ratings Above 4.5:")
for employee in employees:
    rating = employee["performance"]["rating"]

    if rating > 4.5:
        print(employee["name"], rating)


# Q30. Sort employees by rating descending.
sorted_employees = sorted(
    employees,
    key=lambda employee: employee["performance"]["rating"],
    reverse=True
)

print("\nQ30 - Employees Sorted by Rating:")

for employee in sorted_employees:
    print(
        employee["name"],
        employee["performance"]["rating"]
    )


# Q31. Add one skill to employee 303.
for employee in employees:
    if employee["employee_id"] == 303:
        if "Python" not in employee["skills"]:
            employee["skills"].append("Python")

        break

print("\nQ31 - Updated Employee 303:")

for employee in employees:
    if employee["employee_id"] == 303:
        print(employee)


# Q32. Save modified JSON.
updated_file = BASE_DIR / "employees_updated.json"
with open(updated_file, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=2)

print("\nQ32 - Updated employee data saved.")


