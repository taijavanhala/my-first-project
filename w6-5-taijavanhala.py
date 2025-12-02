SEPARATOR = ";"


def read_numbers_from_file(filename: str) -> str:
    """
    Reads integer values line by line from the given file and
    returns them as a single string separated by SEPARATOR.
    Example: "12;45;7"
    """
    values_str = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                if values_str == "":
                    values_str = line
                else:
                    values_str += SEPARATOR + line

    return values_str


def analyse_numbers(values_str: str) -> str:
    """
    Takes a SEPARATOR-separated string of integers,
    calculates count, sum, greatest and average,
    and returns one CSV data row as a string:
    "count;sum;greatest;average"
    """
    parts = values_str.split(SEPARATOR)

    numbers = [int(p) for p in parts if p != ""]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    result_row = (
        f"{count}{SEPARATOR}"
        f"{total}{SEPARATOR}"
        f"{greatest}{SEPARATOR}"
        f"{average:.2f}"
    )
    return result_row


def main():
    print("Program starting.")
    print("This program analyses numbers from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading numbers from "{filename}".')
    print("Analysing numbers...")

    try:
        values_str = read_numbers_from_file(filename)

        if values_str == "":
            print("No numbers found in file.")
        else:
            result_row = analyse_numbers(values_str)
            print("Analysis complete!")
            print("Count;Sum;Greatest;Average")
            print(result_row)

    except FileNotFoundError:
        print("Error: File not found.")

    print("Program ending.")


if __name__ == "__main__":
    main()
