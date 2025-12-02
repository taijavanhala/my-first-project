print("Program starting.")

# Ask user input
user_input = input("Insert comma separated integers: ")

# Split input
values = user_input.split(",")

valid_integers = []
invalid_values = []

# Validate entries
for value in values:
    value = value.strip()
    try:
        num = int(value)
        valid_integers.append(num)
    except ValueError:
        invalid_values.append(value)

# Report invalid values
for invalid in invalid_values:
    print(f"Error: '{invalid}' is not a valid integer.")

# Handle case where no valid integers exist
if len(valid_integers) == 0:
    print("No valid integers to analyze.")
    print("Program ending.")
    exit()

# Calculate results
count = len(valid_integers)
total_sum = sum(valid_integers)
parity = "even" if total_sum % 2 == 0 else "odd"

# Output results
print(f"There are {count} integers in the list.")
print(f"Sum of the integers is {total_sum} and it's {parity}")

print("Program ending.")
