# Prompt username first
name = input("Enter your name: ")

# Display menu
print("\nMenu:")
print("1. Print welcome message")
print("2. Print the name backwards")
print("3. Print the first character")
print("4. Show the amount of characters in the name")
print("5. Exit")

# Prompt user to choose option
choice = input("Your choice: ")

# Perform actions based on user input
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    name_backwards = name[::-1]
    print(f'Your name backwards is "{name_backwards}"')
elif choice == "3":
    first_char = name[0]
    print(f'The first character in name "{name}" is "{first_char}"')
elif choice == "4":
    name_length = len(name)
    print(f'There are {name_length} characters in the name "{name}"')
elif choice == "5":
    print("Exiting...")
else:
    print("Unknown option.")
