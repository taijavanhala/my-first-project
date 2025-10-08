# Prompt user to insert three integers
start = int(input("Enter the starting point: "))
stop = int(input("Enter the stopping point: "))
inspect = int(input("Enter the inspection point: "))

# --- Rule checks ---
violations = False

# Rule 1: start must be less than stop
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    violations = True

# Rule 2: inspection must be within the range
if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    violations = True

# If there are violations, skip loops
if violations:
    print("Program ending.")
else:
    # --- No violations: proceed with loops ---

    # First for-loop
    for i in range(start, stop + 1):
        if i == inspect:
            break
        if i != stop and i != inspect - 1:
            print(i, end=" ")
        elif i != inspect:
            print(i)

    # Second for-loop
    for i in range(start, stop + 1):
        if i == inspect:
            continue
        if i != stop:
            print(i, end=" ")
        else:
            print(i)

    print("Program ending.")
