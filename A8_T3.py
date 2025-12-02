# A8_T3.py
# Menu-driven program for analysing number files

from typing import List

def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def readValues() -> list[float]:
    filename = input("Insert filename: ")
    values: list[float] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # skip empty lines
                if line == "":
                    continue
                # convert to float
                values.append(float(line))
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File contains non-numeric data.")

    return values

def calculate_sum(values: list[float]) -> float:
    return sum(values)

def calculate_average(values: list[float]) -> float:
    if len(values) == 0:
        raise ValueError("No values to calculate average.")
    return sum(values) / len(values)

def main() -> None:
    print("Program starting.")

    values: list[float] = []

    while True:
        print()
        showOptions()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid choice.")
            continue

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            values = readValues()

        elif choice == 2:
            print(f"Amount of values {len(values)}")

        elif choice == 3:
            if len(values) == 0:
                print("No values read.")
            else:
                s = calculate_sum(values)
                print(f"Sum of values {s:.1f}")

        elif choice == 4:
            if len(values) == 0:
                print("No values read.")
            else:
                avg = calculate_average(values)
                print(f"Average of values {avg:.1f}")

        else:
            print("Invalid choice.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
