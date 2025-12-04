########################################################
# Task A9_T4
# Developer Taija Vanhala
# Date 2025-12-04
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")

    # Try convert to float
    try:
        value = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

    # Check range
    if value < TEMP_MIN or value > TEMP_MAX:
        raise Exception(f"{value} temperature out of range.")

    return value


def main() -> None:
    print("Program starting.")

    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except Exception as e:
        print(e)

    print("Program ending.")


if __name__ == "__main__":
    main()
