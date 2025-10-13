def askName():
    """Prompts the user to insert their name and returns it."""
    name = input("Please enter your name: ")
    return name


def greetUser(pname):
    """Greets the user using the given name."""
    print(f"Hello {pname}!")
    return None


def main():
    """Main function that controls the program flow."""
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
