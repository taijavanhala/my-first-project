# Prompt username first
name = input("Enter your name: ")

# Display menu
print("\nMenu:")
print("1. Print welcome message")
print("2. Exit")

# Prompt user to choose option
choice = input("Your choice: ")

# Perform actions based on user input
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print("Exiting...")
else:
    print("Unknown option.")
