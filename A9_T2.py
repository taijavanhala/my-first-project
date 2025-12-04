########################################################
# Task A9_T2
# Developer Taija Vanhala
# Date 2025-12-04
########################################################

import sys


def main() -> None:
    print("Program starting.")

    user_input = input("Insert exit code(0-255): ")

    try:
        exit_code = int(user_input)
    except ValueError:
        # Non-integer value → exit with 1
        sys.exit(1)

    # Restrict exit code range
    if exit_code < 0 or exit_code > 255:
        sys.exit(1)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
