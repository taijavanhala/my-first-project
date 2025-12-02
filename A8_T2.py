# A8_T2.py
# Menu-controlled calculator program

from calculator import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))

def main() -> None:
    print("Program starting.")

    while True:
        print()
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            print(f"{a} + {b} = {add(a, b)}")

        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            print(f"{a} - {b} = {subtract(a, b)}")

        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            print(f"{a} * {b} = {multiply(a, b)}")

        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            try:
                print(f"{a} / {b} = {divide(a, b)}")
            except ZeroDivisionError:
                print("Cannot divide by zero.")

        else:
            print("Invalid choice.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
