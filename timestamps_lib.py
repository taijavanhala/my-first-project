# timestamps_lib.py
# Library for handling timestamps in A8_T4

from datetime import datetime

MONTHS: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

WEEKDAYS: list[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    """Read timestamps from file and store them into PTimestamps list."""
    PTimestamps.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                # Adjust the format string if your file format is different
                ts = datetime.strptime(line, "%Y-%m-%d %H:%M")
                PTimestamps.append(ts)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File contains invalid timestamp format.")


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    """Count timestamps that occur during the given year."""
    return sum(1 for ts in PTimestamps if ts.year == PYear)


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    """Count timestamps that occur during the given month name."""
    if not PTimestamps:
        return 0

    month_target = PMonth.strip().lower()
    return sum(
        1
        for ts in PTimestamps
        if MONTHS[ts.month - 1].lower() == month_target
    )


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    """Count timestamps that occur during the given weekday name."""
    if not PTimestamps:
        return 0

    weekday_target = PWeekday.strip().lower()
    return sum(
        1
        for ts in PTimestamps
        if WEEKDAYS[ts.weekday()].lower() == weekday_target
    )
