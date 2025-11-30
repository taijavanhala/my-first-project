def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []

    while True:
        user_input = input("Insert positive integer(negative stops): ")

        # Try to convert to integer
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        # Negative integer stops the loop
        if number < 0:
            print("Stopped collecting positive integers.")
            break

        # Only positive integers are collected
        if number > 0:
            numbers.append(number)

    # Display results
    if len(numbers) == 0:
        print("No positive integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

    print("Program ending.")


if __name__ == "__main__":
    main()
