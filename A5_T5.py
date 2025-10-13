def main():
    """Menu-driven program for handling a stored word."""
    word = ""  # Initialize with empty string
    while True:
        print("\nMenu:")
        print("1. Insert a word")
        print("2. Show current word")
        print("3. Show current word in reverse")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            word = input("Enter a word: ")
            print("Word stored successfully.")
        elif choice == "2":
            if word:
                print(f"Current word: {word}")
            else:
                print("No word stored yet.")
        elif choice == "3":
            if word:
                print(f"Reversed word: {word[::-1]}")
            else:
                print("No word stored yet.")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Unknown option, please try again.")

    return None


if __name__ == "__main__":
    main()
