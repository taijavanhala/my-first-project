########################################################
# Task A9_T7
# Developer Taija Vanhala
# Date 2025-12-07
########################################################

import sys
import os


def showHelp() -> None:
    print("Usage:")
    print("python A9_T7.py <source_file> <destination_file>")


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True

    # Check if destination file exists
    if os.path.exists(PDstFile):
        answer = input("Destination file exists. Overwrite (y/n)?: ").strip().lower()
        if answer != "y":
            proceed = False

    if proceed:
        try:
            with open(PSrcFile, "r", encoding="utf-8") as src:
                content = src.read()

            with open(PDstFile, "w", encoding="utf-8") as dst:
                dst.write(content)

        except Exception:
            print("Error while copying file.")
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

    # Argument count check
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        return

    src_file = sys.argv[1]
    dst_file = sys.argv[2]

    print(f'Source file "{src_file}"')
    print(f'Destination file "{dst_file}"')
    print(f'Copying file "{src_file}" to "{dst_file}".')

    copyFile(src_file, dst_file)

    print("Program ending.")


if __name__ == "__main__":
    main()
