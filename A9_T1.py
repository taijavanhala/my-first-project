########################################################
# Task A9_T1
# Developer Taija Vanhala
# Date 2025-12-04
########################################################

import sys

def main() -> None:
    print("Program starting.\n")

    total = 0.0

    while True:
        user_input = input("Insert a floating-point value (0 to stop): ")

        # Stop condition before conversion attempt
        if user_input.strip() == "0":
            break

        try:
            value = float(user_input)
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(user_input))
            continue

        total += value

    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")

if __name__ == "__main__":
    main()
