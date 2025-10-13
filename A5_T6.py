def showOptions():
    """Show available menu options."""
    print("\nMenu:")
    print("1. Increment")
    print("2. Decrement")
    print("3. Reset")
    print("4. Show current value")
    print("5. Exit")
    return None


def askChoice():
    """
    Ask user for a choice and return an integer regardless of input.
    Prints 'Unknown option!' if input is not numeric.
    """
    choice = input("Select an option (1-5): ").strip()
    if not choice.isnumeric():
        print("Unknown option!")
        return -1
    return int(choice)


def main():
    """Main program logic with the menu cycle."""
    counter = 0  # Initialize the tally counter
    print("Tally Counter")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            counter += 1
            print(f"Count: {counter}")
        elif choice == 2:
            counter -= 1
            print(f"Count: {counter}")
        elif choice == 3:
            counter = 0
            print("Counter reset to 0")
        elif choice == 4:
            print(f"Count: {counter}")
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        elif choice == -1:
            # Non-numeric input already handled with message in askChoice
            continue
        else:
            # Numeric but not a known option
            print("Unknown option!")

    return None


if __name__ == "__main__":
    main()
