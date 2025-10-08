# 1) Prompt user to insert value as an integer
value_str = input("Enter an integer value: ")
value = int(value_str)

# 2) Display menu
print("\nMenu")
print("1 - In one multi-branched decision")
print("2 - Independent if-statement decisions")
print("0 - Exit")

# 3) Prompt user to choose option
choice = input("Your choice: ")

# 4) Apply operations
if choice == "1":
    # One multi-branched decision (if / elif / elif):
    # Only the FIRST matching threshold is applied.
    result = value
    if result >= 400:
        result += 44
    elif result >= 200:
        result += 22
    elif result >= 100:
        result += 11
    # 5) Show result
    print(f"Result after one multi-branched decision: {result}")

elif choice == "2":
    # Independent if-statements one after another:
    # All matching thresholds are applied cumulatively.
    result = value
    if result >= 400:
        result += 44
    if result >= 200:
        result += 22
    if result >= 100:
        result += 11
    # 5) Show result
    print(f"Result after independent if-statements: {result}")

elif choice == "0":
    print("Exiting...")

else:
    print("Unknown option.")
