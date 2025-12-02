WEEKDAYS: tuple[str, ...] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as file_handle:
            header = file_handle.readline()
            for line in file_handle:
                if line == "\n":
                    continue
                PRows.append(line.rstrip("\n"))
    except FileNotFoundError:
        print(f'Error: file "{PFilename}" not found.')

    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    weekdayTimestampAmount: list[int] = [0] * 7

    for row in PRows:
        for j, weekday in enumerate(WEEKDAYS):
            if row.startswith(weekday):
                weekdayTimestampAmount[j] += 1
                break

    for i, weekday in enumerate(WEEKDAYS):
        PResults.append(f" - {weekday} {weekdayTimestampAmount[i]} stamps")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()

    print("Program ending.")
    return None


main()
