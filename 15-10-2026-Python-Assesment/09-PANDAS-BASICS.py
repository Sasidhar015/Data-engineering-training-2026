import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


# Q80. Read registrations.csv into a DataFrame.

registrations = pd.read_csv(
    BASE_DIR / "registrations.csv")

print("Q80 - Registration DataFrame:")
print(registrations)


# Q81. Display first 5 rows.

print("\nQ81 - First 5 Rows:")
print(registrations.head())


# Q81. Display last 5 rows.

print("\nQ81 - Last 5 Rows:")
print(registrations.tail())


# Q81. Display shape.

print("\nQ81 - Shape:")
print(registrations.shape)


# Q81. Display column names.

print("\nQ81 - Columns:")
print(registrations.columns.tolist())


# Q81. Display datatypes.

print("\nQ81 - Data Types:")
print(registrations.dtypes)


# Q82. Display selected columns.

print("\nQ82 - Selected Columns:")

selected_columns = registrations[
    [
        "attendee_name",
        "city",
        "status",
        "amount"
    ]
]

print(selected_columns)


# Q83. Use query() to find Confirmed registrations.

confirmed = registrations.query(
    "status == 'Confirmed'"
)

print("\nQ83 - Confirmed Registrations:")
print(confirmed)


# Q84. Find registrations whose amount exceeds 6000.

high_amount = registrations.query(
    "amount > 6000"
)

print("\nQ84 - Amount Above 6000:")
print(high_amount)


# Q85. Find Confirmed registrations from Hyderabad.

hyderabad_confirmed = registrations.query(
    "status == 'Confirmed' and city == 'Hyderabad'"
)

print("\nQ85 - Confirmed Hyderabad Registrations:")
print(hyderabad_confirmed)


# Q86. Count registrations by status.

print("\nQ86 - Registration Count by Status:")

print(
    registrations["status"].value_counts()
)


# Q87. Find total amount by status.

print("\nQ87 - Total Amount by Status:")

print(
    registrations.groupby("status")["amount"].sum()
)


# Q88. Find average amount by city.

print("\nQ88 - Average Amount by City:")

print(
    registrations.groupby("city")["amount"].mean()
)
