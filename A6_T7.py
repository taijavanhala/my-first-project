# A6_T7 Messages from the Four Emperors

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PLACES = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace",
}


def rot13_char(ch: str) -> str:
    """Return ROT13 ciphered character for a single character."""
    if ch in LOWER_ALPHABETS:
        idx = LOWER_ALPHABETS.index(ch)
        return LOWER_ALPHABETS[(idx + 13) % 26]
    if ch in UPPER_ALPHABETS:
        idx = UPPER_ALPHABETS.index(ch)
        return UPPER_ALPHABETS[(idx + 13) % 26]
    return ch  # other characters unchanged


def rot13(text: str) -> str:
    """Cipher/decipher a full string using ROT13."""
    return "".join(rot13_char(ch) for ch in text)


def read_progress(filename: str = "player_progress.txt") -> tuple[int, int, str]:
    """
    Read player progress from file.
    Returns (current_location_id, next_location_id, ciphered_passphrase).
    If file does not exist, this function will raise an error.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]

    # First non-empty line is header, second is data row 0
    header = lines[0]  # not really used, but kept for clarity
    data_row = lines[1]

    parts = data_row.split(";")
    current_id = int(parts[0])
    next_id = int(parts[1])
    cipher_passphrase = parts[2]

    return current_id, next_id, cipher_passphrase


def append_cipher_line_to_progress(cipher_line: str, filename: str = "player_progress.txt") -> None:
    """Append the ciphered first line of the message into the progress file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(cipher_line + "\n")


def read_emperor_message(next_id: int, cipher_passphrase: str) -> list[str]:
    """
    Read the ciphered message file for the given next location id and passphrase.
    File is named: "{NextLocationId}_{PassPhrase}.gkg"
    Returns all lines (as a list of strings).
    """
    message_filename = f"{next_id}_{cipher_passphrase}.gkg"
    with open(message_filename, "r", encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]
    return lines


def save_plain_message(
    next_id: int,
    plain_passphrase: str,
    cipher_lines: list[str],
) -> None:
    """
    Save the ROT13-deciphered message into a new file:
    "{NextLocationId}-{PlainPassPhrase}.txt"
    """
    plain_lines = [rot13(line) for line in cipher_lines]
    out_filename = f"{next_id}-{plain_passphrase}.txt"

    with open(out_filename, "w", encoding="utf-8") as file:
        for line in plain_lines:
            file.write(line + "\n")


def main() -> None:
    print("Travel starting.")

    # 1. Read progress: where we are and where to go next
    current_id, next_id, cipher_passphrase = read_progress()

    current_place = PLACES.get(current_id, "unknown place")
    next_place = PLACES.get(next_id, "unknown place")

    # 2. Travel messages
    print(f"Currently at {current_place}.")
    print(f"Travelling to {next_place}...")
    print(f"...Arriving to the {next_place}.")
    print("Passing the guard at the entrance.")

    # 3. Shout passphrase (plain ROT13 version)
    plain_passphrase = rot13(cipher_passphrase)
    print(f"\"{plain_passphrase}!\"")

    # 4. Look for the message
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    print("[Game] Progress autosaved!")

    # 5. Read ciphered message file
    cipher_lines = read_emperor_message(next_id, cipher_passphrase)

    # Append first cipher line to progress file
    if cipher_lines:
        append_cipher_line_to_progress(cipher_lines[0])

    # 6. Decipher and save Emperor's message
    print("Deciphering Emperor's message...")
    save_plain_message(next_id, plain_passphrase, cipher_lines)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


if __name__ == "__main__":
    main()
