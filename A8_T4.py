# A8_T4.py
# Menu-driven program for analysing timestamps by year, month and weekday

from datetime import datetime
from timestamps_lib import (
    MONTHS,
    WEEKDAYS,
    readTimestamps,
    calculateYears,
    calculateMonths,
    calculateWeekdays,
)


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def main() -> None:
    print("Program starting.")

    timestamps: list[datetime] = []

    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)

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
            try:
                year = int(input("Insert year: "))
            except ValueError:
                print("Invalid year.")
                continue

            amount = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}")

        elif choice == 2:
            month = input("Insert month: ")
            if month.strip() == "":
                print("Invalid month.")
                continue

            amount = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}")

        elif choice == 3:
            weekday = input("Insert weekday: ")
            if weekday.strip() == "":
                print("Invalid weekday.")
                continue

            amount = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}")

        else:
            print("Invalid choice.")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
