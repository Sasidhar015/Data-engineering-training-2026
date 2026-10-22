from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / "event_log.txt"



# Q47. Write three event-processing messages.
with open(log_file, "w", encoding="utf-8") as file:
    file.write("Event registration process started.\n")
    file.write("Attendee details validated.\n")
    file.write("Ticket booking processed.\n")


# Q48. Append two more messages.
with open(log_file, "a", encoding="utf-8") as file:
    file.write("Payment verification completed.\n")
    file.write("Event registration process finished.\n")


# Q49. Read the complete file.
print("Q49 - Complete Event Log:")

with open(log_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# Q50. Read the file line by line.

print("Q50 - Reading Line by Line:")

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")


# Q51. Display every line without additional blank lines.

print("\n\nQ51 - Clean Line Display:")

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))


# Q52. Use with open() rather than manually closing.

print("\nQ52 - File handling completed using with open().")
