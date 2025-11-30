SEPARATOR = ";"


def read_numbers_from_file(filename: str) -> str:
    """
    Lukee tiedoston rivit, muuttaa ne numeroiksi (tekstinä) ja
    palauttaa ne yhtenä merkkijonona, jossa luvut erotellaan puolipisteellä.
    Esim: "12;45;7"
    """
    values_str = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                if values_str == "":
                    values_str = line
                else:
                    values_str += SEPARATOR + line

    return values_str


def analyse_numbers(values_str: str) -> str:
    """
    Ottaa merkkijonon, jossa numerot ovat muodossa "12;45;7",
    analysoi ne ja palauttaa tulosrivin CSV-muodossa:
    "Count;Sum;Greatest;Average"
    -> esim: "3;64;45;21.33"
    """
    parts = values_str.split(SEPARATOR)

    # Muutetaan luvut kokonaisluvuiksi
    numbers = []
    for p in parts:
        if p != "":
            numbers.append(int(p))

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    # Rakennetaan tulosrivi puolipisteillä
    result_row = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"
    return result_row


def main():
    print("Program starting.")
    print("This program analyses numbers from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading numbers from "{filename}".')
    print("Analysing numbers...")

    try:
        values_str = read_numbers_from_file(filename)

        if values_str == "":
            print("No numbers found in file.")
        else:
            result_row = analyse_numbers(values_str)
            print("Analysis complete!")
            # Otsikkorivi ja tulosrivi CSV-muodossa
            print("Count;Sum;Greatest;Average")
            print(result_row)

    except FileNotFoundError:
        print("Error: File not found.")

    print("Program ending.")


if __name__ == "__main__":
    main()
