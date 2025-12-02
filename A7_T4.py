from dataclasses import dataclass

DELIMITER: str = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as file_handle:
            # Skip header row
            header = file_handle.readline()

            # Read data rows
            for line in file_handle:
                # Skip completely empty lines
                if line == "\n":
                    continue

                # Remove newline and trailing spaces
                row = line.rstrip()

                # Split row into columns
                columns = row.split(DELIMITER)
                if len(columns) < 4:
                    continue

                # Create TIMESTAMP object and fill fields
                timestamp = TIMESTAMP()
                timestamp.weekday = columns[0]
                timestamp.hour = columns[1]
                timestamp.consumption = float(columns[2])
                timestamp.price = float(columns[3])

                PTimestamps.append(timestamp)

                # Clear temporary columns list (not mandatory, but clean)
                columns.clear()

    except FileNotFoundError:
        print(f'Error: file "{PFilename}" not found.')

    return None


def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in PTimestamps:
        total = ts.price * ts.consumption
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €"
        )
    return None


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []

    filename: str = input("Insert filename: ")

    readFile(filename, timestamps)
    displayTimestamps(timestamps)

    timestamps.clear()

    print("Program ending.")
    return None


main()
