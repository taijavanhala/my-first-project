########################################################
# Task A9_T3
# Developer Taija Vanhala
# Date 2025-12-04
########################################################

import sys


def main() -> None:
    print("Program starting.")

    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.readlines()
    except FileNotFoundError:
        print("Error! File '{}' does not exist.".format(filename))
        sys.exit(1)

    # Print file header
    print(f"## {filename} ##")

    # Print file content exactly as in example
    for line in content:
        print(line.rstrip("\n"))

    print(f"## {filename} ##")

    print("Program ending.")


if __name__ == "__main__":
    main()
